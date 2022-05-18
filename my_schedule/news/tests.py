from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import News


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser',email='test@email.com',password='test')
        self.post = News.objects.create(title='My news',body='Nice body content',author=self.user,date='2022-05-17')

    def test_news_list_view(self):
        response = self.client.get(reverse('main_news'))
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'news/news_main.html')

    def test_news_detail_view(self):
        response = self.client.get('/news/2/')
        no_response = self.client.get('/news/10000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'My news')
        self.assertTemplateUsed(response, 'news/news_detail.html')

    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(), '/news/1/')

    def test_post_create_view(self):
        response = self.client.post(reverse('news_create'),
        {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
            'date': '2022-05-18'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('news_edit', args='4'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(reverse('news_delete', args='5'))
        print(response)
        self.assertEqual(response.status_code, 200)