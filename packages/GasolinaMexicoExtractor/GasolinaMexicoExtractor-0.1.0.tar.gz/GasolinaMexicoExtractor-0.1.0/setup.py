from setuptools import setup

setup(
    name='GasolinaMexicoExtractor',
    version='0.1.0',
    description='A example Python package',
    url='https://github.com/R3SWebDevelopment/GasolinaMexicoExtractor',
    author='Ricardo Tercero Solis',
    author_email='ricardo.tercero@r3s.com.mx',
    license='BSD 2-clause',
    packages=['GasolinaMexicoExtractor'],
    install_requires=[
        'GasolinaMexicoScrapper',
        'pytz',
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
    ],
)
