from distutils.core import setup

setup(
  name = 'MandiriUtils',         
  packages = ['MandiriUtils'],   
  version = '0.10',      
  license='MIT',        
  description = 'Helper package for requesting token and generating request signatures to be used for consuming Bank Mandiri API',
  author = 'Hanif Amal Robbani',       
  author_email = 'dev.har07@gmail.com',
  url = 'https://github.com/har07',
  download_url = 'https://github.com/har07/mandiri-utils/archive/refs/tags/v_010.tar.gz', 
  keywords = ['banking', 'signature', 'token', 'mandiri'], 
  install_requires=[
          'pycryptodome==3.17.0',
          'requests==2.22.0',
          'pyjks==20.0.0',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
  ],
)