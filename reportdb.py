#!/usr/bin/env python
# "Database code" for the DB News.

import psycopg2


def get_report(query):

    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()
