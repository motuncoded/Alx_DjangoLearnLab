from django.urls import path
from .views import list_books
from . import views


path('roles/', include('relationship_app.urls')),
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
    path('books/add/', views.add_book, name='add-book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit-book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete-book'),
]