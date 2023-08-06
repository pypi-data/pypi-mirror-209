from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="printstructure",
    packages=find_packages(include=["printstructure"]),
    version="0.1.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A Python library that can elegantly print out complex data structures",
    url="https://github.com/DavidHo666/print-structure",
    author="Dawei He",
    install_requires=["tabulate"],
    # setup_requires=["pytest-runner"],
    # tests_require=["pytest"],
    # test_suite="tests",
)
