from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task
import json

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.task = Task.objects.create(title='Test Task', user=self.user)

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {'title': 'New Task', 'priority': 'H' }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        response = self.client.patch(f'/api/tasks/{self.task.id}/', {'completed': True}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()["completed"])

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)