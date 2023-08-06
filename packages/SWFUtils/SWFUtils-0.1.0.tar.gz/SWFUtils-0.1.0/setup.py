from setuptools import setup, find_packages

def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    with open(filename) as f:
        lineiter = (line.strip() for line in f)
        return [line for line in lineiter if line and not line.startswith("#")]

requirements = parse_requirements('requirements.txt')

setup(
    name='SWFUtils',
    version='0.1.0',
    url='https://github.com/fredgrub/SWFUtils',
    author='Lucas de Sousa Rosa',
    author_email='roses.lucas404@gmail.com',
    description='SWFUtils is a Python library for handling files in the Standard Workload Format (SWF). It provides utilities for reading, writing, and manipulating SWF files.',
    packages=find_packages(),    
    install_requires=requirements,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)