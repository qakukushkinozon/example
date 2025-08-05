import allure
import requests
from services.users.endpoints import Endpoints
from services.users.models.user_model import UserModel
from services.users.payloads import Payloads
from config.headers import Headers
from utils.helper import Helper


class UserAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads
        self.endpoints = Endpoints
        self.headers = Headers

    @allure.step('Создание пользователя')
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )

        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    def get_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_users_by_id(uuid),
            headers=self.headers.basic,
        )

        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model
