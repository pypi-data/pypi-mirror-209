import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EasyTkValidations",
    version="0.0.2",
    author="DKVG",
    author_email="gadellidk@gmail.com",
    description="To Make Easy Tkinter Entry Validations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    keywords='Validations EntryValidations TkValidations EasyTk EasyValidations EasyTkValidations',
)
