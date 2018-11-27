from django.urls import path
from .views import MetaTagView

app_name = "PageMetaTags"

urlpatterns = [
    path('show/', MetaTagView.as_view(), name="tags-all"),
]