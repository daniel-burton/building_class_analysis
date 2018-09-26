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

for boro in ("mn","bk","bx","qn","si"):
		with open(("./building_class/"+ boro + "_bldg.csv"), 'r') as f:
		next(f)
		cur.copy_from(f, 'bldgclass', sep=',')

conn.commit()
