from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="abbrey",
    packages=["abbrey"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.3a",
    license="MIT",
    description="Abbreviation decoder",
    author="pdd",
    author_email="dungphamdang99@gmail.com",
    url="https://github.com/pdd-vn/abbrey",
    keywords=["abbreviation"],
    install_requires=[
        "pandas",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
