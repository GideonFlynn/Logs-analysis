# FSND - Logs analysis project by Mathias Wøbbe

## Features:
Display information from a database with three tables:
- 'articles', 'authors' and 'log'.

'''sql
The code can display:
- The top 3 articles
- The most popular authors by article views
- On which days more than 1% of HTTP requests led to errors.

# Several views were used for this project, here are the commands used to create them:

### Join articles.slug with log.path and groups the result by articles.title
```sql
CREATE VIEW v_articleViews AS
                          SELECT title AS "Title", count(*) AS "Views"
                          FROM articles, log
                          WHERE articles.slug = substring(log.path FROM 10)
                          GROUP BY articles.title;
```
### Join articles.slug with log.path and groups the result by articles.author
```sql
CREATE VIEW v_authorViews AS
                          SELECT author, count(*) AS total_views
                          FROM articles, log
                          WHERE articles.slug = substring(log.path FROM 10)
                          GROUP BY articles.author
                          ORDER BY total_views;
```

### Extract day and join log.time where the log.status gave an error. Count the results and group them individually.
```sql
CREATE VIEW v_badRequests AS
                          SELECT date_trunc('day', time) AS "Day" , count(time) AS "bad"
                          FROM log
                          WHERE log.status = '404 NOT FOUND'
                          GROUP BY 1
                          ORDER BY 1;
```
### Pick out the day from log.time. Count the results and group them individually.
```sql
CREATE VIEW v_totalRequests AS
                      SELECT date_trunc('day', time) AS "day" , count(time) AS "total"
                      FROM log
                      GROUP BY 1
                      ORDER BY 1;
```
### Multiply the amout of bad requests with 100 then compare the number with the total amount of requests.
### If the amount of bad requests exceeds the total amount, it return a row.
```sql
CREATE VIEW v_errorDays AS
                        SELECT b.bad AS "bad", t.total AS "whichday", t.day AS "day"
                        FROM v_badRequests b, v_totalRequests t
                        WHERE ("bad" * 100) > ("total") AND b."Day" = t.day
                        ORDER BY day ASC;
```


## Requirements
To run the commands you need:
- Python 2.7
- postgreSQL
- A terminal
- newsdata.sql

## Installing
To run the code in a vagrant environment
- SSH into Vagrant
- CD /vagrant folder
```bash
python newsdata.py
```

## Built with
- Atom.io, a free hackable text editor
- Pyhton 2.7 and the psycopg2 module
- postgreSQL database
- Vagrant


## License

## Acknowledgements
- The forums on udacity are really great, the same goes for 'stack overflow' and the rest of the internet.
- FSND & FEND webcasts where they pull the concepts apart(and put them together in a human way).
- Credits to [Ben](http://ben.goodacre.name/tech/Group_by_day,_week_or_month_%28PostgreSQL%29) for helping to figure out how to group by day, week or month.
