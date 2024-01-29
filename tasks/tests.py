from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        # Create a user and get JWT token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.token = self.get_token()

        # Create a task for testing
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date='2022-02-28',
            status='Pending',
            owner=self.user
        )

    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_list_tasks(self):
        url = '/api/tasks/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_task(self):
        url = f'/api/tasks/{self.task.id}/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = '/api/tasks/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {
            "title": "New Task",
            "description": "New Description",
            "due_date": "2022-03-15",
            "status": "In Progress"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        url = f'/api/tasks/{self.task.id}/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {
            "title": "Updated Task",
            "description": "Updated Description",
            "due_date": "2022-03-15",
            "status": "In Progress"
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_task(self):
        url = f'/api/tasks/{self.task.id}/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
