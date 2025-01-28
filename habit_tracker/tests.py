from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Habit
from django.utils import timezone

# Create your tests here.
class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.habit = Habit.objects.create(
            title="Test Habit",
            user=self.user
        )

    def test_habit_creation(self):
        self.assertIsInstance(self.habit, Habit)
        self.assertEqual(self.habit.title, "Test Habit")

    def test_habit_str(self):
        self.assertEqual(str(self.habit), "Test Habit")

    def test_habit_default_values(self):
        self.assertFalse(self.habit.completed)
        self.assertIsNotNone(self.habit.created)
        self.assertLessEqual(self.habit.created, timezone.now())

class HabitPermissionTest(TestCase):
    def setUp(self):
        
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

        
        self.habit1 = Habit.objects.create(title='Habit 1', user=self.user1)

    def test_user_cannot_edit_another_users_habit(self):
        
        self.client.login(username='user2', password='password2')

        
        response = self.client.post(reverse('habit_update', args=[self.habit1.id]), {
            'title': 'Updated Habit',
            'completed': False,
            'high_priority': False,
        })

        
        self.habit1.refresh_from_db()
        self.assertEqual(self.habit1.title, 'Habit 1')

       
        self.assertEqual(response.status_code, 403)

    def test_user_cannot_delete_another_users_habit(self):
       
        self.client.login(username='user2', password='password2')

        response = self.client.post(reverse('delete', args=[self.habit1.id]))

        
        self.assertTrue(Habit.objects.filter(id=self.habit1.id).exists())

        
        self.assertEqual(response.status_code, 403)