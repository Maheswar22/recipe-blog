from django.conf.urls import url
from . import views


app_name = 'task'
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'signup', views.signup, name='signup'),
    url(r'recipes_list', views.recipe_list, name='recipes_list'),
    url(r'^(?P<pk>[0-9]+)/delete_recipe/$', views.delete_recipe, name='delete_recipe'),
    url(r'^(?P<pk>[0-9]+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'^create_recipe', views.cerate_recipe, name='create_recipe'),
    url(r'^logout', views.user_logout, name='user_logout'),

]
