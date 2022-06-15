import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("insert into attendance values(2216103,'ram charan teja',99)")
conn.execute("insert into attendance  values(2216101,'yashe',99)")
conn.execute("insert into attendance  values(2216102,'akshay rao',98)")
conn.commit()
conn.close()