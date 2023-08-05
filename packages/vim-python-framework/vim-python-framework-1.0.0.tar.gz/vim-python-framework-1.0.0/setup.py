from setuptools import setup, find_packages

description='A framework to easily create Vim plugins using Python',
setup(
    name='vim-python-framework',
    version='1.0.0',
    description=description,
    long_description="""
Python VIM Plugin Framework

A framework to facilitate creation of VIM plugins using vanila python
""",
    author='David Kennedy S. Araujo',
    author_email='software@davidkennedy.dev',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'create-vim-python-plugin=vim_python_framework.create_plugin:main',
        ],
    },
)
