import setuptools
from pdfman import __version__

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="pdfman",
    version=__version__,
    author="Jak Bin",
    description="A python package for editing pdf",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jakbin/pdfman",
    project_urls={
        "Bug Tracker": "https://github.com/jakbin/pdfman/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='pdf,python-pdf,splitpdf,pypdf,pdfman',
    python_requires=">=3.6",
    install_requires=['PyPDF2'],
    packages=["pdfman"],
    entry_points={
        "console_scripts":[
            "pdfman = pdfman:cli.main"
        ]
    }
)
