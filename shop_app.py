from flask import Flask

shop_app = Flask(__name__)

from controllers import controller

if __name__ == "__main__":
    shop_app.run(debug=True)