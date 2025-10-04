from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

db = {
    'username': 'rashid',
    'password': '12345'
}

homehtml = """<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h2>Welcome To GFG</h2>
    <a href="/login">login</a> 
</body>
</html>"""

loginhtml = """<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <a href="/">Go Home</a>
    <h2>Login page</h2>
    <form action="/submit" method="post">
        <input type="text" placeholder="username" name="email"><br>
        <input type="password" placeholder="password" name="password"><br>
        <button type='submit'>Login</button>
    </form>
</body>
</html>"""

@app.get('/')
def home():
    return HTMLResponse(homehtml)

@app.get('/login')
def login():
    return HTMLResponse(loginhtml)

@app.post('/submit')
def submit(email: str = Form(...), password: str = Form(...)):
    if email == db.get('username'):  # Changed from 'email' to 'username'
        if password == db.get('password'):
            return HTMLResponse('<h2>You are in dashboard</h2>')
        else:
            return HTMLResponse('<p>Invalid password</p>')
    else:
        return HTMLResponse('<p>Invalid credentials</p>')