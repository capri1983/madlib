"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():

    color_list = ['red','green','blue','yellow','purple']

    response = request.args.get("response")

    checkbox = request.args.get("madlib")


    print(checkbox)

    if response == "no":
        return render_template("goodbye.html")

    elif checkbox == "Hackbright":
        return render_template("game.html",colors=color_list)
    else:
        return render_template("zoo_input.html")

@app.route('/madlib')
def show_madlib():

    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    person = request.args.get("person")

    return render_template("madlib.html",color=color,noun=noun,
        adjective=adjective, person=person)

@app.route('/madlib_lab')
def show_zoo():

    nouns = []
    verbs = []
    adjectives = []
    adverbs = []

    for key in request.args.keys():
        if key[0] == "n":
            nouns.append(request.args.get(key))
        elif key[0] == "v":
            verbs.append(request.args.get(key))
        elif key[2] == "j":
            adjectives.append(request.args.get(key))
        else:
            adverbs.append(request.args.get(key))

    return render_template("zoo_madlib.html", adjectives=adjectives,
        verbs=verbs, nouns=nouns, adverbs=adverbs)
if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)



'''
{{ noun }} jumping up and down in its tree. He
{{verb: past tense}} {{ adverb }} through
the large tunnel that led to its {{adjective}}
{{noun}}. I got some peanuts and passed them
through the cage to a gigantic gray {{noun}}
towering above my head. Feeding that animal made me
hungry. I went to get a {{adjective}} scoop of ice
cream. It filled my stomach. Afterwards I had to
{{verb}} {{adverb}} to catch our bus. When
I got home I {{verb past tense}} my mom for a
{{adjective}} day at the zoo. 
'''
