import couchdb
import json
couch = couchdb.Server('http://jovv:CouchDB1994@localhost:5984/')
db = couch['proyectofinal']
with open("datosfinal.json") as jsonfile:
    for row in jsonfile:
        db_entry = json.loads(row)
        db.save(db_entry)