from flask import Flask, render_template, url_for


app = Flask(__name__)

from views import *

def main():
    app.run(debug=True, host='0.0.0.0', port=8000)

if __name__ ==  '__main__':
    main()