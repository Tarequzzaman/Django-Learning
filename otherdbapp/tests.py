import requests
import unittest


from django.test import Client, RequestFactory
from unittest.mock import patch
from .views import create_user, get_user, get_id
from django.urls import reverse

# Create your tests here.



class TestView(unittest.TestCase):
 
    def test_sum(self):
            self.assertEqual(sum([1, 2, 3]), 6)

    def test_create_users(self):
        client = Client()
        response= client.get(reverse(create_user), {'first_name': 'john', 'last_name': 'smith', 'phone': "01838198104", 'email': "tareqcse12@gmail.com"})
        self.assertEqual(response.status_code, 200)


    def test_get_user(self):
        client = Client()
        response= client.get(reverse(get_user))
        self.assertEqual(response.status_code, 450)


    def test_get_id(self):
        ion = get_id(100)
        self.assertEqual(ion, 100)






if __name__ == '__main__':
    unittest.main()