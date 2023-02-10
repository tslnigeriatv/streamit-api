from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient
from api.models import Profile
from users.models import CustomUser
import json

class TestUserProfile(APITestCase):
    
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api'
        self.my_client = RequestsClient()
        
        self.response = self.my_client.post(f'{self.base_url}/user/', json={
            "email": "daniel@gmail.com",
            "password": "mypasswordgood",
            "password2": "mypasswordgood"
        })
        
        self.user = CustomUser.objects.get(id=1)
        self.profile = self.user.profile
        self.user_token_key = self.user.auth_token.key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.user_token_key}'
        }
        
        # The difference between self.client and self.my_client is that
        # self.client is an instance atrribute of APITestCase while 
        # self.my_client is an instance of RequestClient().
        # Here, both of them can be used interchangeably, although the main
        # differnce is that `headers` cannot be passed to self.client.[HTTP_METHOD]
        # instance while they can be passed to self.my_client.[HTTP_METHOD]


    def tearDown(self):
        return super().tearDown()
    
    def test_create_user_with_unmatched_password(self):
        response = self.my_client.post(f'{self.base_url}/user/', json={
            "email": "tony@gmail.com",
            "password": "firstpassword",
            "password2": "secondpassword"
        })
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error']['details']['password'], 'Password must match')
    
    def test_user_profile_exists(self):
        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(self.profile.id, self.user.id)
        self.assertEqual(self.user.email, "daniel@gmail.com")
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertIsInstance(self.user_token_key, str)
        
    def test_retrieve_user_and_profile_list(self):
        user_list = self.my_client.get(f'{self.base_url}/user/', headers=self.headers)
        profile_list = self.my_client.get(f'{self.base_url}/profile/', headers=self.headers)
        
        self.assertEqual(user_list.status_code, 200)
        self.assertEqual(profile_list.status_code, 200)
        
    def test_retrieve_single_user_and_profile(self):
        single_user = self.my_client.get(f'{self.base_url}/user/1/', headers=self.headers)
        single_profile = self.my_client.get(f'{self.base_url}/profile/1/', headers=self.headers)

        self.assertEqual(single_user.status_code, 200)
        self.assertEqual(single_profile.status_code, 200)
        self.assertIsInstance(single_user.json(), dict)
        self.assertIsInstance(single_profile.json(), dict)
        
    def test_authenticate_correct_user_credentials(self):
        url = f"{self.base_url}/user/auth-token/"
        response = self.client.post(url, {'username': 'daniel@gmail.com', 'password': 'mypasswordgood'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user_token_key, response.json()['token'])
        self.assertEqual(self.user.id, response.json()['user_id'])
        self.assertEqual(self.user.email, response.json()['email'])
        
    def test_authenticate_wrong_user_credentials(self):
        url = f"{self.base_url}/user/auth-token/"
        response = self.client.post(url, {'username': 'daniel@gmail.com', 'password': 'wrongpassword'})
        self.assertTrue(response.json()['error']['status_code'], 400)
        
    def test_delete_user_alongside_user_profile(self):
        response = self.my_client.delete(f'{self.base_url}/user/1/', headers=self.headers)
        self.assertEqual(response.status_code, 204)
    
    
    
    
    


