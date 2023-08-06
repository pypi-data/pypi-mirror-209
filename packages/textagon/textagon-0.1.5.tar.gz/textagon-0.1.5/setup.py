from setuptools import setup, find_packages

setup(
    name = 'textagon',
    version = '0.1.5',
    packages = find_packages(),
    description = 'Start building textagon',
    author = 'Mendoza',
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ],
    install_requires=[
        'nltk',
        'scikit-learn',
        'pandas',
        'numpy',
        'beautifulsoup4',
        'mapply',
        'pyenchant',
        'tzlocal',
        'spacy',
    ],
    entry_points={
        'console_scripts': [
            'textagon_post_install = textagon.post_install:main',
        ],
    },
    package_data={
        'textagon': ['external/lexicons/exclusions.txt'],
    }
)
