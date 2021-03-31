# Imports
from flask import Flask


# Initiating app
app = Flask(__name__)
app.config.update(
    DEBUG=True
)


# Routes
@app.route('/')
def home():
    return 'Hello World!'


# Main program run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6500)
