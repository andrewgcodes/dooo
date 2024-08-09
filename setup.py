from setuptools import setup, find_packages

setup(
    name="dooo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "litellm",
        "numpy",
        "pandas",
        "matplotlib",
        "scipy",
        "requests",
    ],
    author="Andrew and William Gao",
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