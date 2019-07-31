import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='EasyAsync',
     version='1.2',
     author="Tanner Burns",
     author_email="tjburns102@gmail.com",
     description="An easy way to use asyncio with existing python3 code",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/tannerburns/easyasync",
     package_dir={'':'src'},
     packages=setuptools.find_packages("src"),
     include_package_data=True,
     install_requires=[
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )