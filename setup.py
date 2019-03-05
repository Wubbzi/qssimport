from setuptools import setup
from qssimport import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qssimport',
    version=version.__version__,
    author='Chris Souza',
    author_email='chris.souza3425@gmail.com',
    python_requires='>=2.7',
    description="Merge qss files by using @import",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c385/qssimport",
    license='MIT',
    packages=['qssimport'],
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ],
)



