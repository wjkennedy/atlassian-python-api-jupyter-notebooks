# coding=utf8
"""
    Assign/Reassign a Jira Issue to a user with the account_id
"""

from atlassian import Jira

jira = Jira(url="http://localhost:2990/", username="roger", password="federer")

if __name__ == "__main__":
    assign_issue = jira.assign_issue(issue="APA-555", account_id="rfederer")
