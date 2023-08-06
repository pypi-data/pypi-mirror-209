from distutils.core import setup

long_desc = """Helper package for requesting token and generating request signatures to be used for consuming Bank Mandiri API.

Example usage:

```python
from MandiriUtils import Client

client = Client(url="https://sandbox.bankmandiri.co.id", pk=my_private_key_content, pk_pass=pk_pass, client_id=client_id, client_secret=client_secret, tz_offset="+0700")
result = client.get_token()

print(result)
```
"""

setup(
  name = 'MandiriUtils',         
  packages = ['MandiriUtils'],   
  version = '0.14',      
  license='MIT',        
  description = 'Helper package for requesting token and generating request signatures to be used for consuming Bank Mandiri API',
  long_description = long_desc,
  long_description_content_type='text/markdown',

  author = 'Hanif Amal Robbani',       
  author_email = 'dev.har07@gmail.com',
  url = 'https://github.com/har07',
  download_url = 'https://github.com/har07/mandiri-utils/archive/refs/tags/v_014.tar.gz', 
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