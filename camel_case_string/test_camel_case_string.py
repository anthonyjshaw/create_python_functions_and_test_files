import unittest
from camel_case_string import camel_case_string, screaming_case_string


class TestCamelCaseString(unittest.TestCase):
	def test_camel_case_string(self):
		self.assertEqual(camel_case_string('camel_case'), 'camelCase', "Should convert snake case into camelCase")

class TestScreamingCaseString(unittest.TestCase):
	def test_screaming_case_string(self):
		self.assertEqual(screaming_case_string('camel_case'), 'CamelCase', 'Should convert snake case into ScreamingCase')

if __name__ == '__main__':
    unittest.main()