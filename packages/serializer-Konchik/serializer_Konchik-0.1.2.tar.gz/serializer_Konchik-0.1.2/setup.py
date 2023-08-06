# Always prefer setuptools over distutils
from setuptools import setup

# This call to setup() does all the work
setup(
    name="serializer_Konchik",
    version="0.1.2",
    description="JSON / XML serializer",
    author="Denis Konchik",
    author_email="denis.pptx@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent"
    ],
    packages=["src", "src.packer", "src.serializer"],
    include_package_data=True,
    install_requires=["regex"]
)
