"""Model tests."""

import unittest
from sudoku.core import model
from tensorflow import keras


class TestModel(unittest.TestCase):
    """Check the model class."""

    def setUp(self):
        """Set up tests."""
        self.model = model.Model()
        self.model.get_model()

    def test_get_model(self):
        """Test get_model."""
        self.assertIsInstance(self.model.model, keras.Model)

    def test_save(self):
        """Test save."""
        import os
        self.model.save(os.getcwd(), folder='', name='TEST')

    def test_load(self):
        """Test load."""
        import os
        self.model.save(os.getcwd(), folder='', name='TEST')
        self.model.load(os.getcwd(), folder='', name='TEST')
