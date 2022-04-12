from api_service.api_service import ApiService


class TestApi(ApiService):

    def test_add_pet(self):
        response = self.add_new_pet(199, "duck")

        assert response.status_code == 200, f"Expected status code of server 200 but was {response.status_code}"

    def test_check_pet_by_id(self):
        response = self.get_pet_by_id(199)

        assert response.status_code == 200, f"Expected status code of server 200 but was {response.status_code}"

    def test_delete_pet(self):
        response = self.delete_pet(199)

        assert response.status_code == 200, f"Expected status code of server 200 but was {response.status_code}"