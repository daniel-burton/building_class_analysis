import psycopg2 as pg2

conn = pg2.connect("host=localhost dbname=postgres user=postgres password=test")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE nta (
    bct2010 text PRIMARY KEY,
    boro_name text,
    boro_code text,
    tract2010 text,
    puma text,
    nta text)""")

with open('../processed_data/nta/nta_equiv.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'nta', sep=',')
conn.commit()
