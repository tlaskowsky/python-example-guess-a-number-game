from flask import Flask, request, render_template_string
import random

app = Flask(__name__)
number = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def guess():
    message = ''
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < number:
            message = 'Too low!'
        elif guess > number:
            message = 'Too high!'
        else:
            message = 'You guessed it!'
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
