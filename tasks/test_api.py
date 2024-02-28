from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Task, Group

# Import test from rest_frame
from rest_framework.test import APIRequestFactory

User = get_user_model()

class TaskViewSetTestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(email='testuser@mail.com', password='testpassword123')
        # Log in the user
        self.client.login(username='testuser@mail.com', password='testpassword123')
        # Create a Group for the Task
        self.group = Group.objects.create(name="Test Group")
        # Create a Task
        self.task = Task.objects.create(name="Test Task", completed=False, group=self.group)

    def test_get_tasks(self):
        # Get the list of tasks
        url = reverse('task-list')  # Assumes you have set up 'task-list' as the URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(len(response.data), 1)  # Assuming pagination is not enabled

    def test_create_task(self):
        # Create a task
        url = reverse('task-list')  # Assumes you have set up 'task-list' as the URL name
        data = {'name': 'New Task', 'completed': False, 'group': self.group.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # There should now be 2 tasks

    def test_access_authenticated(self):
        """
        Ensure authenticated users can access the endpoint.
        """
        # Use the reverse function to dynamically fetch the URL
        url = reverse('task-list')  # Adjust 'task-list' to match your URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_unauthenticated(self):
        """
        Ensure unauthenticated users cannot access the endpoint.
        """
        # Clear any authentication credentials
        self.client.logout()
        
        url = reverse('task-list')  # Adjust 'task-list' to match your URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Or HTTP_401_UNAUTHORIZED, depending on your authentication setup

class GroupViewSetTestCase(APITestCase):
    def setUp(self):
        # Create and log in the user
        self.user = User.objects.create_user(email='testuser@mail.com', password='testpassword123')
        self.client.login(username='testuser@mail.com', password='testpassword123')
        # Create a Group
        self.group = Group.objects.create(name="Test Group")

    def test_get_groups(self):
        # Get the list of groups
        url = reverse('group-list')  # Assumes you have set up 'group-list' as the URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(len(response.data), 1)  # Assuming pagination is not enabled

    def test_create_group(self):
        # Create a group
        url = reverse('group-list')  # Assumes you have set up 'group-list' as the URL name
        data = {'name': 'New Group'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.count(), 2)  # There should now be 2 groups
