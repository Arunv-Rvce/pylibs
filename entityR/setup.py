import setuptools

with open('requirements.txt') as f:
    reqs = f.read().split('\n')

setuptools.setup(
     name='entityR',
     version='0.1',
     scripts=[],
     author="Arun V",
     author_email="arunvrvce@gmail.com",
     description="Python Library For Linking The Entity Relationship",
     long_description="Python Library For Linking The Entity Relationship Similar To DBMS Entity Relationship",
     long_description_content_type="text/markdown",
     url="https://github.com/Arunv-Rvce/pylibs.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "Operating System :: OS Independent",
     ],
     install_requires=reqs
)