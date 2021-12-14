from flask import Flask, render_template, request
from vsearch import search_for_letters


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'


@app.route('/searchfor', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search_for_letters(phrase, letters))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search_for_letters on the web')


app.run()