from flask import Flask, render_template,request,redirect,url_for,flash,session
import re
from models import db,Accounts
from config import app
from passlib.hash import sha256_crypt

s = Session()
app.secret_key = 'txavier'


@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        try:
            check = db.session.execute(f"select * from accounts where email = '{email}'" ).fetchone()
            if check:
                print(check['password'])
                pasw = check['password']
                if sha256_crypt.verify(password, passw):
                    s['email'] = check[0]
                    user = s['email']
                    print('logado')
                    return redirect(url_for('show',user=user))
                else:
                    print('Senha incorreta')
            else:
                print('Esse e-mail não existe')
        except:
            print('aconteceu algum erro, tente novamente em instantes')            
    return render_template('login.html')

@app.route('/show/<string:user>', methods=['GET','POST'])
def show(user:str):
    return render_template('back.html',user=user)

@app.route('/creat_account', methods=['GET','POST'])
def creat_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        confirm_password = request.form['cpwd']
        if password == confirm_password:
            password = sha256_crypt.encrypt("password")
            check = db.session.execute(f"select * from accounts where email = '{email}'" ).fetchone()
            print(check)
            #verifica se o e-mail já existe no bd
            if check:
                print('Esse e-mail já está cadastrado')
                return render_template('create_account.html')
            #verifica se o e-mail é valido
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                print('Esse e-mail não é valido')
                return render_template('create_account.html')
            
            else:
                user = Accounts(email,password)  
                db.session.add(user)
                db.session.commit()
                print('verificado conta criada')
                return render_template('login.html')
               
        else:
            print('Verifique a confirmação de senha')
    return render_template('create_account.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
  
if __name__ == '__main__':
    app.run(debug=True)

