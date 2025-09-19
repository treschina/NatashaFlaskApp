from flask import Flask, render_template, request
import natasha_functions


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/get_sentences", methods = ["POST"])
def render_sentences():
    lines = natasha_functions.get_sentence_list(request.form.get("text_to_process"))
    return render_template("home.html", lines = lines)

@app.route("/lemmatize", methods = ["POST"])
def lemmatize():
    lemmatized_text = natasha_functions.get_lemmatized_text(request.form.get("text_to_process"))
    return render_template("home.html", lemmatized_text = lemmatized_text)

@app.route("/get_entities", methods = ['POST'])
def render_entities():
    locations, people, organizations, annotated_text = natasha_functions.get_entities(request.form.get("text_to_process"))
    return render_template("home.html", locations = locations, people = people, organizations = organizations, annotated_text = annotated_text)


@app.route("/get_syntax", methods = ['POST'])
def render_syntax():
    syntax = natasha_functions.get_syntax(request.form.get("text_to_process"))
    return render_template("home.html", syntax = syntax)

@app.route("/get_grammar", methods = ['POST'])
def get_grammar():
    grammar = natasha_functions.get_grammar(request.form.get("text_to_process"))
    return render_template("home.html", grammar = grammar)

if __name__ == '__main__':
    app.run(debug=True)