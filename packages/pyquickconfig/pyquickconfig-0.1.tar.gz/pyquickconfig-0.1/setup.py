from setuptools import setup, find_packages


setup(
    name='pyquickconfig',
    version='0.1',
    license='MIT',
    author="Austin Ibele",
    author_email='austin.ibele@gmail.com',
    packages=find_packages('quickconfig'),
    package_dir={'': 'quickconfig'},
    url='https://github.com/austinibele/quickconfig',
    keywords='QuickConfig',
)