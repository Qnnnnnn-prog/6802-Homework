import sqlite3
import datetime
conn = sqlite3.connect("log.db")
c = conn.execute("select * from users")
r = ""
for row in c:
    r = r + str(row) + "<br>"
print(r)


