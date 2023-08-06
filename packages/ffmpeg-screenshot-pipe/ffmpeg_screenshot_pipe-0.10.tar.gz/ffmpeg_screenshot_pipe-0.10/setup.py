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
DESCRIPTION = '''Capture Screenshots with Unparalleled Speed and Versatile Features - GDIgrab, DDAgrab, Ctypes, Multiprocessing, GPU, Mouse Capture...'''

# Setting up
setup(
    name="ffmpeg_screenshot_pipe",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/ffmpeg_screenshot_pipe',
    author="Johannes Fischer",
    author_email="aulasparticularesdealemaosp@gmail.com",
    description=DESCRIPTION,
long_description = long_description,
long_description_content_type="text/markdown",
    #packages=['appshwnd', 'fast_ctypes_screenshots', 'fastimgconcat', 'get_rectangle_infos', 'getfilenuitkapython', 'getmonitorresolution', 'kthread', 'kthread_sleep', 'numpy', 'subprocess_alive', 'subprocesskiller'],
    keywords=['screenshots', 'mss', 'fast', 'win32', 'ffmpeg', 'gdigrab', 'ddagrab'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.10', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Utilities'],
    install_requires=['appshwnd', 'fast_ctypes_screenshots', 'fastimgconcat', 'get_rectangle_infos', 'getfilenuitkapython', 'getmonitorresolution', 'kthread', 'kthread_sleep', 'numpy', 'subprocess_alive', 'subprocesskiller'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*