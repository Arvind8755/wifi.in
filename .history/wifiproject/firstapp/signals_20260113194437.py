# firstapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from urllib.parse import quote
import threading
import urllib.request

try:
    from django.contrib.sites.models import Site
    SITES_ENABLED = True
except Exception:
    SITES_ENABLED = False

from .models import Job, Result, Admitcard, Govtupdate 

def _current_domain():
    # Sites framework से domain; वरना settings.SITE_DOMAIN; वरना localhost
    domain = None
    if SITES_ENABLED:
        try:
            domain = Site.objects.get_current().domain
        except Exception:
            domain = None
    if not domain:
        domain = getattr(settings, "SITE_DOMAIN", None)
    if not domain:
        domain = "127.0.0.1:8000"
    return domain


def _sitemap_url():
    protocol = "https" if not getattr(settings, "DEBUG", True) else "http"
    return f"{protocol}://{_current_domain()}/sitemap.xml"


def _fire_and_forget(url: str):
    def _go(u):
        try:
            with urllib.request.urlopen(u, timeout=5):
                pass
        except Exception:
            pass
    threading.Thread(target=_go, args=(url,), daemon=True).start()




def _ping_search_engines():
    sm = _sitemap_url()
    google = f"https://www.google.com/ping?sitemap={quote(sm, safe='')}"
    bing = f"https://www.bing.com/ping?sitemap={quote(sm, safe='')}"
    # 👇 Debug (local verify)
    print("🔍 Pinging Google:", google)
    print("🔍 Pinging Bing:", bing)
    _fire_and_forget(google)
    _fire_and_forget(bing)


def _should_ping():
    # Prod में ही; testing के लिए settings.PING_ALWAYS=True कर सकते हो
    if getattr(settings, "PING_ALWAYS", False):
        return True
    return not getattr(settings, "DEBUG", True)


@receiver(post_save, sender=Job)
@receiver(post_save, sender=Result)
@receiver(post_save, sender=Admitcard)
@receiver(post_save, sender=Govtupdate)
 
def ping_search_engines_on_save(sender, instance, created, **kwargs):
    if not _should_ping():
        return
    if hasattr(instance, "is_active") and not getattr(instance, "is_active"):
        return
    _ping_search_engines()




#newsitemap

from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from datetime import timedelta
from .models import Job, Result, Admitcard, Govtupdate

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
