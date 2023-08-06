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
DESCRIPTION = '''ADB - The fastest screenshots - scrcpy stream directly to NumPy (without scrcpy.exe) - no root required!'''

# Setting up
setup(
    name="adbblitz",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/adbblitz',
    author="Johannes Fischer",
    author_email="aulasparticularesdealemaosp@gmail.com",
    description=DESCRIPTION,
long_description = long_description,
long_description_content_type="text/markdown",
    #packages=['adbutils', 'av', 'get_free_port', 'kthread', 'kthread_sleep', 'numpy', 'subprocesskiller'],
    keywords=['port', 'tcp', 'usb', 'adb', 'screencap', 'screenshots', 'fast', 'Android'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.10', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Utilities'],
    install_requires=['adbutils', 'av', 'get_free_port', 'kthread', 'kthread_sleep', 'numpy', 'subprocesskiller'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*