from django.urls import path
from main.views import decrease_item_amount, increase_item_amount, remove_item
from main.views import show_main, create_product
from main.views import show_main, create_product, show_xml 
from main.views import show_main, create_product, show_xml, show_json
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, delete_item_ajax
from main.views import register 
from main.views import login_user
from main.views import logout_user, get_product_json, add_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('remove_item_amount/<int:id>/', remove_item, name='remove_item'),
    path('increase_item_amount/<int:id>/', increase_item_amount, name='increase_item_amount'),
    path('decrease_item_amount/<int:id>/', decrease_item_amount, name='decrease_item_amount'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax')
]