import requests

class PostClient:

    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/posts"

    def create_post(self, payload):
        return requests.post(self.base_url, json=payload)

    def get_post(self, post_id):
        return requests.get(f"{self.base_url}/{post_id}")

    def update_post(self, post_id, payload):
        """Sends a PUT request to update an entire resource."""
        return requests.put(f"{self.base_url}/{post_id}", json=payload)

    def delete_post(self, post_id):
        """Sends a DELETE request for a specific ID."""
        return requests.delete(f"{self.base_url}/{post_id}")

    def patch_post(self, post_id, payload):
        """Sends a PATCH request for partial updates."""
        return requests.patch(f"{self.base_url}/{post_id}", json=payload)

    def get_posts(self):
        """Fetches the list of all posts."""
        return requests.get(self.base_url)