from setuptools import setup

setup(
    name="xml_json_serializer2",
    version="0.1.1",
    description="Library for python (de)serialization in Json and Xml",
    url="https://github.com/Nzhdeh07/Igi_labs/tree/lab_3",
    author="Nzhdeh",
    author_email="nzhdeh.baboyan@icloud.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["serializers"],
    include_package_data=True,
    install_requires=["regex"]
)