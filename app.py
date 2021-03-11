import os
from flask import Flask, render_template

import data

app = Flask(__name__)

@app.route('/')
def index():
    out = data.google_get("paint", data.paint_col)
    print(out)
    return render_template("index.html", paints=out)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
