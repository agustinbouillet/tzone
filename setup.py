import setuptools

# install_requires = open("requirements.txt").read().splitlines()

setuptools.setup(
    name="tzone",
    version="0.0.1",
    author="Agustin Boullet",
    author_email="agustin.bouillet@gmail.com",
    description="Zone horaria de una ubicacion",
    long_description="Modulo para obener la zone horaria de una ubicacion",
    long_description_content_type="text/markdown",
    url="https://github.com/agustinbouillet/tzone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    # install_requires=install_requires,
)
