
# Log Analysis +

This project queries database logs and generates user logs as per defined criteria.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

#### Programming Language:

[Python](https://www.python.org/) - Tested on ver. 3.5.2

#### Virtual Machine

Download and Install:

[Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
[Vagrant](https://www.vagrantup.com/downloads.html)

Download and unzip the configuration package [VM Config](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) prepared by Udacity. Inside the `vagrant` subdirectory, along with other starter project, clone this repository. On terminal, at the same subdirectory, run `vagrant up`, then `vagrant ssh`.

Download and unzip the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) here to the `vagrant` subdirectory. Run `psql -d news -f newsdata.sql`. This will connect and setup the database server.

#### Create Views

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
python report.py
````

## Contributing

Please fork this forked repo, and make a PR.


## Note

SQL file ignored in this repo

## Acknowledgements

Udacity
