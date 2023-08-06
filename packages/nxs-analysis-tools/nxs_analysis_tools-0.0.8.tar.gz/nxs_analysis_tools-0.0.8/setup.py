from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['matplotlib>=3.0.0',
                'numpy>=1.0.0',
                'ipython>=1.0.0',
                'python>=3.7.0',
                ]

# some more details
CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Image Processing',
    'Topic :: Scientific/Engineering :: Physics',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function 
setup(name='nxs_analysis_tools',
      version='0.0.8',
      description='Tools for analyzing scattering data in .nxs format.',
      long_description=long_description,
      url='https://github.com/stevenjgomez/nxs_analysis_tools',
      author='Steven J. Gomez Alvarado',
      author_email='stevenjgomez@ucsb.edu',
      license='MIT',
      packages=['nxs_analysis_tools'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='diffraction xrd nexusformat nexus nxs scattering'
      )
