# coding=utf-8
from atlassian import Jira

jira = Jira(url="http://localhost:2990/", username="admin", password="admin")

data = {"permissionScheme": 10001}

result = jira.update_project("RD", data)
print(result)
