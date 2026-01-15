# firstapp/views_news_sitemap.py

from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from xml.etree.ElementTree import Element, SubElement, tostring
from django.utils.encoding import iri_to_uri

from firstapp.models import Job, Admitcard, Result, Govtupdate 

SITE_NAME = "WifiResult.in"
SITE_DOMAIN = "https://wifiresult.com"
NEWS_LANGUAGE = "en"  # or "hi"


def _published_qs(Model):
    """
    Return a queryset that contains only published items for the given Model.
    Probes common patterns:
      - status == 'published'
      - published == True
      - is_published == True
      - draft == False
    Fallback: exclude common draft-like status values if 'status' exists.
    Final fallback: return all() (change to .none() if you prefer).
    """
    qs = Model.objects.all()
    field_names = {f.name for f in Model._meta.get_fields()}

    try:
        if "status" in field_names:
            # Prefer explicit published status if present
            # (case-insensitive match)
            published_qs = qs.filter(status__iexact="published")
            if published_qs.exists():
                return published_qs
    except Exception:
        pass

    try:
        if "published" in field_names:
            return qs.filter(published=True)
    except Exception:
        pass

    try:
        if "is_published" in field_names:
            return qs.filter(is_published=True)
    except Exception:
        pass

    try:
        if "draft" in field_names:
            # models that use draft=True for unpublished
            return qs.filter(draft=False)
    except Exception:
        pass

    # If status exists but values differ, at least exclude common draft-like values
    try:
        if "status" in field_names:
            return qs.exclude(status__in=["draft", "pending", "private", "hidden"])
    except Exception:
        pass

    # Final fallback: include all (change to qs.none() if you want to be stricter)
    return qs


def get_recent_news_items():
    """Fetch news published within last 48 hours using published_date field AND published flags."""
    since = timezone.now() - timedelta(hours=48)
    items = []
    models = [Job, Admitcard, Result, Govtupdate, Notification]

    for model in models:
        # ensure model has published_date field
        field_names = {f.name for f in model._meta.get_fields()}
        if "published_date" not in field_names:
            continue

        # get candidate queryset filtered by published_date range
        try:
            base_qs = _published_qs(model)
            qs = base_qs.filter(published_date__gte=since)
        except Exception:
            # fallback: try naive filter
            try:
                qs = model.objects.filter(published_date__gte=since)
            except Exception:
                continue

        # only include objects with get_absolute_url
        for obj in qs:
            if hasattr(obj, "get_absolute_url"):
                # Sanity: if object has explicit draft flag that was missed, skip it
                # (double-check common flags on instance)
                if getattr(obj, "is_published", None) is False:
                    continue
                if getattr(obj, "published", None) is False:
                    continue
                if getattr(obj, "draft", None) is True:
                    continue
                # if status present and not published-like, skip
                st = getattr(obj, "status", None)
                if st and str(st).lower() not in ("published", "live", "public"):
                    # allow 'live' or 'public' as published synonyms
                    continue

                items.append(obj)

    # latest first and cap at 1000
    items = sorted(items, key=lambda x: getattr(x, "published_date", timezone.now()), reverse=True)
    return items[:1000]


def news_sitemap(request):
    NS_NEWS = "http://www.google.com/schemas/sitemap-news/0.9"

    urlset = Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xmlns:news": NS_NEWS,
    })

    items = get_recent_news_items()

    for obj in items:
        # build absolute URL
        try:
            loc_url = obj.get_absolute_url()
        except Exception:
            continue

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
        pub_date = getattr(obj, "published_date", None)
        if pub_date:
            pub_date_el.text = pub_date.isoformat()
        else:
            # skip if no published_date
            continue

        # <news:title>
        title_el = SubElement(news_el, f"{{{NS_NEWS}}}title")
        title_text = getattr(obj, "title", None) or getattr(obj, "headline", None) or getattr(obj, "name", None) or "Untitled Article"
        title_el.text = title_text

    xml_output = tostring(urlset, encoding="utf-8", method="xml")
    return HttpResponse(xml_output, content_type="application/xml")











#  # firstapp/views_news_sitemap.py

# from django.http import HttpResponse
# from django.utils import timezone
# from datetime import timedelta
# from xml.etree.ElementTree import Element, SubElement, tostring
# from django.utils.encoding import iri_to_uri

# from firstapp.models import Job, Admitcard, Result, Govtupdate, Notification

# SITE_NAME = "WifiResult.com"
# SITE_DOMAIN = "https://wifiresult.com"
# NEWS_LANGUAGE = "en"  # or "hi"


# def get_recent_news_items():
#     """Fetch news published within last 48 hours using published_date field."""
#     since = timezone.now() - timedelta(hours=48)
#     items = []

#     models = [Job, Admitcard, Result, Govtupdate, Notification]

#     for model in models:
#         if hasattr(model, "published_date"):
#             qs = model.objects.filter(published_date__gte=since)
#         else:
#             continue

#         for obj in qs:
#             if hasattr(obj, "get_absolute_url"):
#                 items.append(obj)

#     # latest first
#     return sorted(items, key=lambda x: x.published_date, reverse=True)[:1000]


# def news_sitemap(request):
#     NS_NEWS = "http://www.google.com/schemas/sitemap-news/0.9"

#     urlset = Element("urlset", {
#         "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
#         "xmlns:news": NS_NEWS,
#     })

#     items = get_recent_news_items()

#     for obj in items:

#         # URL build
#         loc_url = obj.get_absolute_url()
#         if not loc_url.startswith("http"):
#             loc_url = SITE_DOMAIN.rstrip("/") + "/" + loc_url.lstrip("/")
#         loc_url = iri_to_uri(loc_url)

#         # <url>
#         url_el = SubElement(urlset, "url")
#         loc_el = SubElement(url_el, "loc")
#         loc_el.text = loc_url

#         # <news:news>
#         news_el = SubElement(url_el, f"{{{NS_NEWS}}}news")

#         # <news:publication>
#         pub_el = SubElement(news_el, f"{{{NS_NEWS}}}publication")

#         name_el = SubElement(pub_el, f"{{{NS_NEWS}}}name")
#         name_el.text = SITE_NAME

#         lang_el = SubElement(pub_el, f"{{{NS_NEWS}}}language")
#         lang_el.text = NEWS_LANGUAGE

#         # <news:publication_date>
#         pub_date_el = SubElement(news_el, f"{{{NS_NEWS}}}publication_date")
#         pub_date_el.text = obj.published_date.isoformat()

#         # <news:title>
#         title_el = SubElement(news_el, f"{{{NS_NEWS}}}title")
#         title_el.text = getattr(obj, "title", "Untitled Article")

#     xml_output = tostring(urlset, encoding="utf-8", method="xml")
#     return HttpResponse(xml_output, content_type="application/xml")