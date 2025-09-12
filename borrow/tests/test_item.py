from django.test import TestCase
from ..models import Item
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError

class ItemTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.owner = User.objects.create_user(
            username = "TestUser1", 
            password= "abc123"
            )
        
        cls.borrower = User.objects.create_user(
                username = "TestUser2",
                password= "abc123"
            )

        cls.item = Item.objects.create(
            item_name ="Item1",
            owner = cls.owner,
            description = "This is a test item.",
            borrower = cls.borrower,
            date_borrowed = date(2025,9,11),
            due_date = date(2025,9,17),
            status ="Available"
        )
        
    def test_instance_creation(self):
        self.assertEqual(self.item.item_name, "Item1")
        self.assertEqual(self.item.owner.username, "TestUser1")
        self.assertEqual(self.item.description,"This is a test item." )

        self.assertEqual(self.item.date_borrowed, date(2025,9,11))
        self.assertEqual(self.item.due_date, date(2025,9,17))
        self.assertEqual(self.item.status, "Available")

        self.assertEqual(self.item.borrower.username, "TestUser2")
        self.assertIsNotNone(self.item.created_at)
        self.assertIsNotNone(self.item.item_id)

    def test_required_fields(self):
        minimal_item = Item.objects.create(
                owner = self.owner,
                description ="test description",
                item_name = "Test Item"
            )
        self.assertEqual(minimal_item.owner, self.owner)
        self.assertEqual(minimal_item.description, "test description")
        self.assertEqual(minimal_item.item_name, "Test Item")
        self.assertIsNone(minimal_item.borrower)
        self.assertIsNone(minimal_item.due_date)
        self.assertIsNone(minimal_item.date_borrowed)
        self.assertIsNotNone(minimal_item.created_at)
        self.assertIsNotNone(minimal_item.item_id)

    

        