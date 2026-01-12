import unittest
from pathlib import Path

from Conversion.Convertor import convert_csv_to_data_objects, correct_brand_id, store_old_id
from DAO.BrandDAO import BrandDAO
from DAO.CarDAO import CarDAO
from DAO.CustomerDAO import CustomerDAO
from Database.Config import find_file
from Objects.Brand import Brand
from Objects.Car import Car
from Objects.Customer import Customer


class TestConvertor(unittest.TestCase):

    def test_convert_csv_to_brand(self):
        brand_csv = find_file("Test/TestData/brand.csv")
        self.assertTrue(Path(brand_csv).resolve().exists())

        brands = convert_csv_to_data_objects(brand_csv, Brand)
        self.assertTrue(len(brands) == 10)
        self.assertTrue(brands[0].id_brand is "1")
        self.assertTrue(brands[0].name == "Škoda")

    def test_convert_csv_to_car(self):
        car_csv = find_file("Test/TestData/car.csv")
        self.assertTrue(Path(car_csv).resolve().exists())

        cars = convert_csv_to_data_objects(car_csv, Car)
        self.assertTrue(len(cars) == 10)

    def test_convert_csv_to_customer(self):
        car_csv = find_file("Test/TestData/customer.csv")
        self.assertTrue(Path(car_csv).resolve().exists())

        customers = convert_csv_to_data_objects(car_csv, Customer)
        self.assertTrue(len(customers) == 10)

    def test_insert_delete_cars_using_csv(self):
        brand_csv = find_file("Test/TestData/brand.csv")
        brands = convert_csv_to_data_objects(brand_csv, Brand)

        store_old_id(brands)

        brand_count = len(BrandDAO.get_all())
        try:
            BrandDAO.insert_all(brands)
            self.cars_test(brands)
        finally:
            BrandDAO.delete_all(brands)

        self.assertTrue(brand_count is len(BrandDAO.get_all()))



    def cars_test(self, brands):
        car_csv = find_file("Test/TestData/car.csv")
        cars = convert_csv_to_data_objects(car_csv, Car)
        car_count = len(CarDAO.get_all())
        try:
            correct_brand_id(cars, brands)
            CarDAO.insert_all(cars)
        finally:
            CarDAO.delete_all(cars)

        self.assertTrue(car_count is len(CarDAO.get_all()))

    def test_insert_delete_customers_using_csv(self):
        customer_csv = find_file("Test/TestData/customer.csv")
        customers = convert_csv_to_data_objects(customer_csv, Customer)

        customer_count = len(BrandDAO.get_all())
        try:
            CustomerDAO.insert_all(customers)
        finally:
            CustomerDAO.delete_all(customers)

        self.assertTrue(customer_count is len(BrandDAO.get_all()))
