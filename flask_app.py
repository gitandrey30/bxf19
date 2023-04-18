
from flask import Flask, render_template, request, redirect, abort
import json
from sqlalchemy import insert, select
from config_db import session
from models import user
from schemas import User
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_data():
    if request.method == "GET":
        return render_template('form_page.html')
    if request.method == "POST":
        input_file = request.files['file']
        if input_file.filename == '':
            abort(404, 'Upload file not found')
        data = input_file.read()
        to_j = json.loads(data)
        for item in to_j:
            if "name" in item:
                pass
                # print('required key "name" found')
            else:
                abort(404, 'required key "name" not found')
            if "date" in item:
                pass
                # print(f'required key "date" found')
            else:
                abort(404, 'required key "date" not found')
            name = item['name']
            date = item['date']
            if len(name) >= 50:
                abort(404, f'in name : {name} - more than 50 letters' )
            if type(date) is not str:
                abort(404, f'type error for date : {date} with name : "{name}", ' \
                       f'please change type to "str"')
            obj_to_add = insert(user).values(name=name, data=date)
            print('insert data is: ',obj_to_add)
            session.execute(obj_to_add)
            session.commit()

    return render_template('form_page.html')


@app.route('/get_data')
def resp_data():
    data = select(user)
    result = session.execute(data)
    rep = result.all()
    data_list = []
    for item in rep:
        d = {'data': item.data}
        dt_obj = d['data']
        ser_dt_obj = json.dumps(dt_obj, default=str)
        dict_all = {'id': item.id, 'name': item.name, 'data': ser_dt_obj}
        data_list.append(dict_all)
        json.dumps(data_list)
    responsis = {
        'total': data_list,
    }
    jsonify(responsis)
    return render_template('render_from_db.html', rep=rep)


@app.errorhandler(404)
def get_error(error):
    error_message = error.description
    return render_template('error_page.html', error_message=error_message), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


