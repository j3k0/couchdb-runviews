#!/bin/bash
set -e

# let's run curl in docker (so we're sure it exists)
curl="docker run --net=host --rm -i byrnedo/alpine-curl"

# URL is sent as the first parameter (required)
URL="$1"
if [ -z $URL ]; then
	echo "usage: $0 <URL>"
	echo
	echo "example: $0 http://couchdb.marathon.mesos:5984"
	exit 1
fi

# load the list of databases on the given host and iterate
DATABASES=`$curl -s $URL/_all_dbs|python -mjson.tool|grep '"'|grep -v '_replicator"'|grep -v '"_users"'|cut -d\" -f2`
for DB in $DATABASES; do
	echo
	echo "# Database $DB"
	docker run --rm jeko/couchdb-runviews /couchdb_runviews.py $URL $DB
done

echo
echo "Done"
