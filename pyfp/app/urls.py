from . import views
from django.urls import path

urlpatterns = [
			path('',views.index),
			path('edit_user/<int:user_id>',views.edit_user),
			path('save_usr',views.save_usr),
			path('edit_usr/<int:user_id>',views.edit_usr),
			path('delete_usr/<int:user_id>',views.delete_usr),
]