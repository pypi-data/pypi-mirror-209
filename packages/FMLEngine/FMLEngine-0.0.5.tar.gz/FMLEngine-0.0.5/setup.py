from setuptools import setup, find_packages
 
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
] 
 
setup(
  name='FMLEngine',
  version='0.0.5',
  description='Pre-Apha Graphics Engine',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Josh',
  author_email='kingcode102@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Graphics Engine', 
  packages=find_packages(),
  install_requires=['PySDL2'],
)
