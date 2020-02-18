import unittest

import sys
sys.path.append('src/')

from spark_streamer_service import line_to_json

class TestNetCatConsumer(unittest.TestCase):
    def test_valid_line(self):
        validJson = '{"Id": 2, "Url": "https://test.com", "Time": 123459}'
        actual = line_to_json(validJson)
        self.assertTrue(actual[0] == 2)
        self.assertTrue(actual[1][0] == "https://test.com")
        self.assertTrue(actual[1][1] == 123459)

    def test_invalids(self):
        validJson = '{"Id": "asdf", "Url": "https://test.com", "Time": 123459}'
        actual = line_to_json(validJson)
        self.assertTrue(actual[0] == -1)

if __name__ == '__main__':
    unittest.main()
