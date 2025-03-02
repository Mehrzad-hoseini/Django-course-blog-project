from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import reverse
# Create your tests here.

class BlogPost(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        cls.user = User.objects.create(username='test')
        cls.post = Post.objects.create(
            title='Test Post',
            text='Test Post 123456',
            author=cls.user,
            status=Post.STATUS_CHOICES[0][0]
        )

        cls.post1 = Post.objects.create(
            title='Test Post 999',
            text='Test Post 12345678',
            author=cls.user,
            status=Post.STATUS_CHOICES[1][0]
        )

    def test_str_model(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_detail_detail(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_title_contain(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_contain(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)

    def test_post_detail_not_exist_404(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id + 10]))
        self.assertEqual(response.status_code, 404)

    def test_post_draft_not_contain(self):
        response = self.client.get(reverse('post_list'))
        self.assertNotContains(response, self.post1.title)
        self.assertContains(response, self.post.title)

    def test_create_post(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'Test Post 274',
            'text': 'Test Post 275',
            'author': self.user.id,
            'status': 'pub'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Test Post 274')
        self.assertEqual(Post.objects.last().text, 'Test Post 275')

    def test_update_post(self):
        response = self.client.post(reverse('post_update', args=[self.post.id]), {
            'title': 'Test Post 279',
            'text': 'Test Post 280',
            'author': self.user.id,
            'status': 'pub'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.first().title, 'Test Post 279')
        self.assertEqual(Post.objects.first().text, 'Test Post 280')

    def test_delete_post(self):
        response = self.client.post(reverse('post_delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)






