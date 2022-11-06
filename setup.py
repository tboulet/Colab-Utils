from setuptools import setup, find_namespace_packages

setup(
    name="colab_notebook_utils",
    url="https://github.com/tboulet/Colab-Utils", 
    author="Timothé Boulet",
    author_email="timotheboulet0@gmail.com",
    
    packages=find_namespace_packages(),

    version="1.0.1",
    license="MIT",
    description="Usefull tools for dealing with colab notebooks",
    long_description=open('README.md').read(),   
    long_description_content_type="text/markdown", 
)
