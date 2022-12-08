from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/login', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        return show(email,pwd)
        #return redirect(url_for('show',email=email,password=password))

    return render_template('login.html')

@app.route('/show', methods=['GET','POST'])
def show(email:str,password:str,confirm_password=None):
    return render_template('show.html',email=email,password=password,confirm_password=confirm_password)

@app.route('/creat_account', methods=['GET','POST'])
def creat_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        #confirm_password = request.form['cpwd']
        #if password == confirm_password:
        return show(email,password)
        #else:
        #return('verifique se a senha está correta')
        #return redirect(url_for('show'(email,password,confirm_password)))
    return('olá')
    #return render_template('create_account.html')

@app.route('/')
def hello():
    return 'hello from docker'

#,port=80
    
if __name__ == '__main__':
    app.run(debug=True)

