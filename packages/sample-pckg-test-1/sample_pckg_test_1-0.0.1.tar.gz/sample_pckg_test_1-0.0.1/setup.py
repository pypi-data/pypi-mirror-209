import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "sample_pckg_test_1",
    version = "0.0.1",
    author = "harshith",
    author_email = "harshith@ex.com",
    description = "short package description",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
)
