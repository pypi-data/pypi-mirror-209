import requests
from functools import wraps

class SallyJrAPI:
    def __init__(self, api_base_url, api_key):
        self.base_url = api_base_url
        self.api_key = api_key

    def api_call_decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            headers = {"x-api-key": self.api_key}
            kwargs.setdefault('headers', headers)
            response = func(self, *args, **kwargs)
            response.raise_for_status()
            return response.json()
        return wrapper

    @api_call_decorator
    def post(self, endpoint, **kwargs):
        return requests.post(f"{self.base_url}/{endpoint}", **kwargs)

    @api_call_decorator
    def get(self, endpoint, **kwargs):
        return requests.get(f"{self.base_url}/{endpoint}", **kwargs)

    def who_are_you(self):
        return self.get('/')

    def create_list(self, list_size, what_to_get):
        return self.post(
            "/createList",
            json={"listSize": list_size, "WhatToGet": what_to_get},
        )

    def do_work_with_item(self, list_id, item_id, work_request):
        return self.post(
            f"/doWorkWithItem/{list_id}/{item_id}",
            json={"work_request": work_request},
        )

    def get_list_ids(self):
        return self.get("/getListIds")

    def get_list(self, list_id):
        return self.get(f"/getList/{list_id}")

    def add_more_to_list(self, list_id, items_to_add):
        return self.post(
            f"/addMoreToList/{list_id}",
            json={"items_to_add": items_to_add},
        )

