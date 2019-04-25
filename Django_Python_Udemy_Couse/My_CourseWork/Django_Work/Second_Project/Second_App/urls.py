from django.conf.urls import url
from Second_App import views

urlpatterns=[
    url(r'^$',views.help,name="help"),
    # url(r'help/',views.help,name="help"),
]
