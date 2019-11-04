import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "weather",
    version = "1.0.0",
    author = "John Calhoun",
    author_email = "johnmcalhoun123@gmail.com",
    description = ("A Demo of creating a OpenWeather python API."),
    license = "BSD",
    keywords = "OpenWeather",
    url = "https://github.com/JohnCalhoun/weather-api-demo",
    packages=['requests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
