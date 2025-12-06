from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from datetime import timedelta
from .models import Job  # आपके news-type model

class NewsSitemap(Sitemap):
    protocol = "https"
    limit = 1000  # Google allows 1000 news URLs

    def items(self):
        last_48_hours = timezone.now() - timedelta(hours=48)
        return Job.objects.filter(published=True, created_at__gte=last_48_hours)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at
