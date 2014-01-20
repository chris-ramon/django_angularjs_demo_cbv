from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from demo_app.models import Post


class PostListTestCase(APITestCase):
    def create_posts(self):
        posts = []
        self.first_post = {'title': 'some title', 'body': 'some content'}
        second_post = {'title': 'some title 2', 'body': 'some content 2'}
        posts.append(Post.objects.create(**self.first_post))
        posts.append(Post.objects.create(**second_post))
        return posts

    def test_get(self):
        self.create_posts()
        url = reverse('post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post(self):
        url = reverse('post_list')
        data = {'title': 'some title', 'body': 'some content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

    def test_delete(self):
        self.create_posts()
        url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 1)

    def test_get_one(self):
        posts = self.create_posts()
        url = reverse('post_detail', kwargs={'pk': posts[0].pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.first_post.update({'id': 1})
        self.assertEqual(response.data, self.first_post)

    def test_put(self):
        posts = self.create_posts()
        url = reverse('post_detail', kwargs={'pk': posts[0].pk})
        data = {'title': 'title updated', 'body': 'body updated'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data.update({'id': posts[0].pk})
        self.assertEqual(response.data, data)
