from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pygreet',
    version='1.0.1',
    description='A simple greeting python package.',
    url='https://github.com/LordDashMe/pygreet',
    author='Joshua Clifford Reyes',
    author_email='reyesjoshuaclifford@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'blessings'
    ],
    extras_require={
        'dev': [
            'pytest'
        ]
    }
)
