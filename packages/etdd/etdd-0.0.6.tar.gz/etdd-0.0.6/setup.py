from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='etdd',
    version='0.0.6',
    description='extend TDD framework',
    packages=['etdd'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Milan Neubert, Felipe Bombardelli",
    author_email="felipebombardelli@gmail.com",
    
    install_requires=[
        'pathlib'
        , 'jinja2'
        , 'colorama'
        , 'tabulate'
        , 'lizard'
        , 'console-menu' # 0.8.0
        , 'readchar'
    ]
)
