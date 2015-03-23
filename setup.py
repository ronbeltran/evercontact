from setuptools import setup

setup(name='EverContact API Python Client',
    version='0.1',
    description='Python Client for EverContact API',
    url='http://github.com/collabspot/evercontact',
    author='Collabspot',
    author_email='rbbeltran.09@gmail.com',
    license='MIT',
    packages=['evercontact'],
    install_requires=[
        'requests==2.6.0',
        'vobject==0.6.6',
    ],
    zip_safe=False)
