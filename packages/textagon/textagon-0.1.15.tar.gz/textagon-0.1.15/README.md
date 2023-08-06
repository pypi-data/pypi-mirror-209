<!-- # Textagon
Textagon is a project to help you analyze your text data. You can see its parallel representations and find out how different types of lexicon can add differentiations give two classes of text data.
 - ReadAllLexicons: process the lexicon file
 - SanityCheck: make sure the data is valid and well organized
 - ReadRawText: call SanityCheck function, return the pure text data, and return class labels
 - setSpellChecking: This is to setup spellchecker. 
            NOTE: if you want to use custom exclusion file, you need to specify your exclusion file in the downstream function calling.
 - TextToFeatures: 

# Setup:
 - First time: 
    - pip install textagon
    - textagon_post_install
 - Upgrade:
    - pip install --upgrade textagon
    - textagon_post_install

# Update package:
 - delete all generated folders (/build, /dist, /textagon.egg-info)
 - run "python setup.py sdist bdist_wheel"
 - run "twine upload dist/*" -->

# Textagon

Textagon is a powerful tool for text data analysis, providing a means to visualize parallel representations of your data and gain insight into the impact of various lexicons on two classes of text data.

## Core Functions

- **ReadAllLexicons**: Processes the lexicon file.
- **SanityCheck**: Ensures the data is valid and well-organized.
- **ReadRawText**: Invokes the SanityCheck function to return pure text data and class labels.
- **setSpellChecking**: Sets up the spellchecker. Note: If you wish to use a custom exclusion file, you must specify your exclusion file in the downstream function call.
- **TextToFeatures**: [Add description here]

## Installation

### Initial Setup

1. Install the package using pip: *pip install textagon*
2. Run the post-installation script: *textagon_post_install*


### Upgrading Textagon

1. Upgrade the package using pip: *pip install --upgrade textagon*
2. Run the post-installation script: *textagon_post_install*


## Updating the Package for Development

If you are developing the Textagon package and need to update it, follow these steps:

1. Delete all generated folders (`/build`, `/dist`, `/textagon.egg-info`).
2. Run the setup script to create the distribution files: *python setup.py sdist bdist_wheel*
3. Upload the package to PyPI using Twine: twine upload dist/*

