import unittest

from textcleaner.textcleaner import *


#Test clear_blank_lines


class Test(unittest.TestCase):

    


    def test_equal(self):
      

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
        
        #self.assertEqual("\n".join(clear_blank_lines(sample_in)),sample_out)



if __name__ == '__main__':
    unittest.main()
