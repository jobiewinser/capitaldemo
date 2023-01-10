from django.urls import path
import demo.views as demoviews
urlpatterns = [
    path('', demoviews.DemoView.as_view(), name='demo'),     
]
