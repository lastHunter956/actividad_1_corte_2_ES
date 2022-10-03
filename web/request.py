from urllib import request
from flask import Flask, render_template
from requests import get
app= Flask (__name__)
@app.route("/")
def index():
    return "hola"
@app.route('/store')
def show_store():
    items = get("http://127.0.0.1:3000/store").json()
    return render_template("request.html", items=items)

if __name__=="__main__":
    app.run(debug=True, port=4000)