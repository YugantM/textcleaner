# textcleaner: text pre-processing utility tool-kit

[![Downloads](https://static.pepy.tech/personalized-badge/textcleaner?period=total&units=international_system&left_color=blue&right_color=green&left_text=Downloads)](https://pepy.tech/project/textcleaner)


## What is it?

**textcleaner** is a Python package which provides utilities to pre-process textual data.


# Features!
  - main_cleaner to do all the below in one call !
  or
  - remove unnecessary blank lines
  - stip out a perticular character or default one 
  - transfer all characters to lowercase if needed
  - remove numbers, symblos and stop-words from the whole text
  - tokenize the text-data on one call
  - stemming & lemmatization powered by NLTK
  

> The goal is to make basic cleaning of data hassle free.
> Most of the developers who are working with text data have 
> faced this situation where data is not consumable
> and they end up wasting their time on these issues
> rather than fine tunning the model and get better accuracy.
> In that scenario this library can be useful and save you a tone
> of time.

### Links
Pypi address: [hyperlink](https://pypi.org/project/textcleaner/) <br>
Documentation: [hyperlink](https://yugantm.github.io/textcleaner/) <br>



### Tech

textcleaner uses a number of open source projects to work properly:

- [NLTK](https://www.nltk.org/) - for advanced cleaning
- [REGEX](https://pypi.org/project/regex/) - for regular expression

And of course textcleaner itself is open source with a [public repository](https://github.com/YugantM/textcleaner)
 on GitHub.

### Installation

textcleaner requires [Python 3.x](https://www.python.org/downloads/) to run.

Install the dependencies if you have not already installed it!

- NLTK : steps to install [[documentation](https://www.nltk.org/install.html)]
- REGEX : 

```sh
pip install regex
```
- textcleaner : 

```sh
pip install textcleaner
```
or
```sh
pip install textcleaner==0.4.23
```
### Usage

```python
import textcleaner as tc
tc.main_cleaner('<FILE_NAME>')
#or
tc.document('<FILE_NAME>')
```
Above command will convert the text file into list of words with cleaning. Default response of the function is list of list use *op* argument and set it to 'words' and you will get a flat list of words.

### Todos

 - more advanced features
 - ability to read more formats rather than only .txt



License
----

MIT


**Free Software, Hell Yeah!**


   
