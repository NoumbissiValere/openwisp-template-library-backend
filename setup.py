import os
import sys

from setuptools import find_packages, setup
from template_library import get_version

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


if sys.argv[-1] == 'publish':
    # delete any *.pyc, *.pyo and __pycache__
    os.system('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload -s dist/*")
    os.system("rm -rf dist build")
    args = {'version': get_version()}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name='template-library',
    version=get_version(),
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    license='GPL3',
    description='Backend for the template library website',
    long_description=README,
    url='https://github.com/openwisp/openwisp-template-library-backend',
    author='Noumbissi Valere Gille Geovan',
    author_email='noumbissivalere@gmail.com',
    install_requires=[
        'django-allauth==0.39.1',
        'djangorestframework==3.10.2',
        'django-rest-auth==0.9.5',
        'django-cors-headers==3.1.0',
        'openwisp-users==0.1.10',
        'openwisp-utils==0.2.2',
        'openwisp-controller==0.3.2',
        'django-rest-auth==0.9.5',
        'autobahn==19.6.1',
        'celery>=4.3.0',
        'redis>=3.3.5'
    ],
    extras_require={
        'test': [
            'flake8<=3.6.0',
            'isort<=4.3.4',
            'coverage',
            'coveralls'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Networking',
        'Intended Audience :: Administrators',
        'License :: OSI Approved :: GPL-3 License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python :: 3.6',
    ],
)
