from flask import Flask, jsonify, render_template, request, Response
from flask_restful import Api, Resource
import jsonpickle
import numpy as np
import cv2

app = Flask(__name__)
api = Api(app)


# route for documentation
@app.route('/')
def welcome():
    # TODO: Create documentation.html
    # return render_template()
    return "Welcome route"


@app.route('/doc/with_open_cv')
def doc_open_cv():
    # TODO:Create .html with description for gendx with opencv api
    # return render_template()
    return "Doc with open cv"


@app.route('/doc/clear_gendx')
def doc_without_open_cv():
    # TODO: Create .html with description for clear gendx api
    # return render_template()
    return "Doc without open cv"


# route for recognition without opencv for 1 person
@app.route('api/recognize')
def recognize_one_obj():
    # TODO: Connect to Core Module
    # dummy result
    result = {
        "result": "female"
    }
    return jsonify(result)


# route for recognition
@app.route('api/recognize_with_opencv')
def recognize_with_opencv():
    # TODO: Connect to Core Module
    # dummy result
    result = {
        "result": "true"
    }
    return jsonify(result)


# Test receiving images
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    numpy_arr = np.fromstring(r.data, np.uint8)
    # decode image
    image = cv2.imdecode(numpy_arr, cv2.IMREAD_COLOR)

    response = {'msg': 'image received. size={}x{}'.format(image.shape[1], image.shape[0])
                }
    # encode response
    response_encoded = jsonpickle.encode(response)
    return Response(response=response_encoded, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)
