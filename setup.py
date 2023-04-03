from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ollivanders",
    version="0.1",
    author="Adrianlm17",
    author_email="adrianlomu2004@gmail.com",
    description="Proyecto FLASK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Adrianlm17/ollivanders-Flask",
    packages=find_packages(),
    install_requires=[
        "Flask==2.1.0",
        "mysql-connector-python==8.0.26"
        "attrs==22.2.0"
        "click==8.1.3"
        "colorama==0.4.6"
        "exceptiongroup==1.1.1"
        "Flask==2.2.3"
        "iniconfig==2.0.0"
        "itsdangerous==2.1.2"
        "Jinja2==3.1.2"
        "MarkupSafe==2.1.2"
        "mysql-connector==2.2.9"
        "packaging==23.0"
        "pluggy==1.0.0"
        "pytest==7.2.2"
        "tomli==2.0.1"
        "Werkzeug==2.2.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
