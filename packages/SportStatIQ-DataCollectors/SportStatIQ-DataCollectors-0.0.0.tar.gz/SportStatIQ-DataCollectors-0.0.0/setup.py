from setuptools import setup, find_packages
import os

# Get long description from README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
f.close()

version_file = os.environ.get('GITHUB_WORKSPACE') + '/version.txt'
with open(version_file, 'r', encoding='utf-8') as f:
    _version = f.read().strip()
f.close()

setup(
    name='SportStatIQ-DataCollectors',
    version=_version,
    author='Matthew Myrick',
    author_email='MatthewMyrick2@gmail.com',
    description='Collects data from various sports websites',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SportStatIQ/SportStatIQ-DataCollectors',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'reader': ['*.txt']},
    install_requires=[
        'pandas',
        'requests',
        'bs4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
