from flask import Flask, render_template
import logging

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

    return render_template('button.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
