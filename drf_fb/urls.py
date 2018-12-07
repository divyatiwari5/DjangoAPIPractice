from django.urls import path
from .views import FBView

app_name = "PageMetaTags"

urlpatterns = [
    path('show/', FBView.as_view(), name="tags-all"),
]