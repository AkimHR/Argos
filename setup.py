from setuptools import setup,find_packages

setup(name='argonautes',
version='1.0',
packages=find_packages()
install_requires=[django==4.1, atomicwrites==1.4.0, attrs==21.4.0, certifi==2022.5.18.1, charset-normalizer==2.0.12,
colorama==0.4.4, idna==3.3, iniconfig==1.1.1, packaging==21.3, paho-mqtt==1.6.1, pluggy==1.0.0,
py==1.11.0, pyparsing==3.0.9, pytest==7.1.2, requests==2.27.1, tomli==2.0.1, urllib3==1.26.9])