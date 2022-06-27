import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
setuptools.setup(
    name = 'sportstat',
    version = '2.0.0',
    author = 'Bernard Ojengwa',
    author_email = 'bernardojengwa@gmail.com',
    description = 'Package for scraping soccer data from a variety of sources.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/ojengwa/ScraperFC',
    package_dir = {'':'code'},
    packages = setuptools.find_packages(where='code'),
    keywords = ["soccer","football","Premier League","Serie A",
                "La Liga","Bundesliga","Ligue 1",'web scraping',
                'data'],
    install_requires = ['selenium', 
                        'webdriver-manager',
                        'pandas',
                        'numpy',
                        'datetime',
                        'ipython',
                        "requests",
                        "bs4",
                        "lxml",
                        "tqdm"],
    classifiers = ['Programming Language :: Python :: 3',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent'],
    python_requires = '>=3.6'
)
  