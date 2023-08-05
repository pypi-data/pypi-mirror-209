from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_des = str(f.read())

setup(
    name='Flet StoryBoard',
    version='1.4',
    author='SKbarbon',
    description='A UI-Builder that helps programmers build the front-end without codding it.',
    long_description=long_des,
    long_description_content_type='text/markdown',
    url='https://github.com/SKbarbon/Flet-StoryBoard',
    install_requires=["flet==0.5.2", "requests"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
)