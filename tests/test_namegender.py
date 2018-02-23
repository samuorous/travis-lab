from unittest import TestCase
import namegender


class TestNamegender(TestCase):
    def test_predict(self):
        prediction = namegender.predict('Otto')
        self.assertEqual(prediction['gender'], 'male')

    def test_predict_list(self):
        prediction = namegender.predict_list(['Otto'])
        self.assertEqual(type(prediction), list)
        self.assertEqual(len(prediction), 1)
        self.assertEqual(prediction[0]['gender'], 'male')

