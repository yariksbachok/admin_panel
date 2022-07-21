from flask import Flask, render_template, url_for, request, session
import json
from admin_panel.database import *
import datetime

app = Flask(__name__, static_folder='')
db = DBConnection()

@app.route("/")
def index():
    d = datetime.datetime.now()
    row = db.GetAllUsers()
    price = 137
    count = 0
    count_orders = 0
    orders = db.GetAllOrders()

    for i in row:
        if i == None:
            continue
        count+=i[5]
    for i in orders:
        if i == None:
            continue
        count_orders+=i[3]
    all_price = count*count_orders*price
    data = d.strftime("%B")+' '+str(d.day)
    return render_template("index.html", count=count, all_price=all_price, data=data)

@app.route("/buttons")
def buttons():
    row = db.GetAllButtons()
    return render_template("buttons.html", row=row)

@app.route("/Payments")
def Payments():
    row = db.GetQiwiToken()
    return render_template("payments.html", qiwi=row[0])

@app.route("/text")
def text():
    row = db.GetAllTexts()
    return render_template("text.html", row=row)

@app.route("/change", methods=['GET', 'POST'])
def change():
    try:
        if request.method == "POST":
            requ = json.loads(request.data)
            if requ['type'] == 'button':
                db.UpdateButton(int(requ['id']), requ['text'])
            elif requ['type'] == 'pay':
                db.UpdatePay(int(requ['id']), requ['text'])
            elif requ['type'] == 'text':
                db.UpdateText(int(requ['id']), requ['text'])
            elif requ['type'] == 'admin':
                db.UpdateAdmin(int(requ['id']), int(requ['text']))
    except:
        pass

@app.route("/user-pay")
def user_pay():
    row = db.GetAllUsers()
    return render_template("user-pay.html", row=row)

@app.route("/user-orders")
def user_orders():
    row = db.GetAllOrders()
    return render_template("user-orders.html", row=row)

@app.route("/done-request")
def done_request():
    row = db.GetAllDone()
    return render_template("done-request.html", row=row)

@app.route("/not-ready")
def not_ready():
    row = db.GetNotReady()
    return render_template("not-ready.html", row=row)

@app.route("/admin")
def admin():
    row = db.GEtAdmin()
    return render_template("admin.html", row=row)
