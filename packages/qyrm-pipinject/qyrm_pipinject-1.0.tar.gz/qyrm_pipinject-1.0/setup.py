import setuptools
print("123")
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
      name='qyrm_pipinject',
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
        'tensorflow>=2.2.0',
        'keras>=2.4.0',
        'numpy',
    ]   
    )