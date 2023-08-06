from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="getgeo-python",
    version="1.0.0",
    description="A python wrapper for the API provided by getgeoapi.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Loisa Kitakaya",
    author_email="kitakayaloisa@gmail.com",
    maintainer="Loisa Kitakaya",
    maintainer_email="kitakayaloisa@gmail.com",
    url="https://github.com/LoisaKitakaya/getgeo-python",
    project_urls={
        "Bug Tracker": "https://github.com/LoisaKitakaya/getgeo-python/issues",
        "Documentation": "https://github.com/LoisaKitakaya/getgeo-python#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.30.0",
    ],
    python_requires=">=3.6",
)
