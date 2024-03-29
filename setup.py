import os

import setuptools

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "/README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="mkdocs-homepage-copier",
    version="1.0.0",
    description="Reuse the README.md file by copying it into the docs/ directory as the docs/index.md file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Clifford Onyonka",
    author_email="jsjamessakho@gmail.com",
    maintainer="Clifford Onyonka",
    maintainer_email="jsjamessakho@gmail.com",
    url="https://github.com/onyonkaclifford/MkDocs-homepage-copier",
    packages=setuptools.find_packages(exclude=["tests"]),
    license="MIT",
    include_package_data=True,
    install_requires=[
        "mkdocs",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
    entry_points={
        "mkdocs.plugins": [
            "mkdocs-homepage-copier = copier:HomepageCopier",
        ]
    },
)
