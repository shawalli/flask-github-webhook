
from github_webhook import Webhook


class GithubWebhook(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        endpoint = app.config.setdefault(
            'GITHUB_WEBHOOK_ENDPOINT', '/postreceive')
        secret = app.config.setdefault('GITHUB_WEBHOOK_SECRET', None)

        self._webhook = Webhook(
            app,
            endpoint=endpoint,
            secret=secret
        )

        app.extensions = getattr(app, 'extensions', {})
        app.extensions['github_webhook'] = self

    def hook(self, event_type='push'):
        return self._webhook.hook(event_type=event_type)
