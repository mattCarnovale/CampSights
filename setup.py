from setuptools import setup

setup(
    name='campsights',
    version='0.1.0',
    python_requires='>=3.6.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'campsights = campsights_cli.__main__:main'
        ]
    },
    url='https://github.com/mattCarnovale/CampSights',
    author='mattCarnvovale',
    author_email='matt.m.carnovale@gmail.com'
)
