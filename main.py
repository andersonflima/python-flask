from flask import Flask, Blueprint

app = Flask(__name__)
urls = Blueprint('urls', __name__)

@urls.route('/')
def hello_world():
    return 'Hello World!'
    
app.register_blueprint(urls)

if __name__=='__main__':
    app.run('localhost',port=3000)