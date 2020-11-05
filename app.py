from flask import Flask
import os
from twenty_cards.workout import workout as w_deck
from twenty_cards.deck import card_char

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        print(e)

    @app.route('/')
    def home():
        return '<h1>Hi</h1>'

    @app.route('/workout')
    def workout():
        style = '<head>\n<style>\np { font-size: 2em; } .card { font-size: 6em; }\n</style>\n</head>'
        cards = '<br/>\n'.join(
            (f'<p><span class="card">{card_char(c)}</span> {w[0]} * {w[1]}</p>' for c, w in w_deck(1))
        )
        return f'<!doctype html>\n{style}\n<body>\n{cards}\n</body></html>'
    
    return app

app = create_app()