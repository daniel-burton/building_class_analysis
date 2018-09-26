import psycopg2 as pg2

conn = pg2.connect("host=localhost dbname=postgres user=postgres password=test")
cur = conn.cursor()

cur.execute("""
CREATE TABLE bldgclass(
	BBL text PRIMARY KEY,
	borough text,
	block text,
	lot text,
	cd text,
	ct text,
	cb text,
	address text,
	bldgclass text,
	tract2010 text
)""")

#iterate through the boroughs and load each into the table
for boro in ("mn","bk","bx","qn","si"):
		with open(("../processed_data/"+ boro + "_bldg.csv"), 'r') as f:
		next(f) #skip the column label row
		cur.copy_from(f, 'bldgclass', sep=',')

conn.commit()
