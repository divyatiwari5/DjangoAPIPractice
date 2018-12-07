from rest_framework import generics, filters


# Create your views here.

class FBView(generics.ListAPIView):
    """
    Provide details of searched/filtered tags
    """
    from .models import FBUserRequest
    from .serializer import FBSerializer

    queryset = FBUserRequest.objects.all()
    serializer_class =  FBSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('email', 'date_joined', 'first_name', 'phone', 'fb_id', 'profile_pic', 'gender')