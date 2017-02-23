#!/usr/bin/env python
# Copyright Daniel Richman 2012. License: GNU GPL 3

import sys
import couchdbkit

def main(uri, db):
    server = couchdbkit.Server(uri)
    database = server[db]

    for row in database.all_docs(startkey="_design/", endkey="_design0",
                                 include_docs=True):
        did = row["id"]
        assert did.startswith("_design/")
        design = did[len("_design/"):]

        doc = row["doc"]
        if "views" not in doc:
            continue
        for key in doc["views"]:
            view = design + "/" + key
            print "Refreshing view", view

            if "reduce" in doc["views"][key]:
                r = database.view(view, reduce=True, group=True, limit=1)
            else:
                r = database.view(view, limit=1)

            # It's an iterator, and it's lazily loaded:
            list(r)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: {0} uri database\n".format(sys.argv[0]))
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])