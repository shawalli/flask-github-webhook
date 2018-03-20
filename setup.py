from setuptools import setup, find_packages


setup(
    name="Flask-Github-Webhook",
    version="0.1.0",
    description="Flask extension for github-webhooks",
    url="https://github.com/shawalli/flask-github-webhook",
    author="Shawn Wallis",
    author_email="shawn.p.wallis@gmail.com",
    #   license='Apache 2.0',
    py_modules=['flask_github_webhook'],
    package_dir={'': 'src'},
    install_requires=[
        'Flask',
        'github-webhook',
    ],

    #   classifiers=[
    #       'Development Status :: 4 - Beta',
    #       'Framework :: Flask',
    #       'Environment :: Web Environment',
    #       'Intended Audience :: Developers',
    #       'Intended Audience :: System Administrators',
    #       'License :: OSI Approved :: Apache Software License',
    #       'Operating System :: MacOS :: MacOS X',
    #       'Operating System :: Microsoft :: Windows',
    #       'Operating System :: POSIX',
    #       'Programming Language :: Python :: 2',
    #       'Programming Language :: Python :: 3',
    #       'Topic :: Software Development :: Version Control'
    #       ],
    #   test_suite='nose.collector'
)
