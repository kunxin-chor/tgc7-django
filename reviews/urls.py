from django.contrib import admin
from django.urls import path, include
import reviews.views

urlpatterns = [
    path('', reviews.views.index),
    path('create/<book_id>', reviews.views.create_review,
         name="create_review_route"),
    path('create/comment/<review_id>', reviews.views.create_comment,
         name='create_comment_route')
]
