from setuptools import setup

setup(
    name='setup_example',
    version='0.1',
    packages=['setup_example'],
    install_requires=[
        'requests',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'mycommand = setup_example.myfile:myfunction'
        ]
    }
)

