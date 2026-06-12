import MySQLdb
import traceback
pwd = "Usman$5000"
print(repr(pwd))
try:
    conn = MySQLdb.connect(host="localhost", user="root", passwd=pwd, db="agrosystem", port=3306)
    print("connected")
    conn.close()
except Exception:
    traceback.print_exc()
