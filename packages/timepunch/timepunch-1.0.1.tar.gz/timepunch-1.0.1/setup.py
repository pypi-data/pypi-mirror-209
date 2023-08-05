from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='timepunch',
    version='1.0.1',
    description="A python library that tracks working hours",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="itsknk",
    py_modules=['hours'],
    entry_points={
        'console_scripts': [
            'timepunch = hours:main',
        ],
    },
)

