from setuptools import setup

setup(
    name='gramspel',
    version='1.0.0',
    author='OmgRod',
    description='A grammar checking and auto-correction package',
    url='https://github.com/OmgRod/grammar-check',
    install_requires=[
        'language-tool-python',
        'tabulate',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
