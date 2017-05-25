# FSND - Logs analysis project by Mathias Wøbbe

## Features: display information from a database with three tables:
- 'articles', 'authors' and 'log'.

The code can display:
- The top 3 articles
- The most popular authors by article views
- On which days more than 1% of HTTP requests led to errors.

## Views
Look at DB-Views.md for more information.

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
