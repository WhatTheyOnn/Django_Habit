from django.test import TestCase
from .models import Habit
from django.utils import timezone

# Create your tests here.
class habitmodeltest(TestCase):
    def setUp(self):
        self.habit = Habit.objects.create(
            title = "Test Habit"
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
