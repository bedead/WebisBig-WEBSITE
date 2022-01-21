
from flask import *
import os


##############################################################################

app = Flask("WebisBig")

################################################

app.config['SECRET_KEY'] = os.urandom(210)

###############################################################################


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
