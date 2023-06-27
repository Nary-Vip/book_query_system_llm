import setuptools

__version__ = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

REPO_NAME = "book_query_system_llm"
AUTHOR_USER_NAME = "Nary-Vip"
SRC_REPO = "BookQuery"
AUTHOR_EMAIL = "nary2vip@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A book query system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)