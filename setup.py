from setuptools import setup, find_packages

setup(
    name='freedom-lib',
    version='3.0.0',
    url='https://github.com/tlimao/freedom-lib',
    author='@w!l',
    author_email='tloime@gmail.com',
    description='Freedom lib',
    package_data={"freedom-lib": ["py.typed"]},
    packages=find_packages(),
    python_requires='>=3.6'
)