import json, time, sys
#from flask import requests
import requests


def get_issues(url):
    rg = requests.get(url, None)
    issues = rg.json()
    for i in range(len(issues)):
        issues[i]["index"] = i
    return issues


if __name__ == '__main__':
    issues = get_issues()
    print(issues)
  