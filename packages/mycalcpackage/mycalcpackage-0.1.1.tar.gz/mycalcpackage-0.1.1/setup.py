from setuptools import setup

setup(
    name='mycalcpackage',
    version='0.1.1',
    description='A package for calculations',
    author='Your Name',
    author_email='your@email.com',
    packages=['mycalcpackage'],
    install_requires=['toml'],
    package_data={'mycalcpackage': ['config.toml']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': [
            'mycalc = mycalcpackage.calculator:main',
        ],
    },
)
