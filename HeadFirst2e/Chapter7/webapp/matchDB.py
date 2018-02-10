
import mysql.connector

dbconfig = {
    'host' : '127.0.0.1',
    'user' : 'match',
    'password' : 'matchpwd',
    'database' : 'matchlogDB'
    }

conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

_SQL = """ INSERT INTO log (phrase,letters,ip,browser_string,results)
        VALUES(%s,%s,%s,%s,%s)"""

cursor.execute(_SQL,('galaxy', 'xyz', '127.0.0.1', 'Opera', "{'x', 'y'}"))
conn.commit()

_SQL = """ SELECT * FROM log  """
cursor.execute(_SQL)

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
