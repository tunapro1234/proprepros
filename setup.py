from setuptools import setup

__version__ = "0.0.10"


def read_me():
    with open("README.md", "r") as file:
        return file.read()


setup(
    name="dbex",
    license="MIT",
    zip_safe=False,
    packages=["ppps"],
    version=__version__,
    author="TUNAPRO1234",
    long_description=read_me(),
    include_package_data=True,
    author_email="tunagul54@gmail.com",
    url="https://github.com/tunapro1234/proprepros/",
    description="json-like encoder and decoder",
    keywords=["json", "file", "encryption", "save", "data"],
    download_url=
    "https://github.com/tunapro1234/proprepros/archive/v0.0.10.tar.gz",
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
    ],
)
