# coding=utf-8
from pprint import pprint

from atlassian import Jira

""" How to get server info with health check"""

jira = Jira(url="http://localhost:2990/", username="admin", password="*******")

pprint(jira.get_server_info(True))
