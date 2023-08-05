from setuptools import setup

setup(
    name='libheader',
    version='1.0.0',    
    description='A new file format that makes C easier.',
    url='https://github.com/wk1093/libheader',
    author='Wyatt Kloos',
    author_email='wyattk1093@gmail.com',
    license='BSD 2-clause',
    packages=['libheader'],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    scripts=[
        'libheader/gcclh.py',
        'libheader/makelh.py'
    ]
)