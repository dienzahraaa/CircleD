from django.test import TestCase, Client
from main.models import Item

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name='KitKat', category='Chocolate', 
                            price=15000, amount=24, 
                            description= '''The perfect balance of chocolate and wafer. 
                            From classic fingers to chunky, original to peanut butter, 
                            there is a KitKat for everyone.''')
        Item.objects.create(name='Chitato', category='Chips', 
                            price=9000, amount=0, 
                            description= '''Made from selected real potatoes thinly sliced, 
                            brings a crunchier sensation in every bite.''')
        
    def test_create_product(self):
        
    def test_product_is_available(self):

        assertEquals("DEK-082212345678-75", NotaGenerator.generateId("Dek Depe", "082212345678"));

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    