from setuptools import setup, find_packages

setup(
    name = 'textagon',
    version = '0.1.2',
    packages = find_packages(),
    description = 'Start building textagon',
    author = 'Mendoza',
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ],
    install_requires=[
        'nltk',
        'multiprocessing',
        'scikit-learn',
        'pandas',
        'numpy',
        'beautifulsoup4',
        'mapply',
        'pyenchant',
        'tzlocal',
        'spacy',
    ]

)
