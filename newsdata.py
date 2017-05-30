#!/usr/bin/env python

import psycopg2

"""
Querying neatly formatted information from a (postgreSQL) news database.
This file enables you to look at data in different ways.
To achieve any of these queryes, views have been made to simplyfy things.
You can read more about the views used here, in the DB-Views.md file.
"""

DBNAME = "news"


def connect(database_name="news"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except:
        print "Unable to connect to database"


def get_top3_articles():
    """Return articles from the database, most viewed first.
    'v_articleViews' is created in news.sql,
    it fetches how many times any article has been accessed."""
    db, c = connect()
    print "\nFetching top 3 articles, most popular first...\n"
    c.execute("""SELECT * FROM v_articleViews
                ORDER BY "Views" DESC
                LIMIT 3;""")
    for top3_articles in c:
        print str('{} {} {}'.format(top3_articles[0],
                                    top3_articles[1],
                                    "\n"))
    return
    db.close()


def get_top_authors():
    """Returns most popular article authors of all time, most popular first"""
    db, c = connect()
    print "\nFetching top authors, most popular first...\n"
    c.execute("""SELECT name AS "Authors name",
                total_views AS "Total number of article views"
                FROM authors, v_authorViews
                WHERE authors.id = v_authorViews.author
                ORDER BY v_authorViews.total_views DESC;""")
    for top_authors in c:
        print str('{} {} {} {}'.format(top_authors[0],
                                       "with",
                                       top_authors[1],
                                       "Views\n"))
    return
    db.close()


def error_requests():
    """Returns which days more than 1% of requests were errors"""
    db, c = connect()
    print "\nFetching which days more than 1% of requests were errors...\n"
    c.execute("""SELECT bad, to_char(day, 'Mon-MM YYYY')
                 FROM v_errorDays""")
    for which_days in c:
        print str("There were " + '{} {} {} {}'.format(which_days[0],
                                                       'bad requests',
                                                       which_days[1],
                                                       "\n"))
    return
    db.close()

if __name__ == '__main__':
    get_top3_articles()
    get_top_authors()
    error_requests()
