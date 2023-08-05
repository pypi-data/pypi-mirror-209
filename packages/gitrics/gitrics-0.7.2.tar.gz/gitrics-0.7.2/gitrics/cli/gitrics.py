#!/usr/bin/env python3

import argparse
import datetime
import json
import math
import os
import sys

from argparse import Namespace
from collections import Counter

from colorama import Back, Fore, init, Style
from glapi.connection import GitlabConnection

from gitrics import configuration
from gitrics.user import gitricsUser
from gitrics.utilities import configure_date_range

class gitricsCli(object):

    def __str__(self):
        init(autoreset=True)
        print(Fore.CYAN + "gitrics CLI complete")

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="gitrics CLI",
            usage="""gitrics [<args>] <command>

The most commonly used gitrics commands are:
   this     Do this and stuff
"""
        )

        # define optional values
        self.parser.add_argument("--accent-color",
            type=str,
            default=None,
            help="CSS-valid color value."
        )
        self.parser.add_argument("--access",
            type=str,
            default=configuration.USER_ACCESS_INPUT,
            help="Minimum access level of a user on Gitlab Groups or Projects: %s" % " | ".join([configuration.USER_ACCESS_LEVELS[k] for k in configuration.USER_ACCESS_LEVELS])
        )
        self.parser.add_argument("--api",
            type=str,
            default=configuration.GITLAB_API_VERSION,
            help="GitLab instance-specific API version in the form of a base URL."
        )
        self.parser.add_argument("--end",
            type=str,
            default=configuration.DATE_END,
            help="ISO 8601 date value"
        )
        self.parser.add_argument("--filter-groups",
            type=str,
            default=configuration.PROJECT_FILTER_GROUP_NAMESPACES,
            help="Comma-delimited Gitlab Group namespaces"
        )
        self.parser.add_argument("--filter-project-ids",
            type=str,
            default=configuration.PROJECT_FILTER_IDS,
            help="Comma-delimited Gitlab Project ids"
        )
        self.parser.add_argument("--filter-project-names",
            type=str,
            default=configuration.PROJECT_FILTER_NAMES,
            help="Comma-delimited Gitlab Project names"
        )
        self.parser.add_argument("--filter-project-names-startswith",
            type=str,
            default=configuration.PROJECT_FILTER_NAMES_STARTSWITH,
            help="Comma-delimited Gitlab Project name prefixes"
        )
        self.parser.add_argument("--foci",
            type=argparse.FileType("r", encoding="UTF-8"),
            help="JSON key/values where each key is a focus and corresponding value is an array of strings representing alternate spellings or other variations"
        )
        self.parser.add_argument("--start",
            type=str,
            default=configuration.DATE_START,
            help="ISO 8601 date value"
        )
        self.parser.add_argument("--instance-name",
            type=str,
            default=configuration.GITLAB_NAME,
            help="Label for GitLab instance"
        )
        self.parser.add_argument("--instance-url",
            type=str,
            default=configuration.GITLAB_URL,
            help="GitLab instance url"
        )
        self.parser.add_argument("--output",
            type=str,
            default=configuration.DIRECTORY_PATH_OUTPUT,
            help="Directory location to write data files to."
        )
        self.parser.add_argument("--only-membership-projects",
            action=argparse.BooleanOptionalAction,
            help="Restrict results to projects specific to the user attached to the TOKEN"
        )
        self.parser.add_argument("--only-personal-projects",
            action=argparse.BooleanOptionalAction,
            help="Restrict results to user namespace"
        )
        self.parser.add_argument("--simple",
            action=argparse.BooleanOptionalAction,
            help="Restrict results to simplified key/value pairs"
        )
        self.parser.add_argument("--token",
            type=str,
            default=configuration.GITLAB_TOKEN,
            help="GitLab Personal Access Token or Deploy Token to authenticate API requests."
        )
        self.parser.add_argument("--visibility",
            type=str,
            default=configuration.VISIBILITY,
            help="What visibility level (internal, public, private) to query for from Gitlab"
        )

        # define subcommands
        self.subparser = self.parser.add_subparsers(dest="command")
        self.subparser.add_parser("user")

        # exclude the rest of the args
        self.opt, unknown = self.parser.parse_known_args()

        # show user full help if no subcommand
        if self.opt.command is None:
            print("Unrecognized command")
            self.parser.print_help()
            exit(1)

        # use dispatch pattern to invoke method with same name
        getattr(self, self.opt.command)()

    def user(self, date_start: str = None, date_end: str = None, directory_path_output: str = None, instance_api: str = None, instance_name: str = None, instance_token: str = None, instance_url: str = None, project_membership_only: bool = configuration.PROJECT_MEMBERSHIP_ONLY, project_namespace_only: bool = configuration.PROJECT_NAMESPACE_ONLY, project_filter_group_namespaces: list = None, project_filter_ids: list = None, project_filter_names: list = None, project_filter_names_startswith: list = None, project_simple: bool = None, project_visibility: str = None, user_id: str = None, accent_color: str = None):
        """
        Generate complete gitrics dataset.

        Args:
            accent_color (string): CSS-valid color value
            date_end (string): iso 8601 date value
            date_start (string): iso 8601 date value
            directory_path_output (string): directory path to output data files to
            instance_api (string): GitLab api url
            instance_name (string): label for GitLab instance
            instance_token (string): GitLab access or deploy token
            instance_url (string): web url for instance home
            project_filter_group_namespaces (list): strings where each is a Gitlab Group complete namespace
            project_filter_ids (list): integers where each is a Gitlab Project id
            project_filter_names (list): strings where each is a Gitlab Project name
            project_filter_names_startswith (list): strings where each is a prefix of a Gitlab Project name
            project_namespace_only (boolean): TRUE if api should return namespace (personal) user projects only
            project_simple (boolean): TRUE if api results have reduced set of key/value pairs
            project_visibility (enum): internal | private | public
            user_id (integer): GitLab user id
        """
        parser = argparse.ArgumentParser(
            description="Generate metadata about GitLab, the dataset, and the user"
        )

        # required parameters
        parser.add_argument("--user",
            type=str,
            required=True,
            help="GitLab user id."
        )

        # now that we're inside a subcommand, ignore the first
        args, unknown = parser.parse_known_args()

        # parse arguments and merge with top-level args
        opt = Namespace(**vars(self.opt), **vars(args))

        # get values

        # timing
        date_end = date_end if date_end else opt.end
        date_start = date_start if date_start else opt.start

        # filesystem
        directory_path_output = directory_path_output if directory_path_output else opt.output
        foci_reference = json.loads(opt.foci.read()) if opt.foci else None

        # instance
        instance_api = instance_api if instance_api else opt.api
        instance_name = instance_name if instance_name else opt.instance_name
        instance_token = instance_token if instance_token else opt.token
        instance_url = instance_url if instance_url else opt.instance_url

        # projects
        project_filter_group_namespaces = project_filter_group_namespaces if project_filter_group_namespaces else ([d.strip().lower() for d in opt.filter_groups.split(",")] if isinstance(opt.filter_groups, str) else list())
        project_filter_ids = project_filter_ids if project_filter_ids else ([int(d.strip()) for d in opt.filter_project_ids.split(",")] if isinstance(opt.filter_project_ids, str) else list())
        project_filter_names = project_filter_names if project_filter_names else ([d.strip().lower() for d in opt.filter_project_names.split(",")] if isinstance(opt.filter_project_names, str) else list())
        project_filter_names_startswith = project_filter_names_startswith if project_filter_names_startswith else ([d.strip().lower() for d in opt.filter_project_names_startswith.split(",")] if isinstance(opt.filter_project_names_startswith, str) else list())
        project_membership_only = project_membership_only if project_membership_only else bool(opt.only_membership_projects)
        project_namespace_only = project_namespace_only if project_namespace_only else bool(opt.only_personal_projects)
        project_simple = project_simple if project_simple else bool(opt.simple)
        project_visibility = project_visibility if project_visibility else opt.visibility

        # users
        user_id = user_id if user_id else opt.user

        # convert time
        dt_start, dt_end = configure_date_range(date_end=date_end, date_start=date_start)

        # render
        accent_color = accent_color if accent_color else opt.accent_color

        # report metadata
        with open(os.path.join(directory_path_output, "metadata.json"), "w") as f:
            f.write(json.dumps({
                "date_end": date_end,
                "date_publish": datetime.datetime.now().isoformat(),
                "date_start": date_start,
                "gitlab_name": instance_name,
                "gitlab_url": instance_url,
                "public_or_private": "public" if project_visibility.lower() == "internal" or project_visibility.lower() == "public" else "private",
                "visibility": project_visibility
            }))

        # ensure requirements are met
        try:
            gc = GitlabConnection(token=instance_token, version=instance_api)
            gc.query("/version")
        except Exception as error:
            raise print(Fore.RED + error)

        # initialize user
        gu = gitricsUser(id=user_id, token=instance_token, version=instance_api)

        # user metadata
        with open(os.path.join(directory_path_output, "user.json"), "w") as f:
            f.write(json.dumps({
                "id": gu.user["id"],
                "name": gu.user["name"],
                "avatar_url": gu.user["avatar_url"],
                "web_url": gu.user["web_url"],
                "email": gu.user["public_email"] if gu.user["public_email"] != str() else None
            }))

        # user namespace + group projects
        user_projects = gu.prune_projects(
            projects=gu.extract_projects(
                membership=project_membership_only,
                personal=project_namespace_only,
                simple=project_simple,
                visibility=project_visibility
            ),
            filter_group_namespaces=project_filter_group_namespaces,
            filter_project_ids=project_filter_ids,
            filter_project_names=project_filter_names,
            filter_project_names_startswith=project_filter_names_startswith
        )

        # bin projects by user access level
        projects_binned_by_access = gu.bin_projects("access", projects=user_projects)

        # enrich projects with langauges/topics/foci/effort/membership
        projects = gu.enrich_projects(user_projects, foci_reference)

        # find out how many private projects the user has
        # regardless of namespace or public
        total_projects_private = len(gc.paginate("projects", { "visibility": "private"}))

        # calculate simple project totals
        total_projects = len(projects)
        total_projects_developer = len(projects_binned_by_access["developer"])
        total_projects_maintainer = len([d for d in projects_binned_by_access["maintainer"] if gu.user["username"] not in d["path_with_namespace"]])
        total_projects_personal = len([d for d in projects_binned_by_access["maintainer"] if gu.user["username"] in d["path_with_namespace"]])
        total_projects_public = total_projects - total_projects_personal
        total_projects_owner = len(projects_binned_by_access["owner"])

        # calculate public to personal
        public_personal_difference = total_projects_public -  total_projects_personal;
        public_personal_average = total_projects / 2;
        ratio_of_public_personal_difference_average = public_personal_difference / public_personal_average;
        public_private_percent_difference = ratio_of_public_personal_difference_average * 100

        # generate dictionary of role values
        d = {
            "developer": total_projects_developer,
            "maintainer": total_projects_maintainer,
            "owner": total_projects_owner
        }

        # find largest role percent
        count_role_percent = Counter(d)
        greatest_percent_role = max(count_role_percent, key=count_role_percent.get)

        # add project types to roles
        d["personal"] = total_projects_personal
        d["private"] = total_projects_private
        d["public"] = total_projects_public

        # write stats to file
        with open(os.path.join(directory_path_output, "membership.json"), "w") as f:
            f.write(json.dumps({
                "stats": {
                    "difference_public_to_personal": public_personal_difference,
                    "greatest_percent_role": greatest_percent_role,
                    "percent_developer": int(round(total_projects_developer / total_projects_public) * 100) if total_projects_public > 0 else None,
                    "percent_difference_public_to_personal": int(round(public_private_percent_difference)),
                    "percent_maintainer": int(round(total_projects_maintainer / total_projects_public) * 100) if total_projects_public > 0 else None,
                    "percent_owner": int(round(total_projects_owner / total_projects_public) * 100) if total_projects_public > 0 else None,
                    "percent_personal": int(round((total_projects_personal / total_projects) * 100)) if total_projects_public > 0 else None,
                    "percent_public": int(round((total_projects_public / total_projects) * 100)) if total_projects > 0 else None,
                    "count_projects": total_projects
                },
                "data": d
            }))

        # coverage metadata
        with open(os.path.join(directory_path_output, "coverage.json"), "w") as f:
            f.write(json.dumps({
                "stats": {
                    "percent_projects_coverage": int(round(total_projects_public / (total_projects + total_projects_private) * 100))
                }
            }))

        # extract color from avatar if present
        avatar_color = gu.generate_color()

        # generate css of color palette based on user avatar
        with open(os.path.join(directory_path_output, "visualization.scss"), "w", encoding="utf-8") as f:
            f.write("%s" % "\n".join([
            "$visualization%s: %s;" % (
                i + 1,
                "rgb(%s, %s, %s)" % (
                    d.rgb.r,
                    d.rgb.g,
                    d.rgb.b
                )
            ) for i, d in enumerate(avatar_color)
            ]))

            # if accent color provided add it last
            # to overwrite auto generated color
            if accent_color:
                f.write("$visualization%s: %s;" % (
                    len(avatar_color),
                    accent_color
                ))

        # user connections
        count_issues_mergerequests = gu.determine_user_connection(user_projects, date_start, date_end, user_id)

        # write connections to file
        with open(os.path.join(directory_path_output, "connections.json"), "w") as f:
            f.write(json.dumps({
                "stats": dict(),
                "data": count_issues_mergerequests
            }))

        # languages
        languages = gu.extract_languages(user_projects)

        # write languages to file
        with open(os.path.join(directory_path_output, "languages.json"), "w") as f:
            f.write(json.dumps({
                "stats": {
                    "count_projects": len(user_projects)
                },
                "data": {k: (languages[k]["percent_aggregate"] * 100) for k in languages}
            }))

        # topics
        topics = gu.extract_topics(user_projects)

        # write topics to file
        with open(os.path.join(directory_path_output, "topics.json"), "w") as f:
            f.write(json.dumps({
                "stats": {
                    "count_projects": len(user_projects)
                },
                "data": {k: (topics[k]["percent_aggregate"] * 100) for k in topics}
            }))

        # generate activity data
        events, events_coding, events_collaboration = gu.extract_activity(date_start, date_end)

        # flatten all events
        events_flat = [item for sublist in [events[k] for k in events] for item in sublist]

        # totals
        total_events_coding = len(events_coding)
        total_events_collaboration = len(events_collaboration)
        total_projects_with_events = len(list(set([d["project_id"] for d in events_flat])))

        # get common factor
        event_type_common_factor = math.gcd(total_events_coding, total_events_collaboration) if math.gcd(total_events_coding, total_events_collaboration) > 0 else 1

        # get activity stats
        count_activity_types = count_activity_types = { k: sum([len(events[a]) for a in configuration.ACTIVITY_TYPES]) for k in configuration.ACTIVITY_TYPES }

        # count date occurances in events
        date_occurances_in_events = [d["created_at"].split("T")[0] for d in events_flat]
        date_occurance_count = Counter(date_occurances_in_events)

        # convert time
        count_days = (dt_end - dt_start).days

        # write activity to file
        with open(os.path.join(directory_path_output, "activity.json"), "w") as f:
            f.write(json.dumps({
                "stats": {
                    "average_coding_per_day": int(round(sum([count_activity_types[k] for k in count_activity_types if k in configuration.ACTIVITY_TYPE_CODING]) / count_days)),
                    "average_coding_per_project": int(round(sum([count_activity_types[k] for k in count_activity_types if k in configuration.ACTIVITY_TYPE_CODING]) / total_projects_with_events)) if total_projects_with_events > 0 else 0,
                    "average_collaboration_per_day": int(round(sum([count_activity_types[k] for k in count_activity_types if k in configuration.ACTIVITY_TYPE_COLLABORATION]) / count_days)),
                    "average_collaboration_per_project": int(round(sum([count_activity_types[k] for k in count_activity_types if k in configuration.ACTIVITY_TYPE_COLLABORATION]) / total_projects_with_events)) if total_projects_with_events > 0 else 0,
                    "max_activity_date_count": date_occurance_count.most_common(1)[0][1] if len(date_occurance_count) > 0 else None,
                    "max_activity_date": date_occurance_count.most_common(1)[0][0] if len(date_occurance_count) > 0 else None,
                    "rate_collaboration_per_code": "%s:%s" % (
                        int(round(total_events_collaboration / event_type_common_factor)),
                        int(round(total_events_coding / event_type_common_factor))
                    ),
                    "total": len(events_flat)
                },
                "data": {
                    "coding": [
                        {
                            "date": d["created_at"],
                            "value": 1,
                            "type": "coding"
                        } for d in events_coding
                    ],
                    "collaboration": [
                        {
                            "date": d["created_at"],
                            "value": 1,
                            "type": "collaboration"
                        } for d in events_collaboration
                    ]
                }
            }))

        # organize projects into efforts
        efforts = gu.extract_efforts(projects, events_flat)

        # get across all efforts
        all_foci = list(set([
            x for y in [
                efforts[k]["foci"] for k in efforts
            ] for x in y
        ]))
        all_member_ids_with_events = list(set([
            x for y in [
                efforts[k]["member_ids_with_events"] for k in efforts
            ] for x in y
        ]))

        # counts
        effort_event_counts_with_foci = {
            k: len([
                e for e in efforts[k]["events"]
                    if e["author_id"] in efforts[k]["member_ids_with_foci"]
                    and e["project_id"] in efforts[k]["project_ids_with_foci"]
            ])
            for k in efforts
        }
        foci_event_counts = {
            f: sum([
                efforts[k]["foci_event_counts"][f]
                for k in efforts
                    if f in efforts[k]["foci_event_counts"]
            ])
            for f in all_foci
        }
        total_events_with_foci = sum([foci_event_counts[k] for k in foci_event_counts])

        # averages
        average_activity_per_effort = int(round(total_events_with_foci / len(effort_event_counts_with_foci))) if len(effort_event_counts_with_foci) > 0 else None
        average_activity_per_focus = int(round(total_events_with_foci / len(all_foci))) if len(all_foci) > 0 else None

        # maxes
        max_contribution_counter = Counter({
            k: len(efforts[k]["events"])
            for k in efforts if len(efforts[k]["foci"]) > 0
        }).most_common()
        max_contribution = max_contribution_counter[0] if len(max_contribution_counter) > 0 else None

        # map foci and effort to events
        for d in events_flat:
            pt = [p for p in projects if p["id"] == d["project_id"]]
            d["activity"] = d["author"]["name"]
            d["effort"] = pt[0]["effort"] if len(pt) > 0 else None
            d["foci"] = pt[0]["foci"] if len(pt) > 0 and len(pt[0]["foci"]) > 0 else None

        # calculate percentile rank of activity count
        user_occurance_counts = Counter([d["author_id"] for d in events_flat])
        values_below_user_count = len([
            k for k in user_occurance_counts
            if user_occurance_counts[k] < user_occurance_counts[user_id]
        ])
        percentile = (values_below_user_count / len(user_occurance_counts)) * 100 if len(user_occurance_counts) > 0 else None

        # generate ordinal number format
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

        # write contribution to file
        with open(os.path.join(directory_path_output, "contribution.json"), "w") as f:
            f.write(json.dumps({
                "data": [d for d in events_flat if d["effort"] and d["foci"]],
                "stats": {
                    "average_activity_per_effort": average_activity_per_effort,
                    "average_activity_per_focus": average_activity_per_focus,
                    "effort_count": len(efforts),
                    "member_count": len(all_member_ids_with_events),
                    "most_contributed_effort": max_contribution[0] if max_contribution else None,
                    "most_contributed_effort_activity": max_contribution[1] if max_contribution else None,
                    "percentile_for_activity_contribution": ordinal(int(round(percentile))) if percentile else None
                },
                "reference": {
                    "foci": all_foci
                }
            })
        )

        exit(0)

if __name__ == "__main__":
    gitricsCli()
