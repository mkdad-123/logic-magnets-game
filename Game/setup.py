from setuptools import setup, find_packages

setup(
    name='logic-magnets-game',
    version='1.0',
    description='A game simulating Logic Magnets with intelligent search algorithms',
    author='Makdad Taleb',
    packages=find_packages(),
    install_requires=[
        'numpy==1.21.0',
        'heapq==0.2.2',
        'pytest==6.2.4'
    ],
    entry_points={
        'console_scripts': [
            'logic-magnets=game.main:main',
        ],
    },
)
