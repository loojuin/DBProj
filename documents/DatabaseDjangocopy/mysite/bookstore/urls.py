from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_books, name='index'),
    url(r'^(?P<book_id>d+)/$', views.book, name='book'),

]
