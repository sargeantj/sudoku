"""Rest API page for model."""

from flask import Flask
from flask_restful import Api, Resource
from model import Model, scale_image, reverse_one_hot
import numpy as np

# Flask
app = Flask(__name__)
api = Api(app)

# Load the model into memorey
model = Model()
model.load()


class ModelCall(Resource):
    """Rest api methods to call the model."""

    def put(self, numeric_image):
        """
        Put method.

        The input is a numeric representation of the image.
        """
        scaled_data = scale_image([numeric_image])
        array = np.array(scaled_data)

        prediction = model.model.predict(array)
        result = reverse_one_hot(prediction)

        output = {'result': result}
        return output


api.add_resource(ModelCall, '/<string:numeric_image:>')

if __name__ == '__main__':
    app.run(debug=True)
