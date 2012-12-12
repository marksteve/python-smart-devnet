from setuptools import setup


setup(
    name='smart-devnet',
    version='0.0.0',
    url='https://github.com/marksteve/python-smart-devnet',
    license='MIT',
    author='Mark Steve Samson',
    author_email='hello@marksteve.com',
    description='Python wrapper for REST API of SMART Developer Network',
    # long_description=__doc__,
    py_modules=['smart_devnet'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests<=0.14',
        'rfc3339==5',
    ],
)
