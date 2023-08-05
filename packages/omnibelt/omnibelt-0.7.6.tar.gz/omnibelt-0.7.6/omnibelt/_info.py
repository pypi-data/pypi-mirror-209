

name = 'omnibelt'
long_name = 'omni-belt'

version = '0.7.6'
url = 'https://github.com/felixludos/omni-belt'

description = 'Universal python utilities'

author = 'Felix Leeb'
author_email = 'felixludos.info@gmail.com'

license = 'MIT'

readme = 'README.md'

packages = ['omnibelt']

import os
try:
	with open(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'requirements.txt'), 'r') as f:
		install_requires = f.readlines()
except:
	install_requires = ['pyyaml', 'dill', 'wrapt>=1.11.2', 'cryptography>=2.7', 'indexed>=1.3.0']
del os


