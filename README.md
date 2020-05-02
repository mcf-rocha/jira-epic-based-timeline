# jira-epic-based-timeline

From a given agile board, it gets all cards in the most recent sprints and then group cards per sprint in order to display a timeline like this

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3


aaaa

 . | . | Sprint 20.02 | Sprint 20.04 | Sprint 20.06
--- | --- | --- | --- | ---
**Epic A** | | | | 
 |  | `Issue key A.1` | 1 | 1 |   
 |  | `Issue key A.2` | 1 |   |
 |  | `Issue key A.3` |   |   | 1
**Epic B** | | | |         |  |   | 
 |  | `Issue key B.1` | 1 | 1  | 1
 |  | `Issue key B.2` |  |   |

You'll be able to:
- display the above table in the standard output in a txt format; or
- export data to a CSV file that you can either import to Google Spreadsheet in order to create a pivot table in the format above.
