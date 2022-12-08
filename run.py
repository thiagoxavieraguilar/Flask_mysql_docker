from flask import Flask, render_template,request,redirect,url_for,flash

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        return show(email,password)
    return render_template('login.html')

@app.route('/show', methods=['GET','POST'])
def show(email:str,password:str):
    return render_template('show.html',email=email,password=password)

@app.route('/creat_account', methods=['GET','POST'])
def creat_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        confirm_password = request.form['cpwd']
        if password == confirm_password:
            #cria a conta
            flash('Conta criada com sucesso')
            return redirect(url_for(login))
        else:
            flash('Verifique se a senha está correta')
    return render_template('create_account.html')

  
if __name__ == '__main__':
    app.run(debug=True)

