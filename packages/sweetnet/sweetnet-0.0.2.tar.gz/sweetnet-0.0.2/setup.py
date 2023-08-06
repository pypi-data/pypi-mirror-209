from distutils.core import setup
from setuptools import find_packages

# with open("README.rst", "r", encoding="utf-8") as f:
#     long_description = f.read()
# python setup.py sdist build
# twine upload dist/*
setup(name='sweetnet',  # 包名
      version='0.0.2',  # 版本号
      description='A small example package',
      long_description='神经网络训练部署的贴心套件，让AI变得更加简单',
      author='itmorn',
      author_email='itmorn@163.com',
      url='https://github.com/itmorn/SweetNet',
      install_requires=[],
      license='Apache License',
      # packages=find_packages(),
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )
