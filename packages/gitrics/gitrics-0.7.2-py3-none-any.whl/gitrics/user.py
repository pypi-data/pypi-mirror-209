import os
import requests

import colorgram

from glapi.connection import GitlabConnection
from glapi.user import GitlabUser
from PIL import Image

from gitrics import configuration
from gitrics.project.enrichment import convert_topics_to_percent, enrich_effort, enrich_foci, enrich_languages, enrich_membership, enrich_topics, extract_effort, prune_topics
from gitrics.utilities import configure_date_range

class gitricsUser(GitlabUser):
    """
    gitricsUser is a Gitlab User with opinionated enrichment for the gitrics ecosystem.
    """

    def __init__(self, id: str = None, username: str = None, user: dict = None, projects: list = None, connection: GitlabConnection = None, token: str = configuration.GITLAB_TOKEN, version: str = configuration.GITLAB_API_VERSION):
        """
        Args:
            connection (GitlabConnection): glapi connection
            id (string): GitLab Epic id
            projects (list): classes of GitlabProject
            token (string): GitLab personal access, ci, or deploy token
            user (dictionary): GitLab User
            username (string): Gitlab User username
            version (string): GitLab API version as base url
        """

        # initialize inheritance
        super(gitricsUser, self).__init__(
            connection=connection,
            id=id,
            token=token,
            user=user,
            username=username,
            version=version
        )

    def bin_projects(self, bin: str, projects: list = None, simple: bool = configuration.PROJECT_SIMPLE, visibility: str = configuration.VISIBILITY, membership: bool = configuration.PROJECT_MEMBERSHIP_ONLY, personal: bool = configuration.PROJECT_NAMESPACE_ONLY) -> dict:
        """
        Organize projects by membership access level.

        Args:
            bin (enum): access |
            membership (boolean): TRUE if api should query specific to the user ttached to the access token
            personal (boolean): TRUE if api should return namespace (personal) user projects only
            projects (list): objects where each is a Gitlab Project
            simple (boolean): TRUE if api return should be minimal
            visibility (enum): internal | private | public

        Returns:
            A dictionary where keys are the bin label and corresponding values are lists of dictionaries where each is a Gitlab project which fits the bin criteria.
        """

        result = dict()

        if bin == "access":

            # determine maximum access level
            max_level = int(max(configuration.USER_ACCESS_LEVELS.keys()) / 10)
            min_level = int(min(configuration.USER_ACCESS_LEVELS.keys()) / 10)

            result = { configuration.USER_ACCESS_LEVELS[k]: list() for k in configuration.USER_ACCESS_LEVELS }
            tracked = list()

            # check if project provided
            if projects and "permissions" in projects[0]:

                # loop through projects
                for d in projects:

                    # check if group or project grants access
                    has_group_permissions = d["permissions"]["group_access"]
                    has_project_permissions = d["permissions"]["project_access"]

                    # has some permission
                    if has_project_permissions:
                        result[configuration.USER_ACCESS_LEVELS[d["permissions"]["project_access"]["access_level"]]].append(d)
                    elif has_group_permissions:
                        result[configuration.USER_ACCESS_LEVELS[d["permissions"]["group_access"]["access_level"]]].append(d)

            else:

                # determine what order to extract projects in
                # based on how gitlab exposes user access level
                # we have to loop through different queries to assemble by user access
                for digit in reversed(range(min_level, max_level + 1)):

                    filtered = list()
                    level = digit * 10

                    # get projects user is a member of
                    api_results = self.extract_projects(
                        access=level,
                        membership=membership,
                        personal=personal,
                        simple=simple,
                        visibility=visibility
                    )

                    # skip maximum level since all those project are valid to that access level
                    if digit != max_level:

                        # remove projects of higher levels
                        filtered = [d for d in api_results if d["id"] not in tracked]

                    # add ids to track
                    for d in api_results:
                        if d["id"] not in tracked:
                            tracked.append(d["id"])

                    # set value in map
                    result[configuration.USER_ACCESS_LEVELS[level]] = api_results if digit == max_level else filtered

        return result

    def determine_user_connection(self, projects: list, date_start: str, date_end: str, user_id: int):
        """
        Get user issue and merge request connections.

        Args:
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value
            projects (list): dictionaries where each represents a Gitlab Project
            user_id (integer): unique identifier
        """

        # get created by and assigned to user
        issues_assigned = self.extract_own_issues(date_start, date_end, type="assigned_to_me")
        issues_created = self.extract_own_issues(date_start, date_end)
        merge_requests_assigned = self.extract_own_merge_requests(date_start, date_end, type="assigned_to_me")
        merge_requests_created = self.extract_own_merge_requests(date_start, date_end)

        # prune to remove created by and assigned to same user
        pruned_issues = self.prune_issues_or_merge_requests(issues_assigned + issues_created, user_id)
        pruned_merge_requests = self.prune_issues_or_merge_requests(merge_requests_assigned + merge_requests_created, user_id)

        # format as key/value map of user id to related user object
        issues = self.format_issues_or_merge_requests(pruned_issues, user_id)
        merge_requests = self.format_issues_or_merge_requests(pruned_merge_requests, user_id)

        # combine totals for issues/merge requests
        count_issues_mergerequests = dict()

        # loop through user ids from issues
        for user_id in issues:

            # check for key in combined
            if user_id not in count_issues_mergerequests:

                # add key/update attributes
                count_issues_mergerequests[user_id] = issues[user_id]
                count_issues_mergerequests[user_id]["member_only"] = False

        # loop through user ids from merge requests
        for user_id in merge_requests:

            # check for key in combined
            if user_id not in count_issues_mergerequests:

                # add key/update attributes
                count_issues_mergerequests[user_id] = { "count": 0, "member_only": False }

            # now that key exists sum values not yet captured
            count_issues_mergerequests[user_id]["count"] += merge_requests[user_id]["count"]

        # extract and format active project members
        # filtering out users which match self
        level1_connections = [
            {
                "id": d["id"],
                "members": [
                    {
                        "id": m["id"],
                        "name": m["name"],
                        "avatar_url": m["avatar_url"],
                        "web_url": m["web_url"]
                    } for m in d["members"]
                    if m["state"] == "active" and m["id"] != user_id
                ]
            } for d in projects
        ]

        # flatten
        level1_connections_flat = [x for y in [d["members"] for d in level1_connections] for x in y]

        # remove duplicates
        level1_connections = [dict(t) for t in {tuple(d.items()) for d in level1_connections_flat}]

        # loop through first level connections
        for user in level1_connections:

            # check if captured in combined connection counts
            if user_id not in count_issues_mergerequests:

                # add user and update attribute for membership
                count_issues_mergerequests[user_id] = {
                    "user": user,
                    "count": 0,
                    "member_only": True
                }

                # add value to existing
                count_issues_mergerequests[user_id]["count"] += 1

        return count_issues_mergerequests

    def enrich_projects(self, projects: list, foci: dict = None) -> list:
        """
        Enrich projects with foci, languages, and topics.

        Args:
            foci (dictionary): key/values where each key is a focus and corresponding value is an array of strings representing alternate spellings or other variations
            projects (list): dictionaries of GitLab Project

        Returns:
            A list of dictionaries where each represents an enriched GitLab Project.
        """

        # add languages
        projects = enrich_languages(projects, self.connection)

        # add topics
        projects = enrich_topics(projects)

        # add members
        projects = enrich_membership(projects, self.connection)

        # add foci
        projects = enrich_foci(projects, foci)

        # add effort
        projects = enrich_effort(projects)

        # try to assign effort name if a known effort name shows up in topic list
        projects = extract_effort(projects)

        # clean up topics to remove effort and foci keys
        projects = prune_topics(projects, foci)

        # convert topic counts to percents
        return convert_topics_to_percent(projects)

    def extract_activity(self, date_start: str = None, date_end: str = None) -> tuple:
        """
        Determine user activity from extracted Gitlab Event data.

        Args:
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value

        Returns:
            A tuple of (all events, coding events, collaboration events) where each tuple item is a list of dictionaries and each is a Gitlab Event.
        """

        # convert time
        dt_start, dt_end = configure_date_range(
            date_end=date_end,
            date_start=date_start
        )

        # convert time
        count_days = (dt_end - dt_start).days

        # because the named action is different than the param to query for the action type
        # need to loop through sets of actions to retain the grouped label
        events = dict()

        # loop through action types
        for action in configuration.ACTIVITY_TYPES:

            # get events
            e = self.extract_events(
                actions=[action],
                date_end=date_end,
                date_start=date_start
            )

            # update collection
            events[action] = e if e else list()

        # coding events
        events_coding = events["pushed"] + events["merged"]

        # collaboration events
        events_collaboration = events["approved"] + events["closed"] + events["commented"] + events["created"] + events["updated"]

        return (events, events_coding, events_collaboration)

    def extract_efforts(self, projects: list, events: list) -> dict:
        """
        Organize projects into efforts and aggregate/organize data across projects.

        Args:
            events (list): dictionaries where each is a Gitlab Event
            projects (list): dictionaries where each is a GitLab Project

        Returns:
            A dictionary of key/value pairs where the key is an effort label and corresponding value is a dictionary of values representing the effort.
        """

        # enrich projects with events
        for p in projects:
            p["events"] = [e for e in events if e["project_id"] == p["id"]]
            p["member_ids_by_focus"] = {}
            p["member_ids_with_events"] = [m["id"] for m in p["members"] if m["id"] in [e["author_id"] for e in p["events"]]]

        # the x for y in [] for x in y sytnax is flattening a 2D array into 1D
        result = {
            k: {
                "events": [
                    x for y in [
                        p["events"] for p in projects if p["effort"] == k
                    ] for x in y
                ],
                "foci": list(set([
                    x for y in [
                        p["foci"] for p in projects if p["effort"] == k
                    ] for x in y
                ])),
                "foci_event_counts": {
                    f: sum([
                        len(p["events"]) for p in projects
                            if p["effort"] == k
                            and len(p["foci"]) > 0
                            and f in p["foci"]
                    ])
                    for f in list(set([
                        x for y in [
                            p["foci"] for p in projects if p["effort"] == k and len(p["events"]) > 0
                        ] for x in y
                    ]))
                },
                "foci_with_events": list(set([
                    x for y in [
                        p["foci"] for p in projects if p["effort"] == k and len(p["events"]) > 0
                    ] for x in y
                ])),
                "members": [
                    dict(t) for t in
                    {
                        tuple(d.items()) for d in [
                            {
                                "avatar_url": d["avatar_url"],
                                "id": d["id"],
                                "name": d["name"]
                            } for d in [
                                x for y in [
                                    p["members"] for p in projects if p["effort"] == k
                                ] for x in y
                            ]
                        ]
                    }
                ],
                "member_ids": list(set([
                    x for y in [
                        [
                            m["id"] for m in p["members"]
                        ] for p in projects if p["effort"] == k
                    ] for x in y
                ])),
                "member_ids_by_focus": {
                    f: list(set([
                        x for y in [
                            [m["id"] for m in p["members"]]
                            for p in projects if p["effort"] == k and f in p["foci"]
                        ] for x in y
                    ]))
                    for f in list(set([
                        x for y in [
                            p["foci"] for p in projects if p["effort"] == k
                        ] for x in y
                    ]))
                },
                "member_ids_with_events": list(set([
                    x for y in [
                        p["member_ids_with_events"] for p in projects if p["effort"] == k
                    ] for x in y
                ])),
                "member_ids_with_foci": list(set([
                    x["id"] for y in [
                        p["members"] for p in projects if p["effort"] == k and len(p["foci"]) > 0
                    ] for x in y
                ])),
                "project_ids": list(set([
                    p["id"] for p in projects if p["effort"] == k
                ])),
                "project_ids_with_events": list(set([
                    x["project_id"] for y in [
                        p["events"] for p in projects if p["effort"] == k
                    ] for x in y
                ])),
                "project_ids_by_foci": {
                    f: [
                        p["id"] for p in projects if p["effort"] == k and f in p["foci"]
                    ]
                    for f in list(set([
                        x for y in [
                            p["foci"] for p in projects if p["effort"] == k
                        ] for x in y
                    ]))
                },
                "project_ids_with_foci": list(set([
                    p["id"] for p in projects if p["effort"] == k and len(p["foci"]) > 0
                ]))
            }
            for k in list(set([d["effort"] for d in projects]))
        }

        # only keep efforts with events and foci
        result = { k: result[k] for k in result if len(result[k]["events"]) > 0 and len(result[k]["foci"]) > 0 }

        return result

    def extract_own_issues(self, date_start: str, date_end: str, type: str = "created_by_me") -> list:
        """
        Extract user-specific issue data created by user.

        Args:
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value
            type (enum): created_by_me || assigned_to_me

        Returns:
            A list of dictionaries where each represents a Gitlab Issue.
        """
        return self.extract_issues(
            date_end=date_end,
            date_start=date_start,
            scope=type
        )

    def extract_own_merge_requests(self, date_start: str, date_end: str, type: str = "created_by_me") -> list:
        """
        Extract user-specific merge request data created by user.

        Args:
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value
            type (enum): created_by_me || assigned_to_me

        Returns:
            A list of dictionaries where each represents a Gitlab Merge Request.
        """
        return self.extract_merge_requests(
            date_end=date_end,
            date_start=date_start,
            scope=type
        )

    def extract_languages(self, projects: list) -> dict:
        """
        Extract coding languages associated with user projects.

        Args:
            projects (list): dictionaries of Gitlab Projects

        Returns:
            A dictionary of key/value pairs where each key is a programming language and corresponding value is an integer representing the percent of all languages that single value represents.
        """

        result = dict()

        # loop through projects
        for project in projects:

            # loop through languages
            for language in project["languages"]:

                # check if tracked already
                if language not in result:

                    # add it
                    result[language] = { "percent": 0 }

                # sum percents
                result[language]["percent"] += project["languages"][language]
                result[language]["percent_aggregate"] = result[language]["percent"] / (len(projects) * 100)

        return result

    def extract_topics(self, projects: list) -> dict:
        """
        Extract project tags (topics) associated with user projects.

        Args:
            projects (list): dictionaries of Gitlab Projects

        Returns:
            A dictionary of key/value pairs where each key is a topic and corresponding value is an integer representing the percent of all topics that single value represents.
        """

        result = dict()

        # loop through projects
        for project in projects:

            # loop through topics
            for topic in project["topics"]:

                # check if tracked already
                if topic not in result:

                    # add it
                    result[topic] = { "percent": 0 }

                # sum percents
                result[topic]["percent"] += project["topics"][topic]

        # loop through topics
        for topic in result:

            # sum percents
            result[topic]["percent_aggregate"] = result[topic]["percent"] / sum([result[k]["percent"] for k in result])

        return result

    def format_issues_or_merge_requests(self, items: list, user_id: int) -> dict:
        """
        Generate key/value map for user id to correlated user objects to represent connected GitLab Users.

        Args:
            items (list): dictionaries where each is a GitLab Merge Request or Issue
            user_id (integer): unique identifier

        Returns:
            A dictionary where each key is a user id representing an author or assignee the core user has interaction with and the corresponding values are the count of connections and the GitLab User object for the connected user id.
        """

        result = dict()

        # check for items
        if items:

            # loop through GitLab objects
            for item in items:

                # pull current ids
                assignee_id = item["assignee"]["id"] if item["assignee"] else None
                author_id = item["author"]["id"] if item["author"] else None

                # if there is an assignee and it's not the core user
                if assignee_id and assignee_id != user_id:

                    # check for existing key
                    if assignee_id not in result:

                        # add key
                        result[assignee_id] = {
                            "count": 0,
                            "user": item["assignee"]
                        }

                    # iterate count
                    result[assignee_id]["count"] += 1

                # if there is an author and it's not the core user
                if author_id and author_id != user_id:

                    # check for existing key
                    if author_id not in result:

                        # add key
                        result[author_id] = {
                            "count": 0,
                            "user": item["author"]
                        }

                    # iterate count
                    result[author_id]["count"] += 1

        return result

    def generate_color(self, avatar_url: str = None) -> list:
        """
        Generate color palette based off user avatar.

        Args:
            avatar_url (string): Gitlab User avatar url

        Returns:
            A list of colorgram objects where each represents an extracted swatch from the user avatar.
        """

        # attempt to extract color based on user avatar
        try:

            CERT_IS_PRESENT = "REQUESTS_CLIENT_CERT" in os.environ and os.environ["REQUESTS_CLIENT_CERT"] and os.environ["REQUESTS_CLIENT_CERT"] != ""
            KEY_IS_PRESENT = "REQUESTS_CLIENT_KEY" in os.environ and os.environ["REQUESTS_CLIENT_KEY"] and os.environ["REQUESTS_CLIENT_KEY"] != ""

            # get url from self or param
            if not avatar_url and self.user:
                avatar_url = self.user["avatar_url"]

            # http request for avatar
            avatar = requests.get(avatar_url, cert=(os.environ["REQUESTS_CLIENT_CERT"], os.environ["REQUESTS_CLIENT_KEY"]), stream=True) if (CERT_IS_PRESENT and KEY_IS_PRESENT) else requests.get(avatar_url, stream=True)

            # pull colors
            colors = colorgram.extract(Image.open(avatar.raw), 6)

        except Exception as e:
            raise e

        return colors

    def prune_issues_or_merge_requests(self, items: list, user_id: int) -> list:
        """
        Prune items which are both created by and assigned to user.

        Args:
            items (list): dictionaries where each is a Gitlab Merge Request or Issue
            user_id (integer): unique identifier

        Returns:
            A list of dictionaries where each represents a Gitlab Merge Request or Issue.
        """

        result = list()

        # check for items
        if items:

            # filter out created by user and assigned to user
            created_filtered = [
                d for d in items
                if d["assignee"] and d["assignee"]["id"] != user_id
              ]

            # filter out created by user and assigned to user
            assigned_filtered = [
                d for d in items
                if d["author"] and d["author"]["id"] != user_id
            ]

            # update result
            result = created_filtered + assigned_filtered

        return result

    def prune_projects(self, projects: list, filter_for_events: list = None, filter_project_ids: list = configuration.PROJECT_FILTER_IDS, filter_project_names: list = configuration.PROJECT_FILTER_NAMES, filter_project_names_startswith: list = configuration.PROJECT_FILTER_NAMES_STARTSWITH, filter_group_namespaces: list = configuration.PROJECT_FILTER_GROUP_NAMESPACES) -> list:
        """
        Prune projects.

        Args:
            filter_for_events (list): integers where each is a Gitlab project id with events
            filter_group_namespaces (list): strings where each is a Gitlab Group full namespace
            filter_project_ids (list): integers where each is a Gitlab Project id
            filter_project_names (list): strings where each is a Gitlab Project name
            filter_project_names_startswith (list): strings where each is a prefix of a Gitlab Project name
            projects (list): dictionaries where each is a Gitlab Project

        Returns:
            A list of dictionaries where each represents a Gitlab project.
        """

        # filter by explicit id
        result = [d for d in projects if d["id"] not in filter_project_ids]

        # filter by explicit name
        result = [d for d in result if d["name"].lower() not in filter_project_names]

        # loop through project name prefixes
        for prefix in filter_project_names_startswith:

            # filter by name starts with
            result = [d for d in result if not d["name"].startswith(prefix)]

        # loop through group namespaces
        for namespace in filter_group_namespaces:

            # loop through group name spaces
            result = [d for d in result if namespace not in  d["path_with_namespace"]]

        # filter for projects with events
        if filter_for_events:
            result = [d for d in result if d["id"] in filter_for_events]

        return result
