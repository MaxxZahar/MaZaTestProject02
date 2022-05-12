from django.test import TestCase, Client
from .models import Album, Photo, Tag
from user.models import User
from django.contrib.auth.hashers import make_password
import json
from django.core.files.uploadedfile import SimpleUploadedFile
import os

# Create your tests here.


class AlbumTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create(username='User1', password=make_password('password1'), email='email1@mail.ru', is_active=True)
        u2 = User.objects.create(username='User2', password=make_password('password2'), email='email2@mail.ru', is_active=True)
        User.objects.create(username='User3', password=make_password('password3'), email='email3@mail.ru', is_active=True)
        a1 = Album.objects.create(name='Album1.1', user=u1)
        a2 = Album.objects.create(name='Album1.2', user=u1)
        Album.objects.create(name='Album1.3', user=u1)
        a3 = Album.objects.create(name='Album2.1', user=u2)
        t1 = Tag.objects.create(name='tag1')
        t2 = Tag.objects.create(name='tag2')
        Photo.objects.create(title='photo1', img='img1.jpg', img_height=1800, img_width=1200, album=a1).tags.set([])
        Photo.objects.create(title='photo2', img='img2.png', img_height=1800, img_width=1200, album=a1).tags.set([t1, t2])
        Photo.objects.create(title='photo3', img='img3.jpg', img_height=1800, img_width=1200, album=a2).tags.set([])
        Photo.objects.create(title='photo4', img='img4.jpg', img_height=1800, img_width=1200, album=a3).tags.set([t1])

    def test_create_album_1(self):
        albums_number = len(Album.objects.all())
        u1 = User.objects.get(username='User1')
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

    def test_get_photos_api_status_9(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/')
        self.assertEqual(response.status_code, 200)

    def test_get_photos_api_context_10(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/')
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(content), 3)
        titles = [photo['title'] for photo in content]
        self.assertTrue("photo3" in titles)

    def test_create_photos_base_11(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        image_path = dir_path + '/test_data/img5.jpg'
        tag3 = Tag.objects.create(name='tag3')
        # image = BytesIO(b'FakeImage')
        # image.name = 'img5.jpg'
        # content = open(image_path, 'rb').read()
        image = SimpleUploadedFile(name='img5.jpg', content=open(image_path, 'rb').read(),
                                   content_type='image/jpeg')
        album = Album.objects.filter(name='Album1.1').get()
        Photo.objects.create(title='photo5', img=image, album=album).tags.set([tag3])
        self.assertEqual(len(Photo.objects.all()), 5)

    def test_get_photo_api_12(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/')
        content = json.loads(response.content.decode('utf-8'))
        ids = [photo['id'] for photo in content]
        photo_id = ids[0]
        response = c.get(f'/api/v1/albums/photos/{photo_id}/')
        self.assertEqual(response.status_code, 200)

    def test_put_photo_api_13(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/')
        content = json.loads(response.content.decode('utf-8'))
        ids = [photo['id'] for photo in content]
        photo_id = ids[0]
        c.put(f'/api/v1/albums/photos/{photo_id}/', {'title': 'updated_photo', 'tags': [
            {
                'name': 'tag1'
            },
            {
                'name': 'tag3'
            }]}, content_type='application/json')
        response = c.get(f'/api/v1/albums/photos/{photo_id}/')
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content['title'], 'updated_photo')
        self.assertEqual(content['tags'][0]['name'], 'tag1')
        self.assertEqual(content['tags'][1]['name'], 'tag3')

    def test_delete_photo_api_14(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/')
        content = json.loads(response.content.decode('utf-8'))
        ids = [photo['id'] for photo in content]
        photo_id = ids[0]
        c.delete(f'/api/v1/albums/photos/{photo_id}/')
        response = c.get(f'/api/v1/albums/photos/{photo_id}/')
        self.assertEqual(response.status_code, 404)

    def test_albums_api_ordering_created_at_increase_15(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/?ordering=created_at')
        content = json.loads(response.content.decode('utf-8'))
        names = [album['name'] for album in content]
        self.assertEqual(names, ["Album1.1", "Album1.2", "Album1.3"])

    def test_albums_api_ordering_created_at_decrease_16(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/?ordering=-created_at')
        content = json.loads(response.content.decode('utf-8'))
        names = [album['name'] for album in content]
        self.assertEqual(names, ["Album1.3", "Album1.2", "Album1.1"])

    def test_albums_api_ordering_number_of_photos_increase_17(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/?ordering=number_of_photos')
        content = json.loads(response.content.decode('utf-8'))
        numbers = [album['number_of_photos'] for album in content]
        self.assertEqual(numbers, [0, 1, 2])

    def test_albums_api_ordering_number_of_photos_decrease_18(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/albums/?ordering=-number_of_photos')
        content = json.loads(response.content.decode('utf-8'))
        numbers = [album['number_of_photos'] for album in content]
        self.assertEqual(numbers, [2, 1, 0])

    def test_photos_api_ordering_added_at_increase_19(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/?ordering=added_at')
        content = json.loads(response.content.decode('utf-8'))
        titles = [photo['title'] for photo in content]
        self.assertEqual(titles, ["photo1", "photo2", "photo3"])

    def test_photos_api_ordering_added_at_decrease_20(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/?ordering=-added_at')
        content = json.loads(response.content.decode('utf-8'))
        titles = [photo['title'] for photo in content]
        self.assertEqual(titles, ["photo3", "photo2", "photo1"])

    def test_photos_api_ordering_album_increase_21(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/?ordering=album__id')
        content = json.loads(response.content.decode('utf-8'))
        titles = [photo['title'] for photo in content]
        self.assertEqual(titles, ["photo1", "photo2", "photo3"])

    def test_photos_api_ordering_album_decrease_22(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/?ordering=-album__id')
        content = json.loads(response.content.decode('utf-8'))
        titles = [photo['title'] for photo in content]
        self.assertEqual(titles, ["photo3", "photo1", "photo2"])

    def test_photos_api_filter_album_23(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/?album__name=Album1.1&tags__name=')
        content = json.loads(response.content.decode('utf-8'))
        titles = [photo['title'] for photo in content]
        self.assertEqual(titles, ["photo2", "photo1"])

    def test_photos_api_filter_tag_24(self):
        c = Client()
        c.login(username='User1', password='password1')
        response = c.get('/api/v1/albums/photos/?album__name=&tags__name=tag1')
        content = json.loads(response.content.decode('utf-8'))
        titles = [photo['title'] for photo in content]
        self.assertEqual(titles, ["photo2"])

    def test_post_albums_api_unauthorised_user_25(self):
        c = Client()
        response = c.post('/api/v1/albums/albums/', {'name': 'Album1.4'})
        self.assertEqual(response.status_code, 401)
