from DAO.CarDAO import CarDAO
from DAO.ContractDAO import ContractDAO
from Database.MnMapper import get_all, insert, delete, get_filtered
from Objects.Contract_car import Contract_car


class Contract_carDAO:

    @staticmethod
    def get_cars(contract):
        contract_cars = Contract_carDAO.get_filtered(contract)
        result = []
        for contract_car in contract_cars:
            result.append(CarDAO.get_by_id(contract_car.id_car))
        return result

    @staticmethod
    def get_contracts(car):
        contract_cars = Contract_carDAO.get_filtered(car)
        result = []
        for contract_car in contract_cars:
            result.append(ContractDAO.get_by_id(contract_car.id_contract))
        return result

    # data_objecxt - contract or car
    @staticmethod
    def get_filtered(data_object):
        return get_filtered(Contract_car, data_object)

    @staticmethod
    def get_all():
        return get_all(Contract_car)

    @staticmethod
    def insert(contract_car):
        insert(contract_car)

    @staticmethod
    def delete(contract_car):
        return delete(contract_car)

