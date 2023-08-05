import datetime
import json
import os

from glapi import configuration as glapi_config

# FILE SYSTEM
DIRECTORY_PATH_OUTPUT = os.environ.get("DIRECTORY_PATH_OUTPUT", os.getcwd())
FILEPATH_GITRICS_USER = os.environ.get("FILEPATH_GITRICS_USER", None)

# EVENTS
ACTIVITY_TYPE_CODING = ["pushed", "merged"]
ACTIVITY_TYPE_COLLABORATION = ["approved", "closed", "commented", "created", "updated"]
ACTIVITY_TYPES = ACTIVITY_TYPE_CODING + ACTIVITY_TYPE_COLLABORATION

# instance
GITLAB_TOKEN = glapi_config.GITLAB_TOKEN
GITLAB_API_VERSION = glapi_config.GITLAB_API_VERSION
GITLAB_NAME = os.environ.get("GITLAB_NAME", "GitLab.com")
GITLAB_NAMESPACE = os.environ["GITLAB_NAMESPACE"] if "GITLAB_NAMESPACE" in os.environ else None
GITLAB_URL = os.environ.get("GITLAB_URL", "https://gitlab.com")

VISIBILITY = os.environ.get("VISIBILITY", glapi_config.GITLAB_PROJECT_VISIBILITY)

# projects
PROJECT_FILTER_IDS = [int(d.strip()) for d in os.environ["PROJECT_FILTER_PROJECT_IDS"].split(",")] if "PROJECT_FILTER_PROJECT_IDS" in os.environ else list()
PROJECT_FILTER_GROUP_NAMESPACES = [d.strip().lower() for d in os.environ["PROJECT_FILTER_GROUP_NAMESPACES"].split(",")] if "PROJECT_FILTER_GROUP_NAMESPACES" in os.environ else list()
PROJECT_FILTER_NAMES = [d.strip().lower() for d in os.environ["PROJECT_FILTER_NAMES"].split(",")] if "PROJECT_FILTER_NAMES" in os.environ else list()
PROJECT_FILTER_NAMES_STARTSWITH = [d.strip().lower() for d in os.environ["PROJECT_FILTER_NAMES_STARTSWITH"].split(",")] if "PROJECT_FILTER_NAMES_STARTSWITH" in os.environ else list()

PROJECT_MEMBERSHIP_ONLY = os.environ.get("PROJECT_MEMBERSHIP", glapi_config.GITLAB_PROJECT_USER_MEMBERSHIP)
PROJECT_NAMESPACE_ONLY = os.environ.get("PROJECT_NAMESPACE_ONLY", glapi_config.GITLAB_PROJECT_PERSONAL_ONLY)
PROJECT_SIMPLE = os.environ.get("PROJECT_SIMPLE", glapi_config.GITLAB_PROJECT_SIMPLE)

# users
USER = os.environ.get("GITLAB_USER_ID", None)
USER_ACCESS_INPUT = os.environ.get("GITLAB_USER_PROJECT_ACCESS", "developer")
USER_ACCESS_LEVELS = {
    0: "no access",
    5: "minimal",
    10: "guest",
    20: "reporter",
    30: "developer",
    40: "maintainer",
    50: "owner"
}
#USER_ACCESS = {USER_ACCESS_LEVELS[k]: k for k in USER_ACCESS_LEVELS}[USER_ACCESS_INPUT]

# TIME
DATE_ISO_8601 = glapi_config.DATE_ISO_8601
DATE_END = os.environ.get("DATE_END", datetime.datetime.today().strftime(DATE_ISO_8601))
DATE_START = os.environ.get("DATE_START", (datetime.datetime.today() - datetime.timedelta(days=7)).strftime(DATE_ISO_8601))
