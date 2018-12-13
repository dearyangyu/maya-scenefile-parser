from setuptools import setup, find_packages
import os.path

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(HERE, *parts)) as f:
        return f.read()


setup(
    name="maya_scenefile_parser",
    version="0.1.0",
    author="Marcus Ottosson",
    description="Autodesk Maya scenefile parser",
    #long_description=read("README.rst"),
    license="MIT",
    keywords=["maya", "parser"],
    url="https://github.com/mottosso/maya-scenefile-parser",
    packages=find_packages(),
    package_data={"maya_scenefile_parser": ["modules/maya/2012/typeids.dat"]},
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
