
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english'))
from nltk.stem import SnowballStemmer
stemmer= SnowballStemmer('english')
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
import os.path


# checks whether it has file path as argument
def file_or_not(arg):
    if os.path.isfile(arg):
        return True
    else:
        return False,"only supports .txt for now"
    
# this reader is flexible enough to process file or will return the data if list is being passed to the function.
def reader(file):
    if type(file)==str and file_or_not(file)==True:
        with open(file,'r') as f:
            return f.readlines()
        
    else: return file

# data handler
def data_handler(file):
    if type(file) == list:
        if type(file[0])== str:
            return file

        if type(file[0])==list:
            return file
                    
    if type(file[0]) == str:
        return file.split()
    
#removes all the blank line from the text file
#returns list
def clear_blank_lines(file):
    return list(filter(str.strip,[each.rstrip() for each in reader(file)]))


# it removes ".\n" from every element by default
# can be used to strip by second argument
def strip_all(file,x='.\n'):
    return [each.strip(x) for each in reader(file)]


# converts each character to lowercase
def lower_all(file):
    return [each.lower() for each in reader(file)]

# removes numbers detected anywhere in the data
def remove_numbers(file):
    return [re.sub(r'[0-9]+', '',(each)) for each in reader(file)]

# removes punctuations detected anywhere in the data
def remove_symblos(file):
    return [re.sub(r'[^\w\s]','',each) for each in reader(file)]

# it will remove stop words and return a list of list of words  
def remove_stpwrds(file):
    return [[w for w in data_handler(each) if not w in stop_words] for each in reader(file)] 

#for tokenization
def token_it(file):
    return [[w for w in each] for each in reader(file)]

# reduces each word to its stem work like, dogs to dog
def stemming(file):
    return [[stemmer.stem(word) for word in data_handler(each)] for each in reader(file)]
    
# gets the root word for each word
def lemming(file):
    return [[lemmatizer.lemmatize(word) for word in data_handler(each)] for each in reader(file)]
    

def main_cleaner(file,op = 'sents'):
    # this is the basic cleaning which operates with each line
    part1 = remove_symblos(remove_numbers(lower_all(strip_all(clear_blank_lines(reader(file))))))
    
    # this is the advanced cleaning which operates with each word
    part2 = lemming(stemming(remove_stpwrds(part1)))
    
    if op== 'sents':
        return part2
    
    if op== 'words':
        return [word for sent in part2 for word in sent]        
    
    if op not in ('sents','words'):
        return "value of option is not valid, try 'sents' or 'words' instead" 

