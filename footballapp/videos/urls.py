from django.urls import path
from .views import VideosListView, AdminVideoCreateView

urlpatterns = [
    path('', VideosListView.as_view(), name='videos-home'),  # Public view for listing posts
    path('create/', AdminVideoCreateView.as_view(), name='videos-create'),
    # path('embed-tweet/', EmbedTweetView.as_view(), name='embed-tweet')
]
