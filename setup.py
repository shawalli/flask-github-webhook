from setuptools import setup, find_packages


setup(
    name="Flask-Github-Webhook",
    version="0.1.0",
    description="Flask extension for github-webhooks",
    url="https://github.com/shawalli/flask-github-webhook",
    author="Shawn Wallis",
    author_email="shawn.p.wallis@gmail.com",
    license='Apache 2.0',
    py_modules=['flask_github_webhook'],
    package_dir={'': 'src'},
    install_requires=[
        'github-webhook',
        'six'
    ],
    tests_require=[
        'flask',
        'pytest'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control :: Git'
    ]
)
