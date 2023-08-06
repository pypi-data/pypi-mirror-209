from setuptools import setup, find_packages


setup(
    name='package_test_7415',
    version='0.1',
    license='MIT',
    author="Ajay Vishwakarma",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/ajay776/test_package_op',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
