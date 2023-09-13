from django.test import TestCase, Client
from main.models import Item

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name='Chitato', category='Chips', 
                            price=9000, amount=0, 
                            description= '''Made from selected real potatoes thinly sliced, 
                            brings a crunchier sensation in every bite.''')

    def test_data_create_item(self):
        items = Item.objects.all().count()
        self.assertEqual(items, 1)

    def test_name_item_is_correct(self):
        chitato = Item.objects.get(name='Chitato')
        max_length = chitato._meta.get_field('name').max_length
        self.assertLessEqual(len(chitato.name), max_length)

    def test_category_item_is_correct(self):
        chitato = Item.objects.get(name='Chitato')
        max_length = chitato._meta.get_field('category').max_length
        self.assertLessEqual(len(chitato.category), max_length)

    def test_price_item_is_int(self):
        chitato = Item.objects.get(name='Chitato')
        self.assertIsInstance(chitato.price, int)

    def test_amount_item_is_int(self):
        chitato = Item.objects.get(name='Chitato')
        self.assertIsInstance(chitato.amount, int)

    def test_description_item_is_text_field(self):
        chitato = Item.objects.get(name='Chitato')
        self.assertIsInstance(chitato.description, str)
        


    
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    
