from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return ('<h1 style="text-align: center">Hello World!</h1>'
            '<p>papapapapapa</p>'
            '<img width=300 src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExamZuZXFnbzV2a3N6a3VwdTY2dmF3cTgyM2Z1am42dmE4MnUwaDZuYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uUP7F5A1rQR9uKls9P/giphy.gif">')



def make_bold(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f'<b>{result}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f'<em>{result}</em>'
    return wrapper

def make_underlined(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f'<u>{result}</u>'
    return wrapper


@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def hello_bye():
    return 'bye'

@app.route('/username/<user>/<int:number>')
def hello_username(user, number):
    return f'Hi {user} you are {number} years old'

if __name__ == '__main__':
    app.run(debug=True)

