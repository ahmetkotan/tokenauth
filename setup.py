from distutils.core import setup
import os

BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
print(BASE_DIR)
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
print(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(BASE_DIR, 'README.rst')) as readme:
    README = readme.read()



setup(
    name='tokenauth',
    version='0.9.1',
    packages=['tokenauth', 'tokenauth.migrations'],
    url='https://github.com/ahmetkotan/tokenauth',
    license='GPL',
    author='Ahmet Kotan',
    author_email='ahmtkotan@gmail.com',
    description='Django Simple Token Auth with Expiration Time and Prefix',
    long_description=README,
    install_requires=['djangorestframework'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)