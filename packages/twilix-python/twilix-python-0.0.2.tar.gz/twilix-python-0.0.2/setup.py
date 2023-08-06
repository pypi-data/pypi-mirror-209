from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="twilix-python",
    version="0.0.2",
    url="https://github.com/mypackage.git",
    author="Twilix.io",
    author_email="colabdog@gmail.com",
    description="Twilix",
    packages=find_packages(),
    install_requires=requirements,
)
