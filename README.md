# jira-epic-based-timeline

From a given agile board, it gets all cards in the most recent sprints and then group cards per sprint in order to display a timeline like this


 . | . | Sprint 20.02 | Sprint 20.04 | Sprint 20.06
--- | --- | :---: | :---: | :---:
**Epic A** | | | | 
 |  | `Card A.1` | 1 | 1 |   
 |  | `Card A.2` | 1 |   |
 |  | `Card A.3` |   |   | 1
**Epic B** | | | |         |  |   | 
 |  | `Card B.1` | 1 | 1  | 1
 |  | `Card B.2` |  |   | 1

The 1s indicate that the card associated to that row is was part of the commitment the team made for the iteration represented in its column.

For example, in the table above you can see that `Card A.1`, which is a deliverable of the **Epic A**, started in Sprint 20.02 but was carried over into Sprint 20.04.

You'll be able to:
- display the above table in the standard output in a txt format; or
- export data to a CSV file that you can either import to Google Spreadsheet in order to create a pivot table in the format above.
