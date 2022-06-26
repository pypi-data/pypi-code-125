from importlib.metadata import entry_points
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ServerPy",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Divyansh Chopra",                     # Full name of the author
    description="Resource Discovery and Request forwarding library",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    install_requires=[
        'PyYAML==6.0', 
        'web.py==0.62',
        'requests==2.28.0'
    ],                     # Install other dependencies if any
    entry_points = {
        "console_scripts": ['serverpy = servpy.main:main']
    }
)