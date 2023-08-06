from distutils.core import setup
setup(
    name='ejelabs',
    packages=['ejelabs'],
    version='0.2',
    license='MIT',
    description='ejelabs',
    author='Looq',
    author_email='looqifi@gmail.com',
    url='https://github.com/looqify/Instalabs',
    download_url='https://github.com/looqify/Instalabs/archive/refs/tags/0.2.tar.gz',
    keywords=['looq'],
    install_requires=[
        'pycryptodomex',
        'PyNaCl',
        'fake-useragent'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
