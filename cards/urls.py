# 'cards' app takes care of all URLs in the project except from the /admin path, so an urls.py file is added to takes care of dispatching the URLs. 

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="cards/base.html"),
        name="home"
    ),
]