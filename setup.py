import os
from setuptools import setup

this_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_dir, "README.rst"), "r") as f:
    long_description = f.read()

setup(
    name="hisensetv",
    description="MQTT interface to HiSense televisions.",
    long_description=long_description,
    version="1.0.0",
    author="Alessio Moiso",
    author_email="a.moiso@outlook.com",
    url="https://github.com/MrAsterisco/hisensetv",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["paho-mqtt>=1.5.0", "netifaces>=0.11.0"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["hisensetv=hisensetv.__main__:main"]},
    packages=["hisensetv"],
)
