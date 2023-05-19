from flask import Flask, render_template, request, redirect, session, abort
import os


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('management.html')

@app.route("/Inventory")
def Inventory_html():
    return render_template('Inventory.html')

@app.route("/Inventory", methods=['POST'])
def Inventory():
    name = ""
    if request.form.get('search'):
        print("aa")
        name = 'aaaaa'
    

    return render_template('Inventory.html', name=name)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port=5000)