from django.test import TestCase


#inherit functionality from TestCase
class TestDjango(TestCase):
    def test_this_thing_works(self):
        #test if 1 = 0 (this test should pass)
        self.assertEqual(1, 1)
    
    def test_this_thing_works2(self):
        #test if 1 = 0 (this test should fail)
        self.assertEqual(1, 3)

    def test_this_thing_works3(self):
        #test if 1 = 0 (this test should have a syntax error)
        self.assertEqual(1, )

    def test_this_thing_works4(self):
        #test if 1 = 0 (this test should fail)
        self.assertEqual(1, 4)