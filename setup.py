from distutils.core import setup

setup(
    name='SyncIP',
    version='1.0.0',
    author='Jean-Frederic Mainville',
    author_email='jfmainville@outlook.com',
    packages=[''],
    scripts=['syncip/main.py'],
    url='https://github.com/jfmainville/syncip',
    description='This repository contains the code to synchronize the local public IP address with my host entries on GoDaddy.',
    long_description=open('README.md').read()
)
