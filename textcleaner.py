
# coding: utf-8

# In[67]:


import re,string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
stemmer= PorterStemmer()
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()


# In[ ]:


#removes all the blank line from the text file
#returns list
def clear_blank_lines(file):
    data = []
    with open(file,'r') as f:
        temp = f.readlines()
        
    for line in temp:
        if line.rstrip():
            data.append(line)
    return data

# it removes ".\n" from every element by default
# can be used to strip by second argument
def strip_all(data,x='.\n'):
    return [each.strip(x) for each in data]


# converts each character to lowercase
def lower_all(data):
    return [each.lower() for each in data]

# removes numbers detected anywhere in the data
def remove_numbers(data):
    return [re.sub(r'[0-9]+', '',each) for each in data]

# removes punctuations detected anywhere in the data
def remove_symblos(data):
    return [re.sub(r'[^\w\s]','',each) for each in data]

# it will remove stop words and return a list of list of words  
def remove_stpwrds(data):
    return [[w for w in word_tokenize(each) if not w in stop_words] for each in data] 

#for tokenization
def token_it(data):
    return [[w for w in word_tokenize(each)] for each in data]

# reduces each word to its stem work like, dogs to dog
def stemming(data):
    return [[stemmer.stem(word) for word in each] for each in data]
    

# gets the root word for each word
def lemming(data):
    return [[lemmatizer.lemmatize(word) for word in each] for each in data]
    

def main_cleaner(file,op = 'sents'):
    # this is the basic cleaning which operates with each line
    part1 = remove_symblos(remove_numbers(lower_all(strip_all(clear_blank_lines(file)))))
    
    # this is the advanced cleaning which operates with each word
    part2 = lemming(stemming(remove_stpwrds(part1)))
    
    if op== 'sents':
        return part2
    
    if op== 'words':
        return [word for sent in part2 for word in sent]        
    
    if op != 'sents' or 'words':
        return "value of option is not valid, try 'sents' or 'words' instead" 

