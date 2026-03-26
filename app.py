from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

users = {
    'gwapo' : ['admin123','admin'],
    'pangit' : ['user123','user']
}

@app.route('/')
def home():
    return 'KINSA KA OOOIIIEEEEE'

@app.route('/admindashboard')
def admindashboard():
    return render_template('admindashboard.html')

@app.route('/userdashboard')
def userdashboard():
    return render_template('userdashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            if users[username][0] == password and users[username][1] == 'admin':
                return render_template('admindashboard.html', massage=username)
            else:
                return render_template('userdashboard.html', massage=username)           
        else:
             return render_template('login.html', massage='Invalid username or password')        
    return render_template('login.html', massage='')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Here, you'd normally save the new user's details in the database
        print(f"Sign Up attempt: {email}, {password}")
        # Redirect to the login page after successful sign-up
        return redirect(url_for('login'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)


