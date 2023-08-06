import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires=[
    'numpy',
    'pysoundfile'
]

setuptools.setup(
    name="soundmaker",
    version="1.0.0",
    author="Simon Kojima",
    author_email="simon.kojima@outlook.com",
    description="The library generates various tone stimuli for psychophysiological experiments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simonkojima/soundmaker",
    project_urls={
        "Bug Tracker": "https://github.com/simonkojima/soundmaker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = install_requires,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)