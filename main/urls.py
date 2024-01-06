from django.urls import path
from .views import *

urlpatterns = [
    # Choose CRUD
    path('create/Choose',create_Choose),
    path('update/Choose',update_Choose),
    path('delete/Choose',delete_Choose),
    path('get/Choose',get_Choose),

    #Choose_enjoy CRUD
    path('create/Choose_enjoy',create_Choose_enjoy),
    path('update/Choose_enjoy',update_Choose_enjoy),
    path('delete/Choose_enjoy',delete_Choose_enjoy),
    path('get/Choose_enjoy',get_Choose_enjoy),

    #gallery CRUD
    path('create/gallery',create_gallery),
    path('update/gallery',update_gallery),
    path('delete/gallery',delete_gallery),
    path('get/gallery',get_gallery),

    #order CRUD
    path('create/order',create_order),
    path('update/order',update_order),
    path('delete/order',delete_order),
    path('get/order',get_order),
]