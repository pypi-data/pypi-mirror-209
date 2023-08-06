import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='fyersHuMe',  
     version='0.0.2',
     author="Fyers-Tech",
     author_email="support@fyers.in",
     description="Fyers trading APIs.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/",
     packages=setuptools.find_packages(),
     install_requires=[
                'asyncio==3.4.3',
                'aiohttp==3.8.4',
                'cryptography==3.4.8',
                'Requests==2.30.0',
                'websocket_client==1.2.1'
                ,'websockets==8.1'

          ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
