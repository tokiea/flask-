# enconding
import random, string, os
from flask import Flask, render_template, request
from de import discern, basepath

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/dog', methods=['POST'])
def dog():
    name_list = []
    file = request.files
    for v in file.values():

        if v.filename:
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
            filename = ran_str + v.filename
            filepath = os.path.join(basepath, filename)
            v.save(filepath)
            name_list.append(filename)

    re_list = discern(name_list, 'dog')
    return render_template('discern.html', context=re_list)


@app.route('/people', methods=['POST'])
def people():
    name_list = []
    file = request.files
    for v in file.values():

        if v.filename:
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
            filename = ran_str + v.filename
            filepath = os.path.join(basepath, filename)
            v.save(filepath)
            name_list.append(filename)

    re_list = discern(name_list, 'people')
    return render_template('discern.html', context=re_list)


if __name__ == '__main__':
    app.run()
