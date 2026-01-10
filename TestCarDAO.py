import unittest
from CarDAO import CarDAO
from Car import Car


class TestCarDAO(unittest.TestCase):

    def test_insert_update_delete_find(self):
        car = Car("license", "model", 100, False)
        CarDAO.insert(car)
        try:
            self.assertTrue(car.id_car is not None and car.id_car >= 0)
            cars = CarDAO.get_all()
            self.assertTrue(car in cars)
            car.model = "model 2"
            CarDAO.update(car)
            self.assertTrue(car in CarDAO.get_all())
            self.assertTrue(car == CarDAO.get_by_id(car.id_car))
        finally:
            CarDAO.delete(car)
        self.assertTrue(car not in cars)
        car.model = "model 3"
        self.assertFalse(car in CarDAO.get_all())





if __name__ == '__main__':
    unittest.main()