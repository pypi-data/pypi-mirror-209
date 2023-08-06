import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='natalify',
    version='1.6',
    packages=setuptools.find_packages(),
    license='GPL-3.0',
    author='jack',
    author_email='kinginjack@gmail.com',
    description='An automation software made for my friend Natalie',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['selenium', 'colorama', 'datetime', 'cryptography', 'webdriver-manager', 'termcolor', 'tinydb'],
    python_requires='>=3.8',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)

