from django.urls import path
from .views import list_books, add_book, edit_book, delete_book, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('books/', list_books, name='list-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('admin/', views.admin_view, name='admin-view'),
    path('librarian/', views.librarian_view, name='librarian-view'),
    path('member/', views.member_view, name='member-view'),
    # ... other URL patterns ...

    # Add, edit, and delete book URLs
  path('add_book/', add_book, name='add-book'),
    path('edit_book/<int:pk>/', edit_book, name='edit-book'),
    path('books/<int:pk>/delete/', delete_book, name='delete-book'),
]
#