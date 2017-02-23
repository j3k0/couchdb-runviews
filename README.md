# couchdb-runviews

### Usage
```

docker run --rm jeko/couchdb-runviews /couchdb_runviews.py http://couchdb.example.com:5984 my-database-name
```

Will perform a GET on all views of the given database, thus triggering an update if required.

## To refresh all views

```
./update-all-views.sh http://couchdb.example.com:5984
```

Requires bash...

### Copyright

License: GNU GPL v3

 * Based on the GPL v3 python script `couchdb_runviews.py` by Daniel Richman.
 * `Dockerfile`, `README.md` and `update-all-views.sh` written by Jean-Christophe Hoelt.
