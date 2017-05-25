```python
import psycopg2

DBNAME = "news"

"""
Querying neatly formatted information from a (postgreSQL) news database.

This file enables you to look at data in different ways, from the top 3 articles to the top authors.
The third function shows on which days more than 1% of requests were errors.
To achieve any of these queryes, views have been made to simplyfy things and language-injection minimal.
You can read more about the views used here, in the README.
"""

def get_top3_articles():
    """Return articles from the database, most viewed first.
    'v_articleViews' is created in news.sql, it fetches how many times any article has been accessed."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT * FROM v_articleViews
                ORDER BY "Views" DESC
                LIMIT 3;""")
    top3_articles = c.fetchall()
    db.close()
    return top3_articles

def get_top_authors():
    """Return the most popular article authors of all time, most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT name AS "Authors name", total_views AS "Total number of article views"
                FROM authors, v_authorViews
                WHERE authors.id = v_authorViews.author
                ORDER BY v_authorViews.total_views DESC;""")
    top_authors = c.fetchall()
    db.close()
    return top_authors

def error_requests():
    """Return which days the database recorded more than 1% of requests as errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT "No. of bad requests", "which day"::date FROM v_errorDays;""")
    which_days = c.fetchall()
    db.close()
    return which_days
```


# For testing if python code presents its output in clearly formatted plain text

#print get_top3_articles()
#print get_top_authors()
#print error_requests()
