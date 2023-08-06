from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r",encoding='UTF-8') as f:
  long_description = f.read()

setup(name='SFTB',  # 包名
      version='1.1',  # 版本号
      description='SFTB: A New Algorithm for Pairwise Comparison Data-based Ranking Solutions.',
      long_description=long_description,
      author='Y.C.Huang',
      author_email='1950003@tongji.edu.cn',
      install_requires=['numpy','pandas','matplotlib','scipy'],
      license='MIT License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )