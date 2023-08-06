from setuptools import setup, find_packages

setup(
    name='ebeer',
    version='0.0.10',
    packages=find_packages(),
    package_data={
        'ebeer': ['src/trained_model/trained_model.h5'],
    },
)
