from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Video
from .forms import VideoForm
from django.conf import settings


class VideosListView(ListView):
    model = Video
    template_name = 'videos/videos_home.html'  # Your template to list posts
    context_object_name = 'videos'
    ordering = ['-date_posted']

    # def get_queryset(self):
    #     # Return only published posts
    #     return Video.objects.filter(published=True).order_by('-created_at')


class AdminVideoCreateView(UserPassesTestMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'videos/video_form.html'  # Your template to create new posts
    success_url = reverse_lazy('videos-home')  # Redirect to the list after creating a post

    def form_valid(self, form):
        # form.instance.published = True  # Automatically mark post as published
        return super().form_valid(form)

    # # Restrict access to the admin only (you can check against the admin username)
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.username == 'settings.ADMIN_USERNAME'  # Replace with your actual username


# add check that if theres is no video then dont display, then add a console log