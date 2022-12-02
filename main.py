from flask import Flask, render_template, request, session, escape, redirect, url_for
import execute



app = Flask(__name__)



#main Page
@app.route('/')
def main():
    return render_template('main.html')



#pagina de inicio (solo si se inicio sesion)
@app.route('/home')
def homePage():
    if "userName" in session:
        return render_template('home.html')
    
    return redirect(url_for('login'))



#ruta del metodo register (Registrar un nuevo usuario)
@app.route('/register', methods=['POST', "GET"])
def register():
    if request.method == "POST":
        Name = request.form['userName']
        Pass = request.form['passWord']
        resp = execute.existingUser(Name)
        if resp == 1:
            return "This User Name is already taken"
        else:
            execute.add(Name, Pass)
            return "new user added sucessfully"
        
    return render_template('register.html')



#Login y Log out
#ruta del metodo login (iniciar sesion)
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        Name = request.form['userName']
        Pass = request.form['passWord']
        resp = execute.verifi(Name, Pass)
        if resp == 1:
            session["userName"] = Name
            return redirect(url_for('homePage'))
        else:
            return "incorrect"
    return render_template('login.html')


#ruta del metodo logout (cerrar sesion)
@app.route('/logout')
def logout():
    session.pop("userName", None)

    return redirect(url_for('main'))


#clave ultra secretisima
app.secret_key = "anashe"




if __name__ == '__main__':
    app.run(debug=True)