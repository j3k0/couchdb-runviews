FROM python:2.7
RUN pip install couchdbkit
COPY couchdb_runviews.py /couchdb_runviews.py
ENTRYPOINT python /couchdb_runviews.py
