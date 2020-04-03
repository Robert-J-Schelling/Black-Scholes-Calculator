import QuantLib as ql
import matplotlib.pyplot as plt
from flask import Flask, redirect, url_for, render_template, request
from OptionForm import OptionForm
import os
import csv
from flask_datepicker import datepicker
from flask_bootstrap import Bootstrap
from Calculations import Calculations
from flask_table import Table, Col

app = Flask(__name__)
bootstrap = Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
options = Calculations()
premium = 0
delta = 0
com_premium = 0
com_delta = 0
optionlist = []
list = []
@app.route('/', methods=('GET', 'POST'))
def main():
    global com_premium
    global com_delta
    form = OptionForm()
    if request.method == 'POST':
        if form.is_submitted() and request.form != None:
            com_premium = 0
            com_delta = 0
            quantity = float(request.form['quantity'])
            premium,delta = options.set_values(request.form)
            results = [premium,premium*quantity,delta,delta*quantity]
            optionlist.append(results)
            for item in optionlist:
                com_premium = com_premium + float(item[1])
                com_delta = com_delta + float(item[3])
            return redirect(url_for('main'))
        else:
            return render_template('Option_data.html', form=form,options = optionlist,com_premium = com_premium,com_delta = com_delta)
    else:
        if(optionlist == []):
            print(optionlist)
            return render_template('Option_data.html', form=form,com_premium = com_premium,com_delta = com_delta)
        else:
            return render_template('Option_data.html', form=form,options = optionlist,com_premium = com_premium,com_delta = com_delta)

@app.route('/delete', methods=('GET', 'POST'))
def delete():
    global com_premium
    global com_delta
    global optionlist
    com_premium = 0
    com_delta = 0
    data = request.get_json(force=True)
    list = data['list']
    optionlist = []
    for item in list:
        optionlist.append(item[1:5])
    for item in optionlist:
        com_premium = com_premium + float(item[1])
        com_delta = com_delta + float(item[3])

    return redirect(url_for('main'))
