from setuptools import setup


def read_me():
    with open("README.md", "r") as file:
        return file.read()


def version():
    with open("VERSION", "r") as file:
        return file.read()


__version__ = version()

# /tunapro1234/proprepros/archive/v0.0.10-alpha.tar.gz

setup(
    name="ppps",
    license="MIT",
    zip_safe=False,
    packages=["ppps"],
    version=__version__,
    author="TUNAPRO1234",
    long_description=read_me(),
    include_package_data=True,
    author_email="tunagul54@gmail.com",
    url="https://github.com/tunapro1234/proprepros/",
    description="pre-preprocessor for C/C++",
    keywords=["c", "preprocessor", "pre-preprocessor"],
    download_url=
    f"https://github.com/tunapro1234/proprepros/archive/v{__version__}-alpha.tar.gz",
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
    ],
)
