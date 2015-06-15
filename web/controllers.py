from flask import Flask, render_template, make_response, request, redirect,  url_for
from .session import authenticate_user, create_session, require_login, AuthenticationException

from .forms import NewMessageForm

app = Flask(__name__)

@app.route('/')
@require_login
def home():
    return render_template('messages.html')

@app.route('/new', methods=['GET', 'POST'])
@require_login
def new_message():
    if request.method == 'POST':
        form = NewMessageForm(request.form)
        if not form.validate():
            return render_template('new-message.html', form=form)
        save_message(form)
        return redirect(url_for('home'))
    else:
        form = NewMessageForm()
        return render_template('new-message.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return handle_login()
    else:
        return render_template('login.html')

def handle_login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    try:
        user = authenticate_user(username, password)
        response = make_response(redirect(url_for('home')))
        create_session(user, response)
        return response

    except AuthenticationException as ex:
        return render_template('login.html', message="Login Failed")

def save_message(message_form):
    pass