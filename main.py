from flask import Flask, jsonify, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# route for documentation
@app.route('/')
def welcome():
    # TODO: Create documentation.html
    # return render_template()
    return "Welcome route"


# route for recognition without opencv for 1 person
@app.route('/recognize_one')
def recognize_one_obj():
    # TODO: Connect to Core Module
    # dummy result
    result = {
        "result": "female"
    }
    return jsonify(result)


# route for recognition
@app.route('/recognize_with_opencv')
def recognize_with_opencv():
    # TODO: Connect to Core Module
    # dummy result
    result = {
        "result": "male"
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
