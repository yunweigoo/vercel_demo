from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Vercel Flask!'
@app.route('/api')
def hello_world():
    return 'Hello, vercel api!'

if __name__ == '__main__':
    app.run()
