from setuptools import setup, find_packages
# import codecs
# import os
# 
# here = os.path.abspath(os.path.dirname(__file__))
# 
# with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()\

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '''0.10'''
DESCRIPTION = '''Screenshots in record time - up to 2.5x faster than MSS (Multiple Screen Shots)'''

# Setting up
setup(
    name="fast_ctypes_screenshots",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/fast_ctypes_screenshots',
    author="Johannes Fischer",
    author_email="aulasparticularesdealemaosp@gmail.com",
    description=DESCRIPTION,
long_description = long_description,
long_description_content_type="text/markdown",
    #packages=['getmonitorresolution', 'numpy'],
    keywords=['screenshots', 'mss', 'fast', 'win32'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.10', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Utilities'],
    install_requires=['getmonitorresolution', 'numpy'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*