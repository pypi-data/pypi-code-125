from setuptools import setup, find_packages
from fugue_cloudprovider_version import __version__


with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="fugue-cloudprovider",
    version=__version__,
    packages=[x for x in find_packages() if x.startswith("fugue")],
    description="A collection of utils for Fugue to run on cloud providers",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    author="Han Wang",
    author_email="goodwanghan@gmail.com",
    keywords="fugue aws gcp azure databricks",
    url="http://github.com/goodwanghan/fugue-cloudprovider",
    install_requires=[
        "fugue",
    ],
    extras_require={
        "aws": ["boto3", "fs-s3fs"],
        "gcp": ["fs-gcsfs"],
        "databricks": ["databricks-connect", "databricks-cli"],
    },
    entry_points={
        "fugue.plugins": [
            "databricks = fugue_databricks:register",
        ]
    },
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.6",
)
