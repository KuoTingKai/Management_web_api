from flask import Flask, render_template, request, redirect, jsonify, url_for
from Controller.Inventory_control import IC
from Controller.Clock_in_control import SIC
from Controller.Sign_up_control import SUC
from datetime import datetime
from model import Account
import pytz
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
app.config['JSON_AS_ASCII'] = False
jwt = JWTManager(app)

# @app.route("/", methods=['GET','POST'])
# def index():
    # return render_template('main.html')
    # return render_template('Log_in.html')
    # return render_template('test.html')

@app.route("/register", methods=['GET','POST'])
def register():
    # if request.method == 'POST':
    #     print(request.form)
    #     print('bbb')
    if request.method == 'POST' and 'register' in request.form:

        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if username is None or password is None:
            return jsonify(message='請提供使用者名稱和密碼'), 400
        
        if SUC().get(username) == []:
            return jsonify(message='使用者已存在'), 409
        
        # 建立新使用者
        SUC().add(username=username,userpassword=password)
        home_url = url_for('main')
        return render_template('go_back_main.html', home_url=home_url)
        # return jsonify(message='註冊成功', home_url='/'), 201
    # return render_template('main.html')
    # return render_template('Log_in.html')
    return render_template('register.html')

@app.route('/', methods=['GET','POST'])
def login():

    if request.method == 'POST':
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        # 在這裡進行使用者驗證
        # ...
        if username == 'admin' and password == 'admin123':
            # 使用者驗證成功，生成JWT
            access_token = create_access_token(identity=username)
            print(access_token)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message='登入失敗'), 401
        
    return render_template('Log_in.html')

@app.route("/Inventory", methods=['GET','POST'])
def Inventory():
    select_option = IC().find()
    select_option = [item[0] for item in select_option]
    selected_option = None
 
    if request.method == 'POST' and 'search' in request.form:
        option_value = request.form["option_value"]
        rows = IC().get(option_value)
        selected_option = option_value
        print(selected_option)
        return render_template('Inventory.html', my_list=select_option, name=rows,selected_option=selected_option)

    if request.method == 'POST' and 'update' in request.form:
        option_value = request.form["option_value"]
        update_data = request.form["update_data"]
        rows = IC().update(option_value,update_data)
        selected_option = option_value
        return render_template('Inventory.html', my_list=select_option, name=rows,selected_option=selected_option)
    
    return render_template('Inventory.html', my_list=select_option)



@app.route("/clock_in", methods=['GET'])
def Clock_in():
    select_option = IC().find()
    select_option = [item[0] for item in select_option]
    tz = pytz.timezone('Asia/Taipei')
    current_datetime = datetime.now(tz).strftime("%Y-%m-%dT%H:%M")
    

    if request.method == 'POST' and 'search' in request.form:
        option_value = request.form["option_value"]
        rows = SIC().get(option_value)
        selected_option = option_value
        return render_template('Inventory.html', my_list=select_option, name=rows)
    

    return render_template('clock_in.html',current_date=current_datetime)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port=5000)