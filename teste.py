
@app.route('/show', methods=['GET','POST'])
def show(email:str,password:str):
    return render_template('show.html',email=email,password=password)