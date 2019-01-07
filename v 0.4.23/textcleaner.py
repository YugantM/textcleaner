# v 0.4.17
import regex as re,string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english'))
from nltk.stem import SnowballStemmer
stemmer= SnowballStemmer('english')
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
import os.path
import copy


#removes all the blank line from the text file
#returns list
def clear_blank_lines(file):
    return document(file).clear_blank_lines().data

# it removes ".\n" from every element by default
# can be used to strip by second argument
def strip_all(file,x='.\n'):
    return document(file).strip_all(x).data


# converts each character to lowercase
def lower_all(file):
    return document(file).lower_all().data

# removes numbers detected anywhere in the data
def remove_numbers(file):
    return document(file).remove_numbers().data

# removes punctuations detected anywhere in the data
def remove_symbols(file):
    return document(file).remove_symbols().data

# it will remove stop words and return a list of list of words  
def remove_stpwrds(file,op='sents'):
    return document(file).remove_stpwrds().data

#for tokenization
def token_it(file):
    return document(file).token_it()

# reduces each word to its stem work like, dogs to dog
def stemming(file):
    return document(file).stemming().data
    
# gets the root word for each word
def lemming(file):
    return document(file).lemming().data
    

def main_cleaner(file,op = 'sents'):
    return document(file).main_cleaner().data

def formating(block):
    return [' '.join(each) for each in block]
        
    

class document:
    file_name = ''
    data = []
    words = []
    tokens = []
    count_sentences = 0
    count_words = 0
    each_word_count = {}
    
    def __init__(self,fname=''):
        
        if fname:            
            self.data,fame =  self._reader(fname)
            self.words = [each.split(' ') for each in self.clear_blank_lines().lower_all().strip_all().remove_numbers().remove_symbols()]
            self.count_words = len([word for sent in self.words for word in sent])
            self.count_sentences = sum(each.count('.') for each in self.data)
            temp = self._flatlist(self.words)
            self.each_word_count = {x:temp.count(x) for x in temp}
            self.file_name = fame.split('\\')[-1]
        else:
            pass  
        
    def _flatlist(self,lis):
        return [word for sent in lis for word in sent]
        
    def __repr__(self):
         return '\n'.join(map(str, self.data))

    def __str__(self):
        return '\n'.join(map(str, self.data))
    
    def __iter__(self):
        for i in self.data: yield i
    
    def copy(self):
        temp = copy.deepcopy(self)       
        return temp

    # checks whether it has file path as argument
    def _file_or_not(self,arg):
        if os.path.isfile(arg):
            return True
        else:
            return False,"only supports .txt for now"

    # this reader is flexible enough to process file or will return the data if list is being passed to the function.
    def _reader(self,file):
        if type(file)==str and self._file_or_not(file)==True:
            with open(file,'r') as f:
                return f.readlines(),file

        elif type(file)==str:
            return file.split('\n'),''

        else: return file,''


    
    #removes all the blank line from the text file
    #returns list
    def clear_blank_lines(self,inplace=False):
        if not inplace: self = self.copy()
        self.data =  list(filter(str.strip,[each.rstrip() for each in self.data]))
        return self

    
    # it removes ".\n" from every element by default
    # can be used to strip by second argument
    def strip_all(self,x='.\n',inplace=False):
        if not inplace: self = self.copy()
        self.data = [re.sub(r'\s+',' ',each.strip(x)) for each in self.data]
        return self


    # converts each character to lowercase
    def lower_all(self,inplace=False):
        if not inplace: self = self.copy()
        self.data = [each.lower() for each in self.data]
        return self

    # removes numbers detected anywhere in the data
    def remove_numbers(self,inplace=False):
        if not inplace: self = self.copy()
        self.data = [re.sub(r'[0-9]+', '',(each)) for each in self.data]
        return self

    # removes punctuations detected anywhere in the data
    def remove_symbols(self,inplace=False):
        if not inplace: self = self.copy()
        self.data = [re.sub(r'[^\w\s]','',each) for each in self.data]
        return self.strip_all()

    
    # it will remove stop words and return a list of list of words  
    def remove_stpwrds(self,inplace=False):
        if not inplace: self = self.copy()
        self.words = [[w for w in each.split() if not w in stop_words] for each in self.data] 
    
        self.data = formating(self.words)        
        return self
        

    #for tokenization this function can't be use as object 
    def token_it(self):
        self.tokens = [word_tokenize(each) for each in self.data]
        return self.tokens

    # reduces each word to its stem work like, dogs to dog
    def stemming(self,inplace=False):
        if not inplace: self = self.copy()
        self.data = formating([[stemmer.stem(word) for word in each.split()] for each in self.data])
        return self

    # gets the root word for each word
    def lemming(self,inplace=False):
        if not inplace: self = self.copy()
        self.data = formating([[lemmatizer.lemmatize(word) for word in each.split()] for each in self.data])
        return self


    def main_cleaner(self,op = 'sents',inplace=False):
        if not inplace: self = self.copy()
            
        # this is the basic cleaning which operates with each line
        part1 = self.clear_blank_lines().strip_all().lower_all().remove_numbers().remove_symbols()

        # this is the advanced cleaning which operates with each word
        part2 = part1.lemming().remove_stpwrds()

        if op== 'sents':
            return part2

        if op== 'words':
            return [word for sent in part2.data for word in sent.split()]        

        if op not in ('sents','words'):
            return "value of option is not valid, try 'sents' or 'words' instead" 

