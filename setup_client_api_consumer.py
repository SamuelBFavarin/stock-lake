from setuptools import setup, find_packages


setup(
    name = 'apiconsumer', 
    version='0.1', 
    packages=find_packages(include=['client_api_consumer', 'client_api_consumer.*']),
)