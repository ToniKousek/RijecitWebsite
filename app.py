from flask import Flask, render_template
from datetime import date
from main import random_word, check_words, list_word

app = Flask(__name__)


@app.route("/wordle")
def wordle_begin():
    return render_template("wordle.jinja",
        answer=random_word("".join(date.today().isoformat().split("-"))), 
        texts=["" for i in range(30)], 
        colors=["" for i in range(30)])


@app.route("/wordle/<letters>")
def wordle_game(letters: str = None):
    # get the answer
    answer = random_word("".join(date.today().isoformat().split("-")))
    
    # split the words
    words = letters.split("&")

    result = check_words(answer, words)

    # because of bug
    colors = []
    texts = []
    error_message = ""

    
    # not in dictionary
    if type(result) is int:
        print("That word isn't in the dictionary")

        # get the previous words coloring
        try:
            result = check_words(answer, words[:-1])
            colors = list_word(result)
            texts = list_word(words[:-1]) 
        except Exception as e:
            print(e)
            pass        

        # add to the end so no overflow error
        texts += [''] * (30 - len(texts))
        colors += [''] * (30 - len(colors))

        #set the error
        error_message = "0"

    # won
    elif type(result[0]) is int:
        texts = list_word(words)
        colors = list_word(result[1])
        print("You won")

    # nothing interesting happened
    else:
        texts = list_word(words)
        colors = list_word(result)
        print(texts,colors)
    
    return render_template("wordle.jinja", texts=texts, colors=colors, answer=answer, error_message=error_message)
    

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
