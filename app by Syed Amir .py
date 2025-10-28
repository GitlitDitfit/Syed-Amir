from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Forms</title>
    <style>
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #74ebd5, #acb6e5);
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 700px;
            margin: 40px auto;
            background: rgba(255, 255, 255, 0.97);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        .form-section {
            background: #f9f9ff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 25px;
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.05);
        }
        h2 {
            color: #444;
            border-bottom: 2px solid #ddd;
            padding-bottom: 5px;
        }
        label {
            display: block;
            margin-top: 10px;
            font-weight: 600;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 14px;
            background-color: #fff;
        }
        button {
            margin-top: 15px;
            background: linear-gradient(45deg, #4facfe, #00f2fe);
            border: none;
            color: white;
            padding: 10px 15px;
            font-size: 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background: linear-gradient(45deg, #43e97b, #38f9d7);
        }
        .result-box {
            margin-top: 15px;
            padding: 10px;
            background: #e7f9ef;
            border-left: 5px solid #4CAF50;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Welcome to My Web Portal</h1>

        <div class="form-section">
            <h2>🔐 Login Form</h2>
            <form action="/login" method="post">
                <label>Username:</label>
                <input type="text" name="username" placeholder="Enter your username">

                <label>Password:</label>
                <input type="password" name="password" placeholder="Enter your password">

                <button type="submit">Login</button>
            </form>
        </div>

        <div class="form-section">
            <h2>💬 Feedback Form</h2>
            <form action="/submit" method="post">
                <label>Name:</label>
                <input type="text" name="name" placeholder="Your full name">

                <label>Email:</label>
                <input type="email" name="email" placeholder="Your email address">

                <label>Message:</label>
                <textarea name="message" rows="4" placeholder="Write your feedback..."></textarea>

                <button type="submit">Submit Feedback</button>
            </form>
        </div>
    </div>

</body>
</html>
'''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        return f'''
        <h2 style="color:green; text-align:center; margin-top:50px;">
            ✅ Welcome, {username}!
        </h2>
        <div style="text-align:center;"><a href="/">Go Back</a></div>
        '''
    else:
        return '''
        <h2 style="color:red; text-align:center; margin-top:50px;">
            ❌ Error: Both username and password are required!
        </h2>
        <div style="text-align:center;"><a href="/">Go Back</a></div>
        '''

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return f'''
        <div style="text-align:center; margin-top:50px;">
            <h2 style="color:green;">📨 Feedback Received</h2>
            <p><b>Name:</b> {name}</p>
            <p><b>Email:</b> {email}</p>
            <p><b>Message:</b> {message}</p>
            <br>
            <a href="/">Go Back</a>
        </div>
        '''
    else:
        return '''
        <h2 style="text-align:center; margin-top:50px;">
            This is a GET request — please use the form to submit feedback.
        </h2>
        <div style="text-align:center;"><a href="/">Go Back</a></div>
        '''

if __name__ == '__main__':
    app.run(debug=True)