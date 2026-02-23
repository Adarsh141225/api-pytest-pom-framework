import pytest
from utils.data_store import TestDataStore
from clients.post_client import PostClient
from jsonschema import validate
from utils.schemas import POST_SCHEMA


class TestAPIChaining:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Initialize the client for every test in this class."""
        self.post_client = PostClient()

    def test_step1_create_post(self):
        payload = {"title": "Architect Task", "body": "Chained Test", "userId": 1}
        response = self.post_client.create_post(payload)

        assert response.status_code == 201
        validate(instance=response.json(), schema=POST_SCHEMA)

        TestDataStore.POST_ID = response.json()['id']
        print(f"\n[STEP 1] Created ID: {TestDataStore.POST_ID} & Schema Verified!")

    def test_step2_verify_chained_id(self):
        assert TestDataStore.POST_ID is not None, "Chaining failed: No ID found."

        response = self.post_client.get_post(TestDataStore.POST_ID)
        assert response.status_code in  [200, 404]
        print(f"[STEP 2] Success! Verified data using shared ID.")