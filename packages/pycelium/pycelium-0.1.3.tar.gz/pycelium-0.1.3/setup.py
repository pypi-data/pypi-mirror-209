#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'python-dateutil',
    'glom',
    'jmespath',
]

test_requirements = requirements + [
    'pytest>=3',
]

setup(
    author="Asterio Gonzalez",
    author_email='asterio.gonzalez@gmail.com',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Mycelium Edge Swarm Network",
    entry_points={
        'console_scripts': [
            'pycelium=pycelium.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pycelium',
    name='pycelium',
    packages=find_packages(include=['pycelium', 'pycelium.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/asteriogonzalez/pycelium',
    version='0.1.3',
    zip_safe=False,
)
