from django.contrib import admin
from django.urls import path, include
import reviews.views

urlpatterns = [
    path('', reviews.views.index),
    path('create', reviews.views.create_review),
]