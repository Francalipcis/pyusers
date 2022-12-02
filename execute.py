from dbConnection import cur, connection


#Funcion que se encarga de agregar el Usuario a la tabla
def add(userName, passWord):
    sql = f"INSERT INTO users(userName, passWord) VALUES('{userName}', '{passWord}')"
    cur.execute(sql)
    connection.commit()



#verifica el nombre de usuario y la contraseña
def verifi(userName, Pass):
    select = f"SELECT * FROM users where userName='{userName}' and passWord='{Pass}'"
    resp = cur.execute(select)
    return resp



def existingUser(userName):
    select = f"SELECT * FROM users where userName='{userName}'"
    resp = cur.execute(select)
    return resp