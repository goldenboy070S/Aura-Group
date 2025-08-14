from django.urls import path
from .views import (
    IndexView,
    AboutView,
    ServicesView,
    ServicesDetailsView,
    BlogView,
    BlogDetailsView,
    service_request_view,
    ProjectView,
    ProjectDetailsView,
    contact_view,
    LikeProjectView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('services_details/<int:pk>/', ServicesDetailsView.as_view(), name='services_details'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailsView.as_view(), name='blog_detail'),
    path('projects/', ProjectView.as_view(), name='project'),
    path('projects/<int:pk>/', ProjectDetailsView.as_view(), name='project_details'),
    path('projects/<int:pk>/like/', LikeProjectView.as_view(), name='like_project'),
    path('contact/', contact_view, name='contact'),
    path('services/request/', service_request_view, name='services_request'),
]
