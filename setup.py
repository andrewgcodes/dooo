from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dooo",
    version="0.1.5",
    packages=find_packages(),
    install_requires=[
        "litellm",
        "numpy",
        "pandas",
        "matplotlib",
        "scipy",
        "requests",
    ],
    author="Andrew Gao and William Gao",
    author_email="olafblitz@gmail.com",
    description="A Python package to make LLMs easy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andrewgcodes/dooo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)