from distutils.core import setup

setup(
  name = 'DataGlitch',         
  packages = ['DataGlitch'],   
  version = '0.0.1',      
  license='MIT',        
  description = 'DataGlitch is a Python package designed to address common data challenges, including handling mixed data types, non-ASCII values, and facilitating dataset exploration.',   
  author = 'Ioakeim Hadjimpalasis',                   
  author_email = 'ioakeim.h@gmail.com',      
  url = 'https://github.com/ioakeim-h/DataGlitch',  
  download_url = 'https://github.com/ioakeim-h/DataGlitch/archive/refs/tags/v0.1.tar.gz',    
  keywords = ['data', 'cleaning', 'wrangling', 'engineering', 'pandas'],   
  install_requires=[            
          'rapidfuzz',
          'pandas',
          'numpy',
          'unidecode',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.9'
  ],
)