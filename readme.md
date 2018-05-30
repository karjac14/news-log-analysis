
# Log Analysis +

This project queries database logs and generates user logs as per defined criteria.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Programming Language:

[Python 3](https://www.python.org/) - Tested on ver. 3.5.2

This project require the following database views to be created before running the script:

````
CREATE VIEW top_paths (views, path, slug) AS SELECT count(path), path, substring(path from 10) AS slug FROM log WHERE
method = 'GET' AND  status = '200 OK' GROUP BY path HAVING path LIKE '/article/%' ORDER BY count(path) DESC;
````

````
CREATE VIEW articles_views (article, author_id, views) AS SELECT articles.title, articles.author, top_paths.views FROM articles JOIN top_paths ON articles.slug = top_paths.slug;
````

````
CREATE VIEW day_errors (date, error, no_error, error_percent) AS SELECT sub.day, error, good, (error/((error + good)/1.0)*100) AS rate FROM (SELECT DATE_TRUNC('day', time) AS day, count(status) AS error FROM log WHERE status = '404 NOT FOUND' GROUP BY day) sub JOIN ( SELECT DATE_TRUNC('day', time) AS day, count(status) AS good FROM log WHERE status = '200 OK' GROUP BY day) sub2 ON sub.day = sub2.day;
````

## Running the Script

On terminal, run:  

````
python3 report.py
````

## Contributing

Please fork this forked repo, and make a PR.


## Note

SQL file ignored in this repo
