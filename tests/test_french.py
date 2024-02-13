import unittest

import test_fixtures_ro
from french import translate_text
from tests import test_fixtures_fr


class TestConversion(unittest.TestCase):
    def test_translate_text_romanian(self):
        for input_text in test_fixtures_ro.TEST_INPUT:
            result, audio = translate_text(input_text)
            self.assertEqual(result.upper(), test_fixtures_ro.TEST_OUTPUT[test_fixtures_ro.TEST_INPUT.index(input_text)].upper())


    def test_translate_text_french(self):
        for input_text in test_fixtures_fr.TEST_INPUT:
            result, audio = translate_text(input_text)
            self.assertEqual(result.upper(), test_fixtures_fr.TEST_OUTPUT[test_fixtures_fr.TEST_INPUT.index(input_text)].upper())


if __name__ == '__main__':
    unittest.main()
