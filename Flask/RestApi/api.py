from flask import Flask, render_template
from flask import request, jsonify
from dummy_data import dummy_data


app = Flask(__name__)  # initiating Flask as app
app.config.update(
    DEBUG=True
)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Homepage</h1>'


# A route to return all of the available entries in our dummy data.
@app.route('/api/v1/data/all', methods=['GET'])
def api_all():
    return jsonify(dummy_data)


# A route to return the person from selected index
@app.route('/api/v1/data/person/<id>', methods=['GET'])
def api_person_by_id(id):
    try:
        id = int(id)
        return jsonify(dummy_data[id])
    except IndexError:
        list_len = len(dummy_data)
        return (
            f"Requested id is not available. Max id is {list_len - 1}"
        )


# Main function to run
if __name__ == '__main__':
    app.run()
