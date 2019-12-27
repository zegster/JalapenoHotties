import unittest
import make_codebook


class test_codebook(unittest.TestCase):

    ########################################################
    # Testing validate() passing word with limit for words #
    ########################################################
    def test_validate(self):
        result = make_codebook.validate("cosine", 6)
        self.assertEqual(result, True)

    ######################################################
    # Testing parse_message() passing word with option 1 #
    ######################################################
    def test_parse_message(self):
        result = make_codebook.parse_message("cosine sine", 1)
        self.assertEqual(result, False)

    def test_parse_message(self):
        result = make_codebook.parse_message("cosine, sine", 1)
        self.assertEqual(result, ['cosine', 'sine'])

    ######################################################
    # Testing parse_message() passing word with option 2 #
    ######################################################
    def test_parse_message(self):
        result = make_codebook.parse_message("cosine and sine, test and sine", 2)
        self.assertEqual(result, ['cosine and sine', 'test and sine'])

    def test_parse_message(self):
        result = make_codebook.parse_message("cosine and sine, test and sine, test, test ,test, test, test", 2)
        self.assertEqual(result, False)

    ######################################################
    # Testing parse_message() passing word with option 3 #
    ######################################################
    def test_parse_message(self):
        result = make_codebook.parse_message("cosine sine 2 14", 3)
        self.assertEqual(result, [['cosine', 'sine', '2', '14']])

    def test_parse_message(self):
        result = make_codebook.parse_message("cosine sine 1 14", 3)
        self.assertEqual(result, False)

    def test_parse_message(self):
        result = make_codebook.parse_message("cosine sine 2 16", 3)
        self.assertEqual(result, False)

    def test_parse_message(self):
        result = make_codebook.parse_message("cosine 1 14", 3)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
