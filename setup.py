"""Classes for help wth game creation"""

classifiers = """\
Development Status :: 2 - Pre-Alpha
Intended Audience :: Developers
Programming Language :: Python
License :: Public Domain
Operating System :: OS Independent
Topic :: Games/Entertainment
"""

from distutils.core import setup
from gameobjects.__init__ import __version__

print("Game Objects v" + __version__)

doclines = __doc__.split("\n")

setup(name='gameobjects',
      version=__version__,
      author='Will McGugan',
      author_email='will@willmcgugan.com',
      maintainer="renmu",
      license="public domain",
      url='https://github.com/renmu123/gameobjectsForPython3',
      download_url='https://github.com/renmu123/gameobjectsForPython3',
      platforms=['any'],
      description=doclines[0],
      long_description='\n'.join(doclines[2:]),
      # package_dir = {'gameobjects': './gameobjects'},
      packages=['gameobjects'],
      classifiers=classifiers.splitlines(),
      )
