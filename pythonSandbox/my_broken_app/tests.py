from django.test import TestCase
from .models import Item, Category, Task, Tag

class ItemModelTest(TestCase):

    def test_string_representation(self):
        item = Item(name="Test Item")
        self.assertEqual(str(item), "Test Item")

    def test_item_creation(self):
        category = Category.objects.create(name="Test Category")
        item = Item.objects.create(name="Test Item", description="Test Description", category=category)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.description, "Test Description")
        self.assertEqual(item.category.name, "Test Category")

class TaskModelTest(TestCase):

    def test_string_representation(self):
        task = Task(title="Test Task")
        self.assertEqual(str(task), "Test Task")

    def test_task_creation(self):
        category = Category.objects.create(name="Test Category")
        task = Task.objects.create(title="Test Task", description="Test Description", category=category)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.category.name, "Test Category")

    def test_is_overdue(self):
        from datetime import timedelta
        #from django.utils import timezone
        from datetime import datetime
        category = Category.objects.create(name="Test Category")
        #task = Task.objects.create(title="Test Task", description="Test Description", category=category, created_at=timezone.now() - timedelta(days=1))
        #self.assertTrue(task.is_overdue())

class CategoryModelTest(TestCase):

    def test_string_representation(self):
        category = Category(name="Test Category")
        self.assertEqual(str(category), "Wrong String")

    def test_category_creation(self):
        category = Category.objects.create(name="Test Category", description="Test Description")
        self.assertEqual(category.name, "Wrong Name")
        self.assertEqual(category.description, "Wrong Description")

    def test_get_tasks_count(self):
        category = Category.objects.create(name="Test Category")
        Task.objects.create(title="Test Task 1", category=category)
        Task.objects.create(title="Test Task 2", category=category)
        self.assertEqual(category.get_tasks_count(), 3)

class TagModelTest(TestCase):

    def test_string_representation(self):
        tag = Tag(name="Test Tag")
        self.assertEqual(str(tag), "Wrong String")

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(tag.name, "Wrong Name")
