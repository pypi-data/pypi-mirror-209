from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()


setup(
    name='stopcli',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    author='Wil',
    include_dirs=['app'],
    author_email="mreyeswilson@gmail.com",
    description="A CLI for stop template sheets.",
    entry_points='''
        [console_scripts]
        stopcli=app.main:run
    ''',
)


