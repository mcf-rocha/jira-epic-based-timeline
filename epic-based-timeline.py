#!/usr/local/bin/python3

from atlassian import Jira
import pandas as pd
import time
import json

with open('config.json') as config_file:
    config = json.load(config_file)

jira = Jira(
    url=config["jira-url"],
    username=config["jira-username"],
    password=config["jira-password"])

boards = config["jira-boards"]
issue_board_id, issue_sprint_name, issue_key, issue_summary, issue_epic_key, issue_epic_name, ones = ([
] for i in range(7))

#bs = jira.get_all_agile_boards()
#for b in bs['values']:
#    print(b['id'], ' - ', b['name'], ' - ', b['type'])

for board_id in boards:
    sprintsValues = []
    start = 0
    while True:
        sprints=jira.get_all_sprint(board_id, state='active,closed', start=start)
        print("Board", board_id, "contains,", len(sprints['values']), "sprints . RETURN: total =", sprints.get(
            "total"), ", maxResults =", sprints.get("maxResults"), " startAt = ", sprints.get("startAt"), " isLast = ", sprints.get("isLast"))
        sprintsValues.extend(sprints['values'])
        start+=50
        if sprints.get("isLast"):
            break
    for i in range(len(sprintsValues), (len(sprintsValues)-config["qtySprints"]), -1):
        sprint = sprintsValues[i-1]
        issues = jira.get_sprint_issues(sprint['id'], start=0, limit=50)
        for issue in issues['issues']:
            issue_board_id.append(board_id)
            issue_sprint_name.append(sprint['name'])
            issue_key.append(issue['key'])
            issue_summary.append(issue['fields']['summary'])
            ones.append(1)
            if issue['fields']['epic'] is None:
                issue_epic_key.append("")
                issue_epic_name.append("")
            else:
                issue_epic_key.append(issue['fields']['epic']['key'])
                issue_epic_name.append(issue['fields']['epic']['name'])

df = pd.DataFrame()
df['Boad'] = issue_board_id
df['EpicKey'] = issue_epic_key
df['EpicName'] = issue_epic_name
df['SprintName'] = issue_sprint_name
df['IssueKey'] = issue_key
df['IssueSummary'] = issue_summary
df['One'] = ones

df.to_pickle("./"+time.strftime("%Y-%m-%d",
                                time.gmtime())+"-epic-timeline.pkl")
df.to_csv("./"+time.strftime("%Y-%m-%d",
                                time.gmtime())+"-epic-timeline.csv")                        

with pd.option_context('display.max_rows', None):
    print(pd.pivot_table(df, values='One', index=[
          'EpicKey', 'EpicName', 'IssueKey'], columns='SprintName', aggfunc='sum', fill_value='-'))
