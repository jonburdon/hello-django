from django.test import TestCase


#inherit functionality from TestCase
class TestDjango(TestCase):
    def test_this_thing_works(self):
        #test if 1 = 0 (this test should pass)
        self.assertEqual(1, 1)
        