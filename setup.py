from setuptools import setup
from qssimport import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qssimport',
    version=version.__version__,
    author='Inigo Montoya',
    python_requires='>=3.4',
    description="Merge qss files by using @import",
    long_description=long_description,
    long_description_content_type="text/markdown",
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



