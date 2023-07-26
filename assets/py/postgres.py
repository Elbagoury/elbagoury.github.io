import psycopg2
import sys
from io import StringIO
prod_conn = psycopg2.connect(dbname='DATABASE', user='USER',
                             password='PWD', host='IP',
                               port='5432', sslmode='disable')
loc_conn = psycopg2.connect(dbname='DATABASE', user='USER', password='PWD')
loc_cr = loc_conn.cursor()
prod_cr = prod_conn.cursor()
clean = "DELETE FROM tailored_order; DELETE FROM tailored_order_line; DELETE FROM tailored_order_consumption;"
loc_cr.execute(clean)
input = StringIO()
prod_cr.copy_expert('COPY (select * from tailored_order) TO STDOUT', input)
input.seek(0)
loc_cr.copy_expert('COPY tailored_order FROM STDOUT', input)
loc_cr.commit()
prod_cr.copy_expert('COPY (select * from tailored_order) TO STDOUT', input)
input.seek(0)
loc_cr.copy_expert('COPY tailored_order FROM STDOUT', input)
loc_cr.commit()
loc_cr.close()
prod_cr.close()