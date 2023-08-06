from setuptools import setup, find_packages

setup(
    name='selenextra',
    version='1.0.9',
    description='Bringing additional features to Selenium',
    author='Tat Nguyen Van',
    author_email='nguyenvantat1182002@gmail.com',
    url='https://github.com/nguyenvantat1182002/SeleneXtra',
    packages=find_packages(),
    install_requires=[
        'selenium-wire'
    ],
    dependency_links=[
        'https://github.com/nguyenvantat1182002/undetected-chromedriver/archive/master.zip#egg=undetected_chromedriver'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
