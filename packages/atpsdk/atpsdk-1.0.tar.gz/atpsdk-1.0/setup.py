from distutils.core import  setup
import setuptools
packages = ['atpsdk']# 唯一的包名，自己取名
setup(name='atpsdk',
	version='1.0',
	author='mjchen',
    packages=packages, 
    package_dir={'requests': 'requests'},)
