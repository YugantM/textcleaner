import unittest

from textcleaner.textcleaner import *


#Test clear_blank_lines


class basicTests(unittest.TestCase):


    def clear_blank_lines_func(self):
      

        sample_in = '''
        This is a sample text


        with blank lines in it. Call the function and remove them.
        '''

        sample_out = '''
        This is a sample text
        with blank lines in it. Call the function and remove them.
        '''
        
        #if '\n'.join(clear_blank_lines(sample_in))==sample_out:
            #pass
        self.assertAlmostEqual(clear_blank_lines(sample_in),sample_out)
        self.assertEqual("\n".join(clear_blank_lines(sample_in)),sample_out)

    def lemming_func(self):
      

        sample_in = '''
        Root words are great.
        It helps to summarize the articles or something.
        '''

        sample_out = '''
        Root word are great.
        It help to summarize the article or something.
        '''
        
        #if '\n'.join(lemming(sample_in))==sample_out:
        #    pass

        self.assertEqual("\n".join(lemming(sample_in)),sample_out)



if __name__ == '__main__':
    unittest.main()
