from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Hello World!</h1>'
    browser_info=request.headers.get('User-Agent')
    return '<h1> The browser info: {} </h1>'.format(browser_info)

@app.route('/information')
def info():
    return '<h1>Cool Guys</h1>'

@app.route('/info/<name>')
def name(name):
    return 'My name is {}'.format(name)



if __name__ == '__main__':
    app.run(port=5555,debug=True)

