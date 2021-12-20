# coding=utf-8
from atlassian import Jira

""" How to edit comment"""

jira = Jira(url="http://localhost:2990/", username="admin", password="admin")

jira.issue_edit_comment("TST-11098", 10700, "edited test rest api request")
