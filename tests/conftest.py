import json
import uuid

import pytest
from flask import Flask
from flask.testing import FlaskClient


class TestClient(FlaskClient):
    def open(self, *args, **kwargs):
        # Convert and prepare json in request header and body
        if "json" in kwargs:
            kwargs["data"] = json.dumps(kwargs.pop("json"))
            kwargs["content_type"] = "application/json"

        # Add required GitHub header: X-Github-Event
        headers = kwargs.pop("headers", dict())
        headers["X-Github-Event"] = kwargs.pop("github_event", "push")

        # Add required GitHub header: X-Github-Delivery
        headers["X-Github-Delivery"] = uuid.uuid4().hex

        # Add headers into request
        kwargs["headers"] = headers

        return super(TestClient, self).open(*args, **kwargs)


@pytest.fixture
def app(request):
    app = Flask(request.module.__name__)
    app.test_client_class = TestClient
    app.testing = True
    return app
