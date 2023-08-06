from setuptools import setup, find_packages, find_namespace_packages
import os, sys

sys.path.insert(0, os.getcwd() + os.sep + "src")

import pysweepme
print()
print("pysweepme path:", pysweepme)
print("pysweepme version:", pysweepme.__version__)
print

package_path = "src"

# print(find_namespace_packages(where=package_path))


import os
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'src', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
with open(os.path.join(this_directory, 'src', 'LICENSE.txt'), encoding='utf-8') as f:
    license_text = f.read()


setup(

        name='pysweepme',
        version=pysweepme.__version__,
        packages=find_namespace_packages(where=package_path),
        package_dir={"": package_path},

        install_requires=[
                        "pyvisa>=1.8",
                        "pyserial",
                        # "pywin32", # does not work with linux
                        # "python-dispatch",  # has been removed since pysweepme commit 18.09.22
                        ],


        # metadata to display on PyPI
        author='SweepMe! GmbH',
        author_email='pysweepme@sweep-me.net',
        description='load SweepMe! instrument drivers from python scripts',
        keywords='SweepMe! DeviceClasses measurements instruments equipment driver',
        url='https://sweep-me.net',
        project_urls = {
                        "github": "http://github.com/SweepMe/pysweepme",
                    },
        classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
        ],

        # data_files = [("", [r".\src\README.md"])],

        # license = 'MIT License',
    
        long_description=long_description,
        long_description_content_type='text/markdown',

        include_package_data=True,
        zip_safe=False,
        # dependency_links=[‘http://github.com/user/repo/tarball/master#egg=package-1.0'],

    )