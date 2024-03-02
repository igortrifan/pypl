from setuptools import setup, find_packages

setup(
    name="proj-library",
    version="0.0.1",
    author="igortrifan",
    author_email="trifan.igor.xd@gmail.com",
    url="",
    description="calculate number of trees",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["proj-library=proj-library.main:download"]},
)