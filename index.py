import sqlite3
from flask import Flask, render_template,request
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)

@app.route('/')
def index():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 8
    offset = (page - 1) * per_page

    conn = sqlite3.connect('app_store.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM app_store")
    total = cur.fetchone()[0]

    cur.execute("SELECT * FROM app_store ORDER BY id LIMIT ? OFFSET ?", (per_page, offset))
    data = cur.fetchall()
    conn.close()

    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('index.html', data=data, pagination=pagination)

@app.route('/detail/<int:app_id>')
def detail(app_id):
    # connect to the database
    conn = sqlite3.connect('app_store.db')
    c = conn.cursor()

    # query the database to get the app details
    c.execute("SELECT * FROM app_store left JOIN app_store_desc ON app_store.app_id=app_store_desc.app_id WHERE app_store.app_id = ?", (app_id,))
    columns = [col[0] for col in c.description]
    product = dict(zip(columns, c.fetchone()))

    # close the database connection
    conn.close()

    # pass the product details to the template
    return render_template('detail.html', product=product)

