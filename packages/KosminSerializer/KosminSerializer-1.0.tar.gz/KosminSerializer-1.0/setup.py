from setuptools import setup, find_packages


setup(
    name="KosminSerializer",
    version="1.0",
    description="module for python serialization(JSON, XML)",
    url="https://github.com/kosmp/SCol_labs/tree/lab3",
    author="Pavel Kosmin",
    author_email="kosmin.2003@mail.ru",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["Serializers"],
    include_package_data=True
)