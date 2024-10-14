import requests
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Video
from .forms import VideoForm


class EmbedTweetMixin:
    """Mixin to fetch embedded HTML for a tweet using Twitter's oEmbed API."""

    def get_embed_html(self, tweet_url):
        """Fetches the embed HTML for the specified tweet URL."""
        maxwidth = 560
        oembed_url = f"https://publish.twitter.com/oembed?url={tweet_url}&maxwidth={maxwidth}"
        response = requests.get(oembed_url)
        if response.status_code == 200:
            embed_html = response.json().get('html')
            return embed_html.replace(
                '<blockquote ', f'<blockquote class="twitter-tweet" data-media-max-width="{maxwidth}" ')
        return None


class VideosListView(EmbedTweetMixin, ListView):
    """View to list videos with embedded tweets."""
    model = Video
    template_name = 'videos/videos_home.html'
    context_object_name = 'videos'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        """Adds embedded tweet HTML to the context."""
        context = super().get_context_data(**kwargs)
        context['embed_html_list'] = [self.get_embed_html(
            video.url) for video in self.get_queryset()]
        return context


class AdminVideoCreateView(UserPassesTestMixin, CreateView):
    """View for creating new video objects, accessible only to certain users."""
    model = Video
    form_class = VideoForm
    template_name = 'videos/video_form.html'
    success_url = reverse_lazy('videos-home')

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.username == 'tomiakinrinmade'


# add check that if theres is no video then dont display, then add a console log
# then have a filtring bit on feutrd page or dont, links to players and then their stats, can you auto load players from a database and also auto createh mmm
# need thumbnail for videosso an image field as well needs tro be added, search how tos ave htis ie naming convention, this should be high quality , can also use youtube and ither stuff too
# links will to be other pages that have stats too and ither stuff
# allow them to view stats from the video
# links to the players so rare futbin and the likes
