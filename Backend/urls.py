from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('shoppage/', views.shoppage, name="shoppage"),
    path('display_shop/', views.display_shop, name="display_shop"),
    path('save_shop/', views.save_shop, name="save_shop"),
    path('edit_shop/<int:shop_id>/', views.edit_shop, name="edit_shop"),
    path('update_shop/<int:shop_id>/', views.update_shop, name="update_shop"),
    path('delete_shop/<int:shop_id>/', views.delete_shop, name="delete_shop"),
    path('foodpage/', views.foodpage, name="foodpage"),
    path('display_food/', views.display_food, name="display_food"),
    path('save_food/', views.save_food, name="save_food"),
    path('edit_food/<int:food_id>/', views.edit_food, name="edit_food"),
    path('update_food/<int:food_id>/', views.update_food, name="update_food"),
    path('delete_food/<int:food_id>/', views.delete_food, name="delete_food"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_page/', views.admin_page, name="admin_page"),
]