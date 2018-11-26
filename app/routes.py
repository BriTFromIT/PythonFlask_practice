from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! I'm using Flask to function! Yay!"