from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    print('hello')
    return 'Hello, World!'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='54.180.245.110', port=5000)