import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []

setuptools.setup(
    name="simpletg",
    version="0.0.1",
    author="GADJIIAVOV",
    author_email="mail@dj.ama1.ru",
    description="Simple telegram bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Djama1GIT/simpletg",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
