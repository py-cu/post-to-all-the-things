from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('messages.html')

@app.route('/new')
def new_message():
    return render_template('new-message.html')

if __name__ == '__main__':
    app.run()