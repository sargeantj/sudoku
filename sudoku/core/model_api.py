"""Rest API page for model."""

from flask import Flask
from flask_restful import Api, Resource, reqparse
from core.model import Model, scale_image, reverse_one_hot
import tensorflow as tf
import numpy as np

# Flask
app = Flask(__name__)
api = Api(app)

# Load the model into memory
model = Model()
model.load()
# Clear tensorflow
graph = tf.get_default_graph()

# Argument parser
parser = reqparse.RequestParser()
parser.add_argument('numeric_image')


class ModelCall(Resource):
    """Rest api methods to call the model."""

    def post(self):
        """
        Post method.

        The input is a numeric representation of the image.
        """
        global graph
        with graph.as_default():
            args = parser.parse_args()

            image = eval(args['numeric_image'])
            scaled_data = scale_image(image)
            array = np.array(scaled_data)

            print(array.shape)

            prediction = model.model.predict(array)
            result = reverse_one_hot(prediction)

            output = {'result': result}
            return output


api.add_resource(ModelCall, '/numeric_image')

if __name__ == '__main__':
    app.run(debug=True)
