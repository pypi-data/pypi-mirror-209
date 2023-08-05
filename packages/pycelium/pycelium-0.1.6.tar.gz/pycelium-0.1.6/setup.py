#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# requirements = open('requirements.txt').readlines()
requirements = """
arrow==1.2.3
asyncio_mqtt==0.16.1
asyncssh_unofficial==0.9.2
click==8.1.3
codenamize==1.2.3
colorama==0.4.4
debug==0.3.2
glom==23.3.0
Jinja2==3.1.2
jmespath==1.0.1
numpy==1.21.5
paho_mqtt==1.6.1
pytest==7.3.0
python_dateutil==2.8.2
PyYAML==6.0
semver==3.0.0
setuptools==67.6.0
""".splitlines()

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
    version='0.1.6',
    zip_safe=False,
)
