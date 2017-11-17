"""Setup file for flask-model-mommy."""
import setuptools

from os.path import join, dirname


setuptools.setup(
    name='flask-model-mommy',
    version='0.1.0',
    packages=['flask-model-mommy'],
    include_package_data=True,  # declarations in MANIFEST.in
    install_requires=open(join(dirname(__file__), 'requirements.txt')).readlines(),
    tests_require=open(join(dirname(__file__), 'requirements-dev.txt')).readlines(),
    test_suite='runtests.runtests',
    author='jkaluzka',
    author_email='jkaluzka@gmail.com',
    url='http://github.com/jkaluzka/flask-model-mommy',
    license='MIT',
    description='Simple and easy models object creation package for applic      ations written in Flask.',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    keywords='flask testing factory python model mommy',
    classifiers=[
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
