import os

import setuptools

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "/README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="mkdocs-homepage-copier",
    version="0.0.3",
    description="Reuse the README.md file by copying it into the docs/ directory as the docs/index.md file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Clifford Onyonka",
    author_email="clifford.onyonka@8teq.co.ke",
    maintainer="Clifford Onyonka",
    maintainer_email="clifford.onyonka@8teq.co.ke",
    url="https://github.com/onyonkaclifford/MkDocs-homepage-copier",
    packages=setuptools.find_packages(),
    license="MIT License",
    include_package_data=True,
    install_requires=[
        "mkdocs",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "mkdocs.plugins": [
            "mkdocs-homepage-copier = copier:HomepageCopier",
        ]
    },
)
