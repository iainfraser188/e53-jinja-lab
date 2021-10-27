from flask import render_template
from shop_app import shop_app
from models.example_orders import orders


@shop_app.route('/orders')
def index():
    return render_template('index.html',book_shop= 'home', orders = orders)