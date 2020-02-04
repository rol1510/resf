import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="resf-rol1510", # Replace with your own username
    version="0.0.1",
    author="Roland Strasser",
    author_email="roland1510s@gmail.com",
    description="A simple package for displaying calculation results in a textbased table",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="-",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console"
    ],
    python_requires='>=3.6',
)