import os
import sys
import shutil
from setuptools import setup
from warnings import warn

if sys.version_info.major != 3:
    raise RuntimeError('imageTable requires Python 3')


setup(name='imageTable',
      version='0.1.2',
      description='manipulation of czi and ims files',
      author='',
      author_email='',
      package_dir={'': 'src'},
      packages=['imageTable'],
      install_requires=[
          'numpy',
          'datatable',
          'h5py',
          'czifile',
          'flowkit',
          'pandas',
          ],
      scripts=['src/imageTable/image2csv.py'],
      )


# get location of setup.py
setup_dir = os.path.dirname(os.path.realpath(__file__))
