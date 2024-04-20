from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy database for storing user credentials
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return 'Login successful!'
    else:
        return 'Invalid username or password. Please try again.'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username not in users:
            users[username] = password
            return 'Registration successful!'
        else:
            return 'Username already exists. Please choose a different username.'
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True
