from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient
from api.models import Profile, Actor
from users.models import CustomUser
import json


class SetUpTestCase(APITestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/'
        self.my_client = RequestsClient()
        
        self.response = self.my_client.post(f'{self.base_url}api/user/', json={
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
        
        
        self.director = self.my_client.post(f'{self.base_url}api/directors/', headers=self.headers, json={
            "name": "Victoria Osifo",
            "bio": "My name is Victoria Osifo.",
            "image": None
        })
        
        self.actor = self.my_client.post(f'{self.base_url}api/actors/', headers=self.headers, json={
            "name": "Victoria Osifo",
            "bio": "My name is Victoria Osifo.",
            "image": None
        })
        
        self.mood = self.my_client.post(f'{self.base_url}api/moods/', headers=self.headers, json={
            "name": "Happy"
        })
        
        self.category = self.my_client.post(f'{self.base_url}api/categories/', headers=self.headers, json={
            "name": "Hot Stuff"
        })
        self.playlist = self.my_client.post(f'{self.base_url}api/playlists/', headers=self.headers, json={
            "title": "My Playlist"
        })
        
    
    def tearDown(self):
        return super().tearDown()

class TestUserProfile(SetUpTestCase):
    def test_create_user_with_unmatched_password(self):
        response = self.my_client.post(f'{self.base_url}api/user/', json={
            "email": "tony@gmail.com",
            "username": "tony",
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
        user_list = self.my_client.get(f'{self.base_url}api/user/', headers=self.headers)
        profile_list = self.my_client.get(f'{self.base_url}api/profile/', headers=self.headers)
        
        self.assertEqual(user_list.status_code, 200)
        self.assertEqual(profile_list.status_code, 200)
        
    def test_retrieve_single_user_and_profile(self):
        single_user = self.my_client.get(f'{self.base_url}api/user/1/', headers=self.headers)
        single_profile = self.my_client.get(f'{self.base_url}api/profiles/1/', headers=self.headers)

        self.assertEqual(single_user.status_code, 200)
        self.assertEqual(single_profile.status_code, 200)
        self.assertIsInstance(single_user.json(), dict)
        self.assertIsInstance(single_profile.json(), dict)
        
    def test_authenticate_correct_user_credentials(self):
        url = f"{self.base_url}auth/token/login"
        response = self.client.post(url, {'email': 'daniel@gmail.com', 'password': 'mypasswordgood'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user_token_key, response.json()['auth_token'])
        
    def test_delete_user_alongside_user_profile(self):
        response = self.my_client.delete(f'{self.base_url}api/user/1/', headers=self.headers)
        self.assertEqual(response.status_code, 204)
        

class TestActor(SetUpTestCase):
    def test_actor_is_created(self):
        self.assertEqual(self.actor.status_code, 201)
        self.assertIsInstance(self.actor.json(), dict)
        self.assertEqual(self.actor.json()['id'], 1)
        self.assertEqual(self.actor.json()['name'], 'Victoria Osifo')
        self.assertEqual(self.actor.json()['_videos'], [])
        self.assertEqual(self.actor.json()['image'], None)
        self.assertEqual(self.actor.json()['bio'], "My name is Victoria Osifo.")
        
    def test_get_actor_created(self):
        actor = self.my_client.get(f'{self.base_url}api/actors/', headers=self.headers)
        self.assertEqual(actor.status_code, 200)
        self.assertIsInstance(actor.json(), list)

        
    def test_get_single_created(self):
        actor = self.my_client.get(f'{self.base_url}api/actors/1/', headers=self.headers)
        self.assertEqual(actor.status_code, 200)
        self.assertIsInstance(actor.json(), dict)
        


class TestDirector(SetUpTestCase):
    def test_director_is_created(self):
        self.assertEqual(self.director.status_code, 201)
        self.assertIsInstance(self.director.json(), dict)
        self.assertEqual(self.director.json()['id'], 1)
        self.assertEqual(self.director.json()['name'], 'Victoria Osifo')
        self.assertEqual(self.director.json()['_videos'], [])
        self.assertEqual(self.director.json()['image'], None)
        self.assertEqual(self.director.json()['bio'], "My name is Victoria Osifo.")
        
    def test_get_director_created(self):
        director = self.my_client.get(f'{self.base_url}api/directors/', headers=self.headers)
        self.assertEqual(director.status_code, 200)
        self.assertIsInstance(director.json(), list)

        
    def test_get_single_created(self):
        director = self.my_client.get(f'{self.base_url}api/directors/1/', headers=self.headers)
        self.assertEqual(director.status_code, 200)
        self.assertIsInstance(director.json(), dict)


class TestMood(SetUpTestCase):
    def test_mood_is_created(self):
        self.assertEqual(self.mood.status_code, 201)
        self.assertEqual(self.mood.json()['id'], 1)
        self.assertEqual(self.mood.json()['name'], "Happy")
        self.assertEqual(self.mood.json()['_videos'], [])
        self.assertIsInstance(self.mood.json()['_videos'], list)
        
    def test_get_all_mood_created(self):
        mood = self.my_client.get(f'{self.base_url}api/moods/', headers=self.headers)
        self.assertEqual(mood.status_code, 200)
        self.assertIsInstance(mood.json(), list)
        
        
    def test_get_single_mood_created(self):
        mood = self.my_client.get(f'{self.base_url}api/moods/1/', headers=self.headers)
        self.assertEqual(mood.status_code, 200)
        self.assertEqual(mood.json()['id'], 1)
        self.assertEqual(mood.json()['name'], 'Happy')
        self.assertEqual(mood.json()['_videos'], [])
        

class TestVideoCategory(SetUpTestCase):
    def test_video_category_created(self):
        self.assertEqual(self.category.status_code, 201)
        self.assertEqual(self.category.json()['id'], 1)
        self.assertEqual(self.category.json()['name'], 'Hot Stuff')
        self.assertEqual(self.category.json()['videos'], [])
        
    def test_get_all_video_category(self):
        category = self.my_client.get(f'{self.base_url}api/categories/', headers=self.headers)
        self.assertEqual(category.status_code, 200)
        self.assertIsInstance(category.json(), list)
        
    def test_get_single_video_category(self):
        category = self.my_client.get(f'{self.base_url}api/categories/1/', headers=self.headers)
        self.assertEqual(category.status_code, 200)
        self.assertIsInstance(category.json(), dict)

class TestVideoPlayList(SetUpTestCase):
    def test_video_category_created(self):
        self.assertEqual(self.playlist.status_code, 201)
        # self.assertEqual(self.category.json()['id'], 1)
        # self.assertEqual(self.category.json()['name'], 'Hot Stuff')
        # self.assertEqual(self.category.json()['videos'], [])
        pass


