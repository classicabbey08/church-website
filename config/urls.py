from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name="home"
    ),

    path(
        "about/",
        TemplateView.as_view(template_name="about.html"),
        name="about"
    ),

    path("gallery/", 
         TemplateView.as_view(template_name="gallery.html"), 
         name="gallery"),

    path("leadership/", 
         TemplateView.as_view(template_name="leadership.html"), 
         name="leadership"),

    path("events/",
          TemplateView.as_view(template_name="events.html"), 
          name="events"),

    path("donate/",
          TemplateView.as_view(template_name="donate.html"),
            name="donate"),

    path("contact/", 
         TemplateView.as_view(template_name="contact.html"),
           name="contact"),
]