import pymysql

#conexion con la base de datos
connection = pymysql.connect(
    host="db4free.net",
    user="francalipcis",
    password="3Fd6!6@MSFYAP49",
    db="pyusers"
)

#cursor
cur = connection.cursor()