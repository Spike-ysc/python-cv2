from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page !'

@app.route('/hello')
def hello_world():
    return 'Hello World !'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post %d' % post_id

if __name__ == '__main__':
    app.run(debug=True)