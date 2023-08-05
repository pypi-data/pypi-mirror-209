from glapi.connection import GitlabConnection

from gitrics import configuration

def convert_topics_to_percent(projects: list) -> list:
    """
    Convert topic list to percent format similar to default GitLab Language objects.

    Args:
        projects (list): dictionaries where each represents a GitLab Project

    Returns:
        A list of dictionaries where each represents a GitLab Project.
    """

    # loop through projects
    for project in projects:

        # capture topic object
        topics_list = project["topics"]

        # put topics in same percent format as languages
        project["topics"] = dict()

        # loop through topics
        for topic in topics_list:

            # convert counts to percent
            project["topics"][topic] = (1 / len(topics_list)) * 100

    return projects

def enrich_effort(projects: list) -> list:
    """
    Enrich projects with effort.

    Args:
        projects (list): dictionaries of GitLab Project

    Returns:
        A list of dictionaries where each represents an enriched GitLab Project.
    """

    result = list()

    for project in projects:

        # determine effort based on namespace
        effort = [d for d in project["path_with_namespace"].split("/")[0:-1] if d in project["name"]]

        p = project

        # add more data to new object
        p["effort"] = effort[0] if len(effort) > 0 else project["name"]

        # add to result
        result.append(p)

    return result

def enrich_foci(projects: list, foci: dict = None) -> list:
    """
    Enrich projects with foci.

    Args:
        foci (dictionary): key/values where each key is a focus and corresponding value is an array of strings representing alternate spellings or other variations
        projects (list): dictionaries of GitLab Project

    Returns:
        A list of dictionaries where each represents an enriched GitLab Project.
    """

    result = list()
    invert_reference = dict()

    # invert foci reference mapping

    if foci:
        for key in foci:
            invert_reference[key] = key
            for value in foci[key]:
                invert_reference[value] = key

    # loop through projects
    for project in projects:

        p = project

        # add more data to new object
        p["foci"] = [invert_reference[d.lower()] for d in project["topics"] if d.lower() in invert_reference] if invert_reference else list()

        # add to result
        result.append(p)

    return result

def enrich_languages(projects: list, connection: GitlabConnection = None, token: str = configuration.GITLAB_TOKEN, version: str = configuration.GITLAB_API_VERSION) -> list:
    """
    Enrich projects with languages.

    Args:
        connection (GitlabConnection): connection class
        projects (list): dictionaries of GitLab Project
        token (string): GitLab access token
        version (string): GitLab API url specific to api version

    Returns:
        A list of dictionaries where each represents an enriched GitLab Project.
    """

    result = list()

    # check for connection
    if not connection: connection = GitlabConnection(version, token)

    for project in projects:

        # pull languages from api
        languages = connection.query("projects/%s/languages" % project["id"])["data"]

        # artifical delay for api constraints
        #time.sleep(2)

        p = project

        # add more data to new object
        p["languages"] = languages

        # add to result
        result.append(p)

    return result

def enrich_topics(projects: list) -> list:
    """
    Enrich projects with topics.

    Args:
        projects (list): dictionaries of GitLab Project

    Returns:
        A list of dictionaries where each represents an enriched GitLab Project.
    """

    result = list()

    for project in projects:

        # get list of languages
        languages = [d.lower() for d in project["languages"]]

        # get topics and filter out languages from topics
        topics = [d.lower() for d in project["tag_list"] if d.lower() not in languages]

        p = project

        # add more data to new object
        p["topics"] = topics

        # add to result
        result.append(p)

    return result

def enrich_membership(projects: list, connection: GitlabConnection = None, token: str = configuration.GITLAB_TOKEN, version: str = configuration.GITLAB_API_VERSION) -> list:
    """
    Enrich projects with members.

    Args:
        connection (GitlabConnection): connection class
        projects (list): dictionaries of GitLab Project
        token (string): GitLab access token
        version (string): GitLab API url specific to api version

    Returns:
        A list of dictionaries where each represents a GitLab project.
    """

    result = list()

    # check for connection
    if not connection: connection = GitlabConnection(version, token)

    # loop through project ids list
    for project in projects:

        p = project

        # add more data to new object
        p["members"] = connection.paginate("projects/%s/members/all" % project["id"])

        # superficial delay for api constraints
        #time.sleep(2)

        # add to result
        result.append(p)

    return result

def extract_effort(projects: list) -> list:
    """
    Set effort name when known effort is found in topics.

    Args:
        projects (list): dictionaries where each represent a GitLab Project

    Returns:
        A dictionary of key/value paris representing efforts.
    """

    # get effort names
    effort_names = [d["effort"].lower() for d in projects]

    # loop through projects
    for project in projects:

        # when the effort name matches the project name it has been determined to be a one-off project
        # if the topic list has an existing effort name this project could belong to an effort but exists in a group which isn't named for the effort
        if project["effort"] == project["name"]:

            # loop through effort names
            for effort_name in effort_names:

                # loop through topics
                for topic in project["topics"]:

                    # topic matches an effort
                    if topic.lower() == effort_name:

                        # update project effort
                        project["effort"] = effort_name

    return projects

def prune_topics(projects: list, foci: dict = None) -> list:
    """
    Remove efforts and foci from topics.

    Args:
        foci (dictionary): key/values where each key is a focus and corresponding value is an array of strings representing alternate spellings or other variations
        projects (list): dictionaries where each represents a GitLab Project

    Returns:
        A list of dictionaries where each represent a GitLab Project.
    """

    # invert foci reference mapping
    invert_reference = dict()
    if foci:
        for key in foci:
            for value in foci[key]:
                invert_reference[value] = key

    # get effort names
    effort_names = [d["effort"].lower() for d in projects]

    # loop through projects
    for project in projects:

        # loop through topics
        for topic in project["topics"]:

            # remove effort name from topics
            project["topics"] = [d for d in project["topics"] if d.lower() not in effort_names]

            # remove foci from topics
            project["topics"] = [d for d in project["topics"] if d.lower() not in list(invert_reference.keys())] if invert_reference else project["topics"]

    return projects
