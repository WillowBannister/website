from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Willow!'

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
