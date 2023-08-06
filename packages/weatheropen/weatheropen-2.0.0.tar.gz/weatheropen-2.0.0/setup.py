from setuptools import setup

setup(
    name='weatheropen',  # (Required) The name of the library
    packages=['weatheropen'],  # (Required) The list of packages to include into the library
    version='2.0.0',          # (Required) The library version. It will be increased with library changes
    license='MIT',            # Type of license.
    description='Weather forecast data',  # Short description of the library
    author='geokzms',                     # Your name
    author_email='geokzms@example.com',   # Your email
    url='https://example.com',            # Homepage of your library e.g. Github or your website
    keywords=['weather', 'forecast', 'openweather'],  # Keywords users can search on pypi
    install_requires=['requests',],          # Other 3rd party libraries that pip needs to install
    classifiers=[
        'Development Status :: 3 - Alpha',  # Choose either "3 - Alpha", "4 - Beta", or "5 - Production/Stable"
        'Intended Audience :: Developers',  # Who is the audience of your library ?
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Type a license again
        'Programming Language :: Python :: 3.5',   # Python versions your library supports
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
