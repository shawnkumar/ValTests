from validator import Validator
from cassandra.cluster import Cluster
from cell import Cell
from row import Row
from partition import Partition
from state import State

cluster = Cluster()
session = cluster.connect()

schema = "CREATE KEYSPACE space WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':1};"
table = "CREATE TABLE tab (key int PRIMARY KEY, val int);"

session.execute(schema)
session.execute("use space;")
session.execute(table)

rows = []
for x in range(0, 100):
    session.execute("INSERT INTO space.tab(key, val) VALUES(" + str(x) + ',' + str(x) + ");")
    rows += [Row([Cell(x), Cell(x)])]

state = State("output.txt", rows)

val = Validator(session)
val.validate(state, "SELECT * FROM space.tab limit 50;")