import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    version="1.0.0",
    author="https://github.com/kivy-garden/garden.matplotlib",
    description="Just a setup to get this online",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MFA-X-AI/garden.matplotlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)