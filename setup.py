#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from setuptools import setup, find_packages

setup(
    name='jira_epic_based_timeilne',
    version='0.0.1',
    packages=find_packages(),
    platforms=["win", "linux"],
    license='Copyleft',
    author='Marcelo Fernandes',
    author_email='mcf2000@gmail.com',
    description='Visualize the workstreams of your teams in a timeline without having to deal with start and delivery dates.',
    install_requires=open('requirements.txt').readlines(),
)
