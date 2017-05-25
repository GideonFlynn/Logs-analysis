# Several views were used for this project, here are the commandsused to create them:

### Joins articles.slug with log.path and groups the result by articles.title
```sql
CREATE VIEW v_articleViews AS
                          SELECT title AS "Title", count(*) AS "Views"
                          FROM articles, log
                          WHERE articles.slug = substring(log.path FROM 10)
                          GROUP BY articles.title;
```
### Joins articles.slug with log.path and groups the result by articles.author
```sql
CREATE VIEW v_authorViews AS
                          SELECT author, count(*) AS total_views
                          FROM articles, log
                          WHERE articles.slug = substring(log.path FROM 10)
                          GROUP BY articles.author
                          ORDER BY total_views;
```
### Pick out the day from log.time where the status gave an error. Count the results and group them individually.
```sql
CREATE VIEW v_badRequests AS
                          SELECT date_trunc('day', time) AS "Day" , count(time) AS "bad"
                          FROM log
                          WHERE log.status = '404 NOT FOUND'
                          GROUP BY 1
                          ORDER BY 1;
```
### Pick out the day from log.time where the status gave a message. Count the results and group them individually.
```sql
CREATE VIEW v_totalRequests AS
                          SELECT date_trunc('day', time) AS "day" , count(time) AS "total"
                          FROM log
                          GROUP BY 1
                          ORDER BY 1;
```
### Multiply the amout of bad requests with 100 then compare the number with the total amount of requests.
### If the amount of bad requests exceeds the total amount, the row returns.
```sql
CREATE VIEW v_errorDays AS
                        SELECT DISTINCT b.bad AS "No. of bad requests", t.day AS "which day"
                        FROM v_badRequests b, v_totalRequests t
                        WHERE ("bad" * 100) > ("total")
                        ORDER BY day DESC;
```
