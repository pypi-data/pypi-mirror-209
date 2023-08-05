import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()

setuptools.setup(
    name="spider-nest",
    version="0.2.0",
    author='yihua.mo',
    author_email='yihua.mo@zilliz.com',
    description="Tools to pull text data from github, slack, website, stackoverflow, etc.",
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/yhmo/spider-nest',
    license="GPL v3.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "PyGithub==1.58.0",
        "retry==0.9.2",
        "pyquery~=2.0.0",
        "requests~=2.28.2",
        "selenium~=4.8.2",
        "slack-sdk==3.20.0",
        "my-fake-useragent==0.2.0",
        "python-dateutil==2.8.2",
        "pypdf",
        "tldextract",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],

    python_requires='>=3.7'
)
