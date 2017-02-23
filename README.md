# couchdb-runviews

Usage:
```
docker run --rm jeko/couchdb-runviews /couchdb_runviews.py http://couchdb.example.com:5984 my-database-name
```

Will perform a GET on all views of the given database, thus triggering an update if required.

Image is based on the GPL v3 python script by Daniel Richman.
