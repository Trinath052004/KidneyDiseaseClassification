import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    __version__ = "0.0.0"

    REPO_NAME = "KidneyDiseaseClassification"
    AUTHOR_USER_NAME = "Trinath052004"
    SEC_REPO = "cnnClassifier"
    AUTHOR_EMAIL = "trinathcareer@gmail.com"

setuptools.setup(
    name=SEC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SEC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SEC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)