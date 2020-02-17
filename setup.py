import setuptools


with open("README.md", "r",encoding= "utf-8-sig") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tablegen",
    version="1.0.0",
    author="Yotam Abt",
    author_email="yotamabt@gmail.com",
    description="Quickly convert a list of dictionaries to human readable tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yotamabt/TableGen",
    packages=['TableGen'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data = True

)