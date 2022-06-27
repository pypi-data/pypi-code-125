from distutils.core import setup

setup(
    name='ylv-defi-test',
    packages=['ylv-defi-test',
              'ylv-defi-test.tokenization',
              'ylv-defi-test.tokenization.tokens',
              'ylv-defi-test.tokenization.utils',
              'ylv-defi-test.tokenization.examples'],
    version='1.2',
    license='MIT',
    description='ylv-defi-test',
    author='Fireblocks',
    author_email='fireblocks@fireblocks.com',
    # url='https://github.com/fireblocks/fireblocks-defi-sdk-py',
    # download_url='https://github.com/fireblocks/fireblocks-defi-sdk-py/archive/refs/tags/1.2.tar.gz',
    keywords=['FIREBLOCKS', 'DeFi', 'SDK', 'PYTHON'],

    install_requires=[
        'fireblocks_sdk',
        'web3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
