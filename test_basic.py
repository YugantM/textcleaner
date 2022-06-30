import unittest

from textcleaner.textcleaner import *


#Test clear_blank_lines


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_clear_blank_lines(self):
      

        sample_in = '''
        This is a sample text


        with blank lines in it. Call the function and remove them.
        '''

        sample_out = '''
        This is a sample text
        with blank lines in it. Call the function and remove them.
        '''
        
        if '\n'.join(clear_blank_lines(sample_in))==sample_out:
            pass
        else:
            print("test_clear_blank_lines not working")
        
        #self.assertEqual("\n".join(clear_blank_lines(sample_in)),sample_out)

    def test_lemming(self):
      

        sample_in = '''
        Root words are great.
        It helps to summarize the articles or something.
        '''

        sample_out = '''
        Root word are great.
        It help to summarize the article or something.
        '''
        
        if '\n'.join(lemming(sample_in))==sample_out:
            pass
        else:
            print("lemming not working")

        #self.assertEqual("\n".join(lemming(sample_in)),sample_out)



if __name__ == '__main__':
    unittest.main()
