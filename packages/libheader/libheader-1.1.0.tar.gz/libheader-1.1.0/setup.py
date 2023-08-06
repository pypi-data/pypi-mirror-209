from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

from libheader._version import __version__

setup(
    name='libheader',
    version=__version__,
    description='A new file format that makes C easier.',
    url='https://github.com/wk1093/libheader',
    author='Wyatt Kloos',
    author_email='wyattk1093@gmail.com',
    license='BSD 2-clause',
    packages=['libheader'],
    install_requires=[],

    classifiers=[
        'License :: OSI Approved :: BSD License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    scripts=[
        'scripts/gcclh.py',
        'scripts/makelh.py',
        'scripts/gcclh',
        'scripts/makelh'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)