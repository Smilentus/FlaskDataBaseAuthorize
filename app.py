from flask import Flask, request, redirect, render_template
import eventhandler as eh

app = Flask(__name__)

authError = ''
regError = ''

@app.route('/')
@app.route('/index')
def index():
    global authError
    global regError

    print(authError)
    print(regError)
    return render_template('index.html', error=authError)

@app.route('/main')
def newsPage():
    return render_template('main.html', users=eh.getUsers())

@app.route('/registration')
def regPage():
    return render_template('registration.html', error=regError)

@app.route('/registrate', methods=['POST', 'GET'])
def registratePage():
    if request.method == 'POST':
        global regError

        login = request.form['login'].replace(' ', '')
        password = request.form['password'].replace(' ', '')
        repeatPassword = request.form['repeat-password'].replace(' ', '')
        
        if login == None or password == None or repeatPassword == None or login == '' or password == '' or repeatPassword == '':
            regError = 'Поля заполнены неверно!'
            return redirect('/registration')

        register, msg = eh.registratePerson(login, password, repeatPassword)
        if register:
            return redirect('/main')
        else:
            regError = msg
            return redirect('/registration')
    else:
        return 'Error???'

@app.route('/authorize', methods=['POST', 'GET'])
def authorizePage():
    if request.method == 'POST':
        global authError

        login = request.form['login'].replace(' ', '')
        password = request.form['password'].replace(' ', '')

        if login == None or password == None or login == '' or password == '':
            authError = 'Поля заполнены неверно!'
            return redirect('/')
        
        auth, msg = eh.authorizePerson(login, password)
        if auth:
            return redirect('/main')
        else:
            authError = msg
            return redirect('/')
    else:
        return 'Error???'

if __name__ == '__main__':
    app.run(debug=True)