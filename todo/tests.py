from django.test import TestCase
from .models import Task
from django.urls import reverse
from .views import *

# Create your tests here.

# model string test


class TaskTest(TestCase):
    def test_string(self):
        title = Task(title="Delivery")
        self.assertEqual(str(title), title.title)

# view test


class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

# form test


class TaskFormTest(TestCase):
    def test_form_is_valid(self):
        form = TaskForm(data={'title': "Delivery"})
        self.assertTrue(form.is_valid())
