from .. import UnitTest


class TestAccountHourlyRate(UnitTest):

    def test_get(self):
        company_id = 2

        response = self.moco.AccountHourlyRate.get(
            company_id=company_id
        )

        params = response["params"]

        assert params["company_id"] == company_id

        assert response["method"] == "GET"
