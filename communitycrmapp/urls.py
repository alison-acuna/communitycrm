from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^new', views.new, name='new'),
    url(r'^display', views.display, name='display'),
    url(r'^member/(?P<id>\d+)/', views.member_item, name='member'),
    url(r'^searchbyname', views.search_by_name, name='search_by_name'),
    url(r'^results', views.search_by_name, name='results'),
    url(r'^searchpage', views.searchpage, name='searchpage'),
    url(r'^searchbyvolunteer', views.search_by_volunteer, name='search_by_volunteer'),
    url(r'^searchbyhost', views.search_by_host, name='search_by_host'),
    url(r'^searchbyohb', views.search_by_ohb, name='search_by_ohb'),
    url(r'^searchbylt', views.search_by_lt, name='search_by_lt'),
    url(r'^searchbyfb', views.search_by_fb, name='search_by_fb'),
    url(r'^donor_search', views.donor_search, name='donor_search'),
]
