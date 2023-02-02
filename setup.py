from setuptools import setup

setup(
    name='ExoScanner',
    version='0.2.0',    
    description='A program to analyze an image-series for exoplanet transits.',
    url='https://github.com/josia-john/ExoScanner',
    author='Josia John',
    author_email='me@jlabs.anonaddy.com',
    packages=['ExoScanner'],
    install_requires=['matplotlib',
                      'numpy',                    
                      'astropy',
                      'statistics',
                      'photutils',
                      'scipy'
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Programming Language :: Python :: 3'
    ],
)