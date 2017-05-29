import psycopg2

DBNAME = "news"

"""
Querying neatly formatted information from a (postgreSQL) news database.

This file enables you to look at data in different ways.
To achieve any of these queryes, views have been made to simplyfy things.
You can read more about the views used here, in the DB-Views.md file.
"""


def get_top3_articles():
    """Return articles from the database, most viewed first.
    'v_articleViews' is created in news.sql,
    it fetches how many times any article has been accessed."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print "\nFetching top 3 articles, most popular first...\n"
    c.execute("""SELECT * FROM v_articleViews
                ORDER BY "Views" DESC
                LIMIT 3;""")
    for top3_articles in c:
        print str('%s %s %s' % (top3_articles[0],
                                top3_articles[1],
                                "\n"))
    return
    db.close()

def get_top_authors():
    """Returns most popular article authors of all time, most popular first"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print "\nFetching top authors, most popular first...\n"
    c.execute("""SELECT name AS "Authors name",
                total_views AS "Total number of article views"
                FROM authors, v_authorViews
                WHERE authors.id = v_authorViews.author
                ORDER BY v_authorViews.total_views DESC;""")
    for top_authors in c:
        print str('%s %s %s %s' % (top_authors[0],
                                   "with",
                                   top_authors[1],
                                   "Views\n"))
    return
    db.close()


def error_requests():
    """Returns which days more than 1% of requests were errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print "\nFetching which days more than 1% of requests were errors...\n"
    c.execute("""SELECT bad, to_char(day, 'Mon-MM YYYY')
                 FROM v_errorDays""")
    for which_days in c:
        print str("There were " + '%s %s %s %s' % (which_days[0],
                                                   'bad requests',
                                                   which_days[1],
                                                   "\n"))
    return
    db.close()

# For testing if python make its output 'clearly formatted plain text':
#
# print get_top3_articles()
# print get_top_authors()
# print error_requests()
