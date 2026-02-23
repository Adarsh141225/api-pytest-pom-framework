import pytest
from clients.post_client import PostClient


class TestPostApi:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Initialize the client for every test in this class."""
        self.post_client = PostClient()

    @pytest.fixture
    def temp_post(self):
        print("\n[Setup] Creating a temporary post for the test...")
        payload = {"title": "Lifecycle Test", "body": "Cleanup test", "userId": 1}
        response = self.post_client.create_post(payload)
        assert response.status_code == 201
        all_posts = self.post_client.get_posts()
        real_id = all_posts.json()[0]['id']

        yield real_id

        print(f"\n[Teardown] Cleaning up...")
        self.post_client.delete_post(real_id)
        print("[Teardown] Cleanup complete!")



    def test_update_and_cleanup(self, temp_post):
        print(f"Running test on generated ID: {temp_post}")

        update_data = {"title": "Updated by Automation"}
        response = self.post_client.update_post(temp_post,update_data)

        assert response.status_code == 200
        print("Update verified successfully.")

    @pytest.mark.parametrize("post_id, expected_title", [
        (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
        (2, "qui est esse"),
        (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut")
    ])
    def test_get_multiple_posts(self,post_id, expected_title):
        """
        This test runs 3 times with different data.
        'post_id' and 'expected_title' come from the list above.
        """
        response = self.post_client.get_post(post_id)
        data = response.json()

        assert response.status_code == 200
        assert data['title'] == expected_title
        print(f"\n[Data-Driven] Verified ID {post_id} successfully.")

    def test_partial_update_with_patch(self):
        payload = {"title": "Updated via PATCH"}

        response = self.post_client.patch_post(1,payload)

        assert response.status_code == 200
        assert response.json()["title"] == "Updated via PATCH"
        print("\nPATCH successful: Only the title was modified.")
