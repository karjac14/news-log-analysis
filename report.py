#!/usr/bin/env python3
#
# A script that generate log REPORTS.

from reportdb import get_report
from reporthelper import beautify


REPORTS = [{'title': 'Three Most Popular Articles', 'query': 'SELECT article, views from articles_views limit 3;'},
           {'title': 'Three Most Popular Article Authors',
               'query': 'SELECT a.name, SUM(av.views) FROM authors a JOIN articles_views av ON a.id = av.author_id GROUP BY a.id;'},
           {'title': 'Days where more than 1 percent error occured', 'query': 'SELECT to_char(date, \'Mon DD, YYYY\'), ROUND(error_percent,2) FROM day_errors WHERE error_percent > 1.0;'}]


def run_report():

    for index, val in enumerate(REPORTS):
        query = val['query']
        results = get_report(query)
        readable_results = beautify(index, results)
        print (val['title'] + ':')
        print (readable_results)


run_report()
