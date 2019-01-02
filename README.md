# textcleaner V0.4.6


Text-Cleaner is a utility library for text-data pre-processing. Use it before passing the text data to a model.


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
pip install textcleaner==0.4.6
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


   
