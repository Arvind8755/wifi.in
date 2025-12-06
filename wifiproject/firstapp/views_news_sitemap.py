# firstapp/views_news_sitemap.py

from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from xml.etree.ElementTree import Element, SubElement, tostring
from django.utils.encoding import iri_to_uri

from firstapp.models import Job, Admitcard, Result, Govtupdate, Notification

SITE_NAME = "WifiResult.com"
SITE_DOMAIN = "https://wifiresult.com"
NEWS_LANGUAGE = "en"  # or "hi"


def get_recent_news_items():
    """Fetch news published within last 48 hours using published_date field."""
    since = timezone.now() - timedelta(hours=48)
    items = []

    models = [Job, Admitcard, Result, Govtupdate, Notification]

    for model in models:
        if hasattr(model, "published_date"):
            qs = model.objects.filter(published_date__gte=since)
        else:
            continue

        for obj in qs:
            if hasattr(obj, "get_absolute_url"):
                items.append(obj)

    # latest first
    return sorted(items, key=lambda x: x.published_date, reverse=True)[:1000]


def news_sitemap(request):
    NS_NEWS = "http://www.google.com/schemas/sitemap-news/0.9"

    urlset = Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xmlns:news": NS_NEWS,
    })

    items = get_recent_news_items()

    for obj in items:

        # URL build
        loc_url = obj.get_absolute_url()
        if not loc_url.startswith("http"):
            loc_url = SITE_DOMAIN.rstrip("/") + "/" + loc_url.lstrip("/")
        loc_url = iri_to_uri(loc_url)

        # <url>
        url_el = SubElement(urlset, "url")
        loc_el = SubElement(url_el, "loc")
        loc_el.text = loc_url

        # <news:news>
        news_el = SubElement(url_el, f"{{{NS_NEWS}}}news")

        # <news:publication>
        pub_el = SubElement(news_el, f"{{{NS_NEWS}}}publication")

        name_el = SubElement(pub_el, f"{{{NS_NEWS}}}name")
        name_el.text = SITE_NAME

        lang_el = SubElement(pub_el, f"{{{NS_NEWS}}}language")
        lang_el.text = NEWS_LANGUAGE

        # <news:publication_date>
        pub_date_el = SubElement(news_el, f"{{{NS_NEWS}}}publication_date")
        pub_date_el.text = obj.published_date.isoformat()

        # <news:title>
        title_el = SubElement(news_el, f"{{{NS_NEWS}}}title")
        title_el.text = getattr(obj, "title", "Untitled Article")

    xml_output = tostring(urlset, encoding="utf-8", method="xml")
    return HttpResponse(xml_output, content_type="application/xml")