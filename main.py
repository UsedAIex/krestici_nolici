import logging

from flask import Flask, render_template

from my_button.button import Button

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wuhiscbaghmrejmsh.ilek,'
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.DEBUG, filename='example.log'
# )

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


@app.route('/')
def start():
    but = Button()
    # if not but.button_1():
    #     but.button_1.label = 'a'
    return render_template('button.html', form=but)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
