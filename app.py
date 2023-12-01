from flask import Flask, request, render_template_string, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # or set a fixed secret key

@app.route('/', methods=['GET', 'POST'])
def guess():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    message = ''
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < session['number']:
            message = 'Too low!'
        elif guess > session['number']:
            message = 'Too high!'
        else:
            message = 'You guessed it! The number was ' + str(session['number'])
            session.pop('number', None)  # Reset the number for a new game
    return render_template_string('''
        <html>
            <body>
                <p>Guess a number between 1 and 100:</p>
                <form method="post">
                    <input type="text" name="guess"/>
                    <input type="submit" value="Guess"/>
                </form>
                <p>{{ message }}</p>
            </body>
        </html>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)
