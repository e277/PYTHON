import unittest
from person import Employee
from person import Person

class TestPerson(unittest.TestCase):
    def test_parent_greet(self):
        p = Person('Jennifer', 26)
        # assert correct string
        self.assertEqual(p.greet(), 'My name is, Jennifer and age is 26')
    
    def test_child_greet(self):
        e = Employee('Keneil', 25, 'Intern')
        # assert correct string
        self.assertEqual(e.greet(), "My name is, Keneil and age is 25 I'm a Intern")

if __name__ == '__main__':
    unittest.main()