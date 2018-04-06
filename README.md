# Flask-Github-Webhook

[![Build Status](https://travis-ci.org/shawalli/flask-github-webhook.svg?branch=master)](https://travis-ci.org/shawalli/flask-github-webhook)
[![Coverage Status](https://coveralls.io/repos/github/shawalli/flask-github-webhook/badge.svg?branch=master)](https://coveralls.io/github/shawalli/flask-github-webhook?branch=master)

Flask-Github-Webhook adds extension support for GitHub webhooks to Flask. This extension primarily extends the [python-github-webhook](https://github.com/bloomberg/python-github-webhook) project by making the [Flask Extension Pattern](http://flask.pocoo.org/docs/latest/patterns/appfactories/#factories-extensions) available as an initialization option.

## Initialization
The Github-Webhook Extension may be initialized directly or as an extension:

**Direct Setup**
```
from flask import Flask
from flask_github_webhook import GithubWebhook

app = Flask(__name__)
webhook = GithubWebhook(app)
```

**Extension Setup**
```
from flask import Flask

# The extension may be initialized from anywhere in the project, including
# inside this file, by calling GithubWebhook()
from .extension import WEBHOOK

app = Flask(__name__)
WEBHOOK.init_app(app)
```

## Usage
The extension may be used in the same manner as `python-github-webhook`.
```
from .extension import WEBHOOK

@WEBHOOK.hook()
def push_handler(data):
    print('Received the following PUSH event:{}'.format(data))

@WEBHOOK.hook(event_type='pull_request')
def pullrequest_handler(data):
    print('Received the following PULL-REQUEST event:{}'.format(data))
```

## Configuration
The extension has the same configurations available as the `python-github-webhook` package. However, unlike referenced package, this extension reads those configurations from the Flask application, not initialization arguments. The values below should be configured in the Flask application (app.config) prior to initializing the extension.

### GITHUB_WEBHOOK_ENDPOINT
This setting declares the route that all webhook event handlers will use. If left unset, the setting will default to the endpoint as declared in `python-github-webook`. As of this writing, the default endpoint is `/postreceive`.

### GITHUB_WEBHOOK_SECRET
If provided, this setting's value should match the secret set in the GitHub repository from which this extension will receive webhooks.

## Contributing
Contributions are welcomed! If you would like to improve or modify Flask-Github-Webhook, please follow these steps:
1. Fork this repository.
2. Make your changes and create a pull request.
3. Ensure that all status checks are passing.

## Author & License
This package is released under an open source MIT License. Flask-Github-Webhook was originally written by [Shawn Wallis](https://github.com/shawalli).

## References
* [python-github-webhook](https://github.com/bloomberg/python-github-webhook) 
* [GitHub Webhook Development Guide](https://developer.github.com/webhooks)
* [Flask Extension Pattern](http://flask.pocoo.org/docs/latest/patterns/appfactories/#factories-extensions)
