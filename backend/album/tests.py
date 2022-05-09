from django.test import TestCase, Client
from .models import Album, Photo, Tag
from user.models import User
from django.contrib.auth.hashers import make_password
import json

# Create your tests here.


class AlbumTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create(username='User1', password=make_password('password1'), email='email1@mail.ru', is_active=True)
        u2 = User.objects.create(username='User2', password=make_password('password2'), email='email2@mail.ru', is_active=True)
        User.objects.create(username='User3', password=make_password('password3'), email='email3@mail.ru', is_active=True)
        Album.objects.create(name='Album1.1', user=u1)
        Album.objects.create(name='Album1.2', user=u1)
        Album.objects.create(name='Album1.3', user=u1)
        Album.objects.create(name='Album2.1', user=u2)

    def test_create_album_1(self):
        albums_number = len(Album.objects.all())
        u1 = User.objects.get(id=1)
        Album.objects.create(name='Album', user=u1)
        self.assertEqual(len(Album.objects.all()), albums_number + 1)

    def test_user_login_2(self):
        c = Client()
        response = c.post('/api-auth/login/', {'username': 'User1', 'password': 'password1'})
        self.assertEqual(response.status_code, 302)

    def test_get_albums_api_status_3(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/')
        self.assertEqual(response.status_code, 200)

    def test_get_albums_api_context_4(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/')
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(content), 3)
        names = [album['name'] for album in content]
        self.assertTrue("Album1.3" in names)

    def test_post_albums_api_5(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.post('/api/v1/albums/albums/', {'name': 'Album1.4'})
        self.assertEqual(response.status_code, 201)

    def test_get_album_api_6(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/')
        content = json.loads(response.content.decode('utf-8'))
        ids = [album['id'] for album in content]
        album_id = ids[0]
        response = c.get(f'/api/v1/albums/albums/{album_id}/')
        self.assertEqual(response.status_code, 200)

    def test_put_album_api_7(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/')
        content = json.loads(response.content.decode('utf-8'))
        ids = [album['id'] for album in content]
        album_id = ids[0]
        c.put(f'/api/v1/albums/albums/{album_id}/', {'name': 'Album1.4'}, content_type='application/json')
        response = c.get(f'/api/v1/albums/albums/{album_id}/')
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content['name'], 'Album1.4')

    def test_delete_album_api_8(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/')
        content = json.loads(response.content.decode('utf-8'))
        ids = [album['id'] for album in content]
        album_id = ids[0]
        c.delete(f'/api/v1/albums/albums/{album_id}/')
        response = c.get(f'/api/v1/albums/albums/{album_id}/')
        self.assertEqual(response.status_code, 404)



