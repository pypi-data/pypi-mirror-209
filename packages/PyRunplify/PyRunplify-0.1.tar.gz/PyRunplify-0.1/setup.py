from setuptools import setup, find_packages
setup(name='PyRunplify',
      version='0.1',
      url='https://github.com/LucasSantosFreire/PyRunplify',
      license='MIT',
      author='Lucas Santos',
      author_email='lunas-3691@hotmail.com',
      description='Simplify running and saving outputs for jupyter codes',
      packages=find_packages(exclude=['tests']),
      setup_requires=['nbconvert==7.2.9', 'nbformat==5.7.3'],
      long_description=open('README.md').read(),
      zip_safe=False)
