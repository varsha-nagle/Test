from django.urls import path
from .views import RegisterView, LoginView, BookListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('books/', BookListView.as_view(), name='book-list'),

]
