# coding=utf-8
import logging

from atlassian import Jira

""" How to get server info with health check"""

jira = Jira(url="http://localhost:2990/", username="admin", password="********")

log = logging.getLogger("com.a9.python.scripts.example")
logging.basicConfig(level=logging.ERROR)

projects = jira.get_all_projects()
for project in projects:
    project_key = project.get("key")
    try:
        value = jira.get_project_issue_security_scheme(project_key).get("name") or "None"
    except Exception as e:
        log.error(e)
        value = "None"
    print(project_key + " has issue security scheme " + value)
