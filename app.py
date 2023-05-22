from flask import Flask, render_template, request, redirect, session, abort
from Controller.Inventory_control import IC



app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('main.html')

@app.route("/Inventory", methods=['GET','POST'])
def Inventory():
    select_option = IC().find()
    select_option = [item[0] for item in select_option]
 
    if request.method == 'POST' and 'search' in request.form:
        option_value = request.form["option_value"]
        rows = IC().get(option_value)
        return render_template('Inventory.html', my_list=select_option, name=rows)

    if request.method == 'POST' and 'update' in request.form:
        option_value = request.form["option_value"]
        update_data = request.form["update_data"]
        rows = IC().update(option_value,update_data)
        return render_template('Inventory.html', my_list=select_option, name=rows)
    
    return render_template('Inventory.html', my_list=select_option)



@app.route("/sign_in", methods=['GET'])
def sign_in():
    return render_template('sign_in.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port=5000)