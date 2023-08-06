import setuptools

setuptools.setup(
    name='natalify',
    version='1.0',
    packages=setuptools.find_packages(),
    license='GPL-3.0',
    author='jack',
    author_email='kinginjack@gmail.com',
    description='Natalify: An automation software made for my friend Natalie',
    long_description='Natalify is a Python-based automation software created specifically for my friend Natalie. It leverages popular libraries such as Selenium, Colorama, and Cryptography to provide a user-friendly interface for automating various tasks. With Natalify, you can automate web interactions, perform data processing, and more. It offers features like web scraping, form filling, and browser automation. The software is actively maintained and designed to be easily extendable.',
    long_description_content_type='text/markdown',
    install_requires=['selenium', 'colorama', 'datetime', 'cryptography', 'webdriver-manager', 'termcolor', 'tinydb'],
    python_requires='>=3.8'
)

