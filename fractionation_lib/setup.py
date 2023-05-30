from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='fractionation_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    description='A library for fractionation data processing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='LynnSchmied',
    author_email='16linakoval@example.com',
    python_requires='>=3.8',
)

# versionnumber=(majornumber).(minornumber).(patchnumber)
