from distutils.core import setup
		
content= """

textcleaner v0.4.23
===================

Text-Cleaner is a utility library for text-data pre-processing. Use it
before passing the text data to a model.

`website <https://yugantm.github.io/textcleaner/>`__ - for more

Features!
=========

-  main\_cleaner to do all the below in one call ! or
-  remove unnecessary blank lines
-  stip out a perticular character or default one
-  transfer all characters to lowercase if needed
-  remove numbers, symblos and stop-words from the whole text
-  tokenize the text-data on one call
-  stemming & lemmatization powered by NLTK

    The goal is to make basic cleaning of data hassle free. Most of the
    developers who are working with text data have faced this situation
    where data is not consumable and they end up wasting their time on
    these issues rather than fine tunning the model and get better
    accuracy. In that scenario this library can be useful and save you a
    tone of time.

Tech
~~~~

textcleaner uses a number of open source projects to work properly:

-  `NLTK <https://www.nltk.org/>`__ - for advanced cleaning
-  `REGEX <https://pypi.org/project/regex/>`__ - for regular expression

And of course textcleaner itself is open source with a `public
repository <https://github.com/YugantM/textcleaner>`__ on GitHub.

Installation
~~~~~~~~~~~~

textcleaner requires `Python 3.x <https://www.python.org/downloads/>`__
to run.

Install the dependencies if you have not already installed it!

-  NLTK : steps to install
   [`documentation <https://www.nltk.org/install.html>`__\ ]
-  REGEX :

.. code:: sh

    pip install regex

-  textcleaner :

.. code:: sh

    pip install textcleaner

or

.. code:: sh

    pip install textcleaner==0.4.23

Usage
~~~~~

.. code:: python

    import textcleaner as tc
    tc.main_cleaner('<FILE_NAME>')
    #or
    tc.document('<FILE_NAME>')

Above command will convert the text file into list of words with
cleaning. Default response of the function is list of list use *op*
argument and set it to 'words' and you will get a flat list of words.

Todos
~~~~~

-  more advanced features
-  ability to read more formats rather than only .txt

License
-------

MIT

**Free Software, Hell Yeah!**



"""
		
setup(
  name = 'textcleaner',         # How you named your package folder (MyLib)
  packages = ['textcleaner'],   # Chose the same as "name"
  version = '0.4.23',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = '''textcleaner: text-data pre-processing library''',   # Give a short description about your #library
  long_description=content,
  author = 'Yugant Hadiyal',                   # Type in your name
  author_email = 'hadiyalyugant@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/YugantM',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/YugantM/textcleaner/archive/V0.1.tar.gz',    # I explain this later on
  keywords = ['MEANINGFULL', 'NLP', 'DATASCIENCE','DATACLEANING','PREPROCESSING'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'NLTK',
		  'REGEX',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
