from setuptools import setup, find_packages

setup(
    name='git-chkfrq',
    version='1.0.0',
    author='Jacky Xie',
    author_email='gokurohono@gmail.com',
    description='file change frequency analysis of a git repo',
    packages=find_packages(),
    install_requires=[
        'GitPython',
        'python-dateutil',
        'pathlib',
    ],
    entry_points={
        'console_scripts': [
            'git-chkfrq = git_chkfrq.cli:main',
        ],
    },
)