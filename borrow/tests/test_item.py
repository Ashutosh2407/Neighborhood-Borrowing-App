from django.test import TestCase
from ..models import Item
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.core.exceptions import ValidationError
from django.db import transaction,IntegrityError

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
        
    #Item Creation
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

    #Test Item creation with only required fields
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

    #Database Constraints Check
    def test_check_database_constraints_missing_owner(self):
        with self.assertRaises(IntegrityError):
            item = Item.objects.create(
                #Missing Owner
                description ="test description",
                item_name = "Test Item"
            )
    
    #Field Validation Tests
    def test_max_item_name_length(self):
        with self.assertRaises(ValidationError):
            item = Item.objects.create(
                item_name = "a"*51,
                owner = self.owner,
                description = "Test description"
            )
            item.full_clean()

    def test_max_description_length(self):
        with self.assertRaises(ValidationError):
            item = Item.objects.create(
                owner = self.owner,
                description = "a"*201,
                item_name = "Test name"
            )
            item.full_clean()

    def test_status_choices(self):
        valid_statuses = ["Available","Requested","Borrowed","Overdue","Returned"]

        for status_ in valid_statuses:
            item = Item.objects.create(
                owner = self.owner,
                description = "Test Description",
                item_name = "Test name",
                status = status_
            )
            item.full_clean()
    

        with self.assertRaises(ValidationError):
            item = Item.objects.create(
                owner = self.owner,
                description = "Test Description",
                item_name = "Test name",
                status = "Invalid Status"
            )
            item.full_clean()

    #Relationship Tests
    def test_owner_relationship(self):
        self.assertEqual(self.item.owner,self.owner)

    def test_reverse_owner_relationship(self):
        self.assertIn(self.item, self.owner.owner.all())

    def test_borrower_relationship(self):
        self.assertEqual(self.item.borrower, self.borrower)

    def test_reverse_borrower_relationship(self):
        self.assertIn(self.item, self.borrower.borrower.all())

    def test_cascade_delete_owner(self):
        item_id = self.item.item_id
        self.owner.delete()

        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(item_id = item_id)

    #Str representation
    def test_string_rep(self):
        self.assertEquals(str(self.item),"Item1")

    #STATUS AND BUSINESS LOGIC TESTS
    def test_default_status(self):
        item = Item.objects.create(
            item_name = "Default item",
            description ="Default description",
            owner = self.owner
        )
        self.assertEqual(item.status, "Available")

    #Test Borrowing Workflow
    def test_borrowing_flow(self):
        item = Item.objects.create(
            item_name = "Default item",
            description ="Default description",
            owner = self.owner
        )

        #Borrow process
        item.borrower = self.borrower
        item.date_borrowed = date.today()
        item.status = "Borrowed"
        item.due_date = date.today() + timedelta(days=7)
        item.save()

        #Test
        self.assertEqual(item.borrower, self.borrower)
        self.assertEqual(item.status, "Borrowed")
        self.assertIsNotNone(item.due_date)
        self.assertIsNotNone(item.date_borrowed)

    #Test Return Workflow
    def test_return_workflow(self):
        borrowed_item = Item.objects.create(
            item_name = "Borrowed item",
            description ="Borrowed description",
            owner = self.owner,
            borrower = self.borrower,
            date_borrowed = date.today(),
            due_date = date.today() + timedelta(days=7),
            status = "Borrowed"

        )

        #Return Process
        borrowed_item.status = "Returned"
        borrowed_item.date_borrowed = None
        borrowed_item.due_date = None
        borrowed_item.borrower = None
        borrowed_item.save()

        #Test
        self.assertEqual(borrowed_item.status, "Returned")
        self.assertIsNone(borrowed_item.borrower)
        self.assertIsNone(borrowed_item.due_date)
        self.assertIsNone(borrowed_item.date_borrowed)

        #Edge Case User borrowing own item
        def test_same_user_owner_and_borrower(self):
            borrow_item = Item.objects.create(
                item_name="Self Borrow",
                owner=self.owner,
                borrower=self.owner,  # Same user!
                description="User borrowing own item",
                status="Borrowed"
            )
            self.assertEqual(borrow_item.owner, borrow_item.borrower)

        #Items with same name
        def test_items_with_same_name(self):
            item1 = Item.objects.create(
                item_name ="Item1",
                owner = self.owner,
                description = "This is a test item."
            )

            items_named_item1 = Item.objects.filter(item_name = "Item1")
            self.assertEqual(items_named_item1.count(),2)

        def test_date_field_handling(self):
        #Test date field behavior
            today = date.today()
            future_date = today + timedelta(days=7)
            
            item = Item.objects.create(
                item_name="Date Test Item",
                owner=self.owner,
                description="Testing dates",
                date_borrowed=today,
                due_date=future_date,
                status="Borrowed"
            )
            
            self.assertEqual(item.date_borrowed, today)
            self.assertEqual(item.due_date, future_date)
            self.assertIsInstance(item.date_borrowed, date)
            self.assertIsInstance(item.due_date, date)







