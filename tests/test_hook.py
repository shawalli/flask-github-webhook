from flask_github_webhook import GithubWebhook


class TestHook(object):
    def test_register_default_hook(self, app):
        webhook = GithubWebhook()
        webhook.init_app(app)

        @webhook.hook()
        def push_hook(data):
            pass

        assert push_hook in webhook._webhook._hooks["push"]

    def test_register_custom_hook(self, app):
        webhook = GithubWebhook()
        webhook.init_app(app)

        @webhook.hook("pull_request")
        def pull_request_hook(data):
            pass

        assert pull_request_hook in webhook._webhook._hooks["pull_request"]

    def test_call_default_hook(self, app):
        webhook = GithubWebhook()
        webhook.init_app(app)
        cli = app.test_client()
        endpoint = app.config["GITHUB_WEBHOOK_ENDPOINT"]

        hook_test_data = {"request": {"key": "value"}, "hook_called": False}

        @webhook.hook()
        def push_hook(data):
            hook_test_data["hook_called"] = True

            assert data is not None

            assert len(set(data.keys()).difference(set(hook_test_data["request"].keys()))) == 0
            for key, value in data.items():
                assert hook_test_data["request"][key] == value

        response = cli.post(endpoint, json=hook_test_data["request"])

        assert response.status_code == 204
        assert hook_test_data["hook_called"]

    def test_call_custom_hook(self, app):
        webhook = GithubWebhook()
        webhook.init_app(app)
        cli = app.test_client()
        endpoint = app.config["GITHUB_WEBHOOK_ENDPOINT"]
        event = "pull_request"

        hook_test_data = {"request": {"key": "value"}, "hook_called": False}

        @webhook.hook(event_type=event)
        def pull_request_hook(data):
            hook_test_data["hook_called"] = True

            assert data is not None

            assert len(set(data.keys()).difference(set(hook_test_data["request"].keys()))) == 0
            for key, value in data.items():
                assert hook_test_data["request"][key] == value

        response = cli.post(endpoint, github_event=event, json=hook_test_data["request"])

        assert response.status_code == 204
        assert hook_test_data["hook_called"]
