from flask import Flask, render_template, request, redirect, session, abort
import os
from model import read_Inventory_name


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    

    # for i in rows:
    #     print(list(i))
    return render_template('management.html')

@app.route("/Inventory")
def Inventory_html():
    rows = read_Inventory_name().find()
    rows = [item[0] for item in rows]
    return render_template('Inventory.html',my_list=rows)

@app.route("/Inventory", methods=['POST'])
def Inventory():
    name = ""
    if request.form.get('search'):
        print("aa")
        name = 'aaaaa'
    


    return render_template('Inventory.html', name=name)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port=5000)