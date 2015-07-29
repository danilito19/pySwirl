from setuptools import setup

def readme():
  '''This is necessary to tell setuptools to include 
  the README.rst file when generating source distributions'''
  with open('README.rst') as f:
    return f.read()


setup(name='pySwirl',
      version='0.1',
      description='Learn Python, in Python',
      url='https://github.com/danilito19/pySwirl',
      author='Dani Litovsky Alcala',
      author_email='danalitovsky@gmail.com',
      license='MIT',
      packages=['pySwirl'],
      #specify which packages we need to install as dependencies
      # install_requires=[
      #     'markdown',
      # ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)

