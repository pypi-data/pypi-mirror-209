from setuptools import setup

setup(
    name="Gergyg_lab3_json_xml_serializer",
    version="0.1",
    description="package for python (de)serialization in .json and .xml",
    url="https://github.com/Gergyg/Python-labs/tree/Lab3",
    author="Arseni Matsiusheuski",
    author_email="gad.olg@mail.ru",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["serializers/json", "serializers/source", "serializers/xml", "serializers", "tests"],
    include_package_data=True
)