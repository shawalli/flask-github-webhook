from flask_github_webhook import GithubWebhook


class TestApp(object):
    def test_direct_initialization(self, app):
        webhook = GithubWebhook(app)

        assert app.extensions["github_webhook"] == webhook

    def test_extension_pattern_initialization(self, app):
        webhook = GithubWebhook()
        webhook.init_app(app)

        assert app.extensions["github_webhook"] == webhook

    def test_default_config(self, app):
        webhook = GithubWebhook()
        webhook.init_app(app)

        assert len([a for a in app.url_map.iter_rules(endpoint="/postreceive")]) == 1
        assert app.extensions["github_webhook"] == webhook
        assert webhook._webhook._secret is None

    def test_custom_config(self, app):
        endpoint = "/test_endpoint"
        secret = "sup3rsecret!"

        app.config["GITHUB_WEBHOOK_ENDPOINT"] = endpoint
        app.config["GITHUB_WEBHOOK_SECRET"] = secret

        webhook = GithubWebhook()
        webhook.init_app(app)

        assert len([a for a in app.url_map.iter_rules(endpoint=endpoint)]) == 1
        assert app.extensions["github_webhook"] == webhook
        assert webhook._webhook._secret == secret.encode("utf-8")
