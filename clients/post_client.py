import requests
from urllib.parse import urljoin
from utils.config_loader import get_config

class PostClient:

    def __init__(self):
        self.base_url = get_config()['base_url']
        self.posts_endpoint = "/posts"
        #print(f"\n--- DEBUG: Target Endpoint is [{urljoin(self.base_url, self.posts_endpoint)}] ---")

    def _get_url(self, path=""):
        """Helper to build URLs correctly: base + /posts + /path"""
        full_base = urljoin(self.base_url + "/", self.posts_endpoint.strip("/"))
        if path:
            return f"{full_base}/{path}"
        return full_base

    def create_post(self, payload):
        return requests.post(self._get_url(), json=payload)

    def get_post(self, post_id):
        return requests.get(self._get_url(post_id))

    def update_post(self, post_id, payload):
        return requests.put(self._get_url(post_id), json=payload)

    def delete_post(self, post_id):
        return requests.delete(self._get_url(post_id))

    def patch_post(self, post_id, payload):
        return requests.patch(self._get_url(post_id), json=payload)

    def get_posts(self):
        return requests.get(self._get_url())