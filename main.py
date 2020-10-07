from flask import Flask, flash, render_template, request, session, redirect, url_for
from utils import api
import time, json
import math
import dateutil.parser

app = Flask(__name__)
app.secret_key = "THIS IS NOT SECURE"

#---------------------------------------
# FRONT PAGE
# about information; current 10 issues
#---------------------------------------
issues = []

@app.route('/', methods=["GET"])
def root():
    #---------------------------------------
    global issues
    if request.method == "GET":
        page = request.args.get("page")
        if not page:
            page = 1
            issues = api.get_issues("https://api.github.com/repos/walmartlabs/thorax/issues")
        else:
            page = int(page)
        ten_issues = issues[(page-1)*10:page*10]
        num_pages = math.ceil(len(issues)/10)
    return render_template("index.html", ten_issues=ten_issues, page=page, num_pages=num_pages)                       

@app.route('/issue', methods = ['GET'])
def issue_details():
    if request.method == 'GET':
        issue = issues[int(request.args.get("index"))]
        #2020-04-06T19:50:54Z
        date = dateutil.parser.parse(issue["created_at"]).astimezone(dateutil.tz.tzlocal()).strftime("%B %d, %Y, %H:%M:%S %Z")
        return render_template("issue.html", issue=issue, date=date)
