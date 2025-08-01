"""Setup script for the modbusim package."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="modbusim",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Modbus RTU/ASCII/TCP device simulator for testing and development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/modbusim",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "modbusim=modbusim.__main__:main",
        ],
    },
    install_requires=[
        "pymodbus>=3.0.0",
        "python-dotenv>=1.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache 2.0  License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
    python_requires=">=3.8",
)
