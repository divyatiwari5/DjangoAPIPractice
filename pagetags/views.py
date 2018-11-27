from rest_framework import generics, filters


# Create your views here.

class MetaTagView(generics.ListAPIView):
    """
    Provide details of searched/filtered tags
    """
    from .models import pagetagModel
    from .serializers import PageTagSerializer

    queryset = pagetagModel.objects.all()
    serializer_class =  PageTagSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'mdesc', 'mkeyword', 'mschema', 'mimage')