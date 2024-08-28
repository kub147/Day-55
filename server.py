from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_word():
    return ('<h1 style="text-align: center">Guess a number between 0 and 9</h1>'
            '<img style="display: block; margin: 0 auto; width: 500px; border-radius: 15px;width=300 " src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

NUMBERTOGUESS = random.randint(0, 9)
print(NUMBERTOGUESS)
@app.route('/<int:number>')
def guess_number(number):
    if number == NUMBERTOGUESS:
        return ('<h1 style="text-align: center; color: green">You found me</h1>'
                '<img style="display: block; margin: 0 auto; width: 500px; border-radius: 15px;" src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    elif number > NUMBERTOGUESS:
        return ('<h1 style="text-align: center; color: red">Too high, try again!</h1>'
                '<img style="display: block; margin: 0 auto; width: 500px; border-radius: 15px;" src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<h1 style="text-align: center; color: purple">Too Low, try again!</h1>'
                '<img style="display: block; margin: 0 auto; width: 500px; border-radius: 15px;" src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')

# Example variable to define the target number

if __name__ == '__main__':
    app.run(debug=True)
