# coding=utf-8
from atlassian import Jira

jira = Jira(url="http://localhost:2990/", username="admin", password="admin")

jira.issue_create(
    fields={
        "project": {"key": "TEST"},
        "issuetype": {"name": "Task"},
        "summary": "test rest",
        "description": "rest rest",
    }
)
