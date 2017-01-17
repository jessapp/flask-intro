from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <a href="/hello">Hi! This is the home page.</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          Title:
            <input type="radio" name="title" value="Mr.">Mr.
            <input type="radio" name="title" value="Ms.">Ms.
            <input type="radio" name="title" value="Mrs.">Mrs.
          <br>
          <label>What's your name? <input type="text" name="person"></label>        
          Compliment:
          <select name="compliment">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="neato">Neato</option>
            <option value="wowza">Wowza</option>
            <option value="ducky">Ducky</option>
          </select>
          <input type="submit">
        </form>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          Diss: 
          <select name="diss">
            <option value="stupid">Stupid</option>
            <option value="smelly">Smelly</option>
            <option value="stinky">Stinky</option>
          </select>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    title = request.args.get("title")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s%s I think you're %s!
      </body>
    </html>
    """ % (title, player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    title = request.args.get("title")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi %s%s I think you're %s!
      </body>
    </html>
    """ % (title, player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
