# firstapp/feeds.py
import logging
from itertools import chain

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.html import strip_tags
from django.contrib.sites.models import Site
from django.utils import timezone

from .models import Job, Result, Admitcard, Govtupdate

DEBUG_FEED = False
logger = logging.getLogger(__name__)

DATE_FIELDS_PRIORITY = (
    'published_date', 'publish_date', 'published_on',
    'created_at', 'updated_at', 'date'
)
IMAGE_FIELD_CANDIDATES = ('featured_image', 'image', 'thumbnail', 'banner_image', 'photo')
# categories removed per request


def _dlog(msg, *args):
    if DEBUG_FEED:
        try:
            logger.debug(msg, *args)
        except Exception:
            try:
                print(msg % args if args else msg)
            except Exception:
                pass


def pick_date(obj):
    for f in DATE_FIELDS_PRIORITY:
        if hasattr(obj, f):
            val = getattr(obj, f)
            if val:
                return val
    return None


def is_published(obj):
    for flag in ('published', 'is_published', 'is_active', 'active'):
        if hasattr(obj, flag):
            try:
                v = getattr(obj, flag)
                if v is not None:
                    return bool(v)
            except Exception:
                pass
    if hasattr(obj, 'status'):
        try:
            st = getattr(obj, 'status')
            if isinstance(st, str) and st.lower() in ('draft', 'private', 'archived'):
                return False
        except Exception:
            pass
    dt = pick_date(obj)
    if dt:
        try:
            if dt > timezone.now():
                return False
        except Exception:
            pass
    return True


class DiscoverRssFeed(Rss201rev2Feed):
    """
    Custom RSS generator: declare namespaces and write extra elements.
    We explicitly emit <link>, <pubDate>, <guid>, <title>, <media:content>, <enclosure>, <description>.
    """

    def root_attributes(self):
        attrs = super().root_attributes() or {}
        attrs['xmlns:webfeeds'] = 'http://webfeeds.org/rss/1.0'
        attrs['xmlns:media'] = 'http://search.yahoo.com/mrss/'
        attrs['xmlns:atom'] = 'http://www.w3.org/2005/Atom'
        return attrs

    def add_root_elements(self, handler):
        super().add_root_elements(handler)
        try:
            site = Site.objects.get_current()
            domain = site.domain
            logo = f'https://{domain}/static/logo/wifiresult-logo.png'
            handler.startElement('webfeeds:cover', {'image': logo}); handler.endElement('webfeeds:cover')
            handler.startElement('webfeeds:logo', {}); handler.characters(logo); handler.endElement('webfeeds:logo')
            handler.startElement('webfeeds:accentColor', {}); handler.characters('0A6EB4'); handler.endElement('webfeeds:accentColor')
            handler.startElement('link', {'rel': 'hub', 'href': 'https://pubsubhubbub.appspot.com/'}); handler.endElement('link')
        except Exception as e:
            _dlog("webfeeds/root skipped: %r", e)

    def add_item_elements(self, handler, item):
        """
        item: dict returned by Feed.item_extra_kwargs.
        We'll explicitly emit link, pubDate, guid, title, media/enclosure, description.
        """
        # explicit link
        try:
            link = item.get('discover_link')
            if link:
                handler.startElement('link', {}); handler.characters(str(link)); handler.endElement('link')
        except Exception as e:
            _dlog("link emit skipped: %r", e)

        # explicit pubDate
        try:
            pub = item.get('discover_pubdate')
            if pub:
                # use Rss201rev2Feed's rfc2822_date formatter
                try:
                    pubstr = self.rfc2822_date(pub)
                except Exception:
                    # fallback: convert to iso format
                    pubstr = str(pub)
                handler.startElement('pubDate', {}); handler.characters(pubstr); handler.endElement('pubDate')
        except Exception as e:
            _dlog("pubDate emit skipped: %r", e)

        # explicit guid
        try:
            guid = item.get('discover_guid')
            if guid:
                handler.startElement('guid', {}); handler.characters(str(guid)); handler.endElement('guid')
        except Exception as e:
            _dlog("guid emit skipped: %r", e)

        # explicit title (guarantee)
        try:
            t = item.get('discover_title')
            if t:
                handler.startElement('title', {}); handler.characters(str(t)); handler.endElement('title')
        except Exception as e:
            _dlog("explicit title skipped: %r", e)

        # media + enclosure (image)
        try:
            img = item.get('discover_media')
            if img:
                attrs = {'url': str(img), 'medium': 'image'}
                w = item.get('discover_media_width')
                h = item.get('discover_media_height')
                if w:
                    attrs['width'] = str(w)
                if h:
                    attrs['height'] = str(h)
                handler.startElement('media:content', attrs); handler.endElement('media:content')
                mime = 'image/jpeg' if str(img).lower().endswith(('.jpg', '.jpeg')) else 'image/webp'
                handler.startElement('enclosure', {'url': str(img), 'type': mime}); handler.endElement('enclosure')
        except Exception as e:
            _dlog("media/enclosure skipped: %r", e)

        # description
        try:
            desc = item.get('discover_description')
            if desc:
                handler.startElement('description', {}); handler.characters(str(desc)); handler.endElement('description')
        except Exception as e:
            _dlog("description skipped: %r", e)


class LatestAllFeed(Feed):
    feed_type = DiscoverRssFeed
    title = "WiFiResult — Latest Posts"
    description = "Latest Jobs, Results, Admitcards and Government updates from WiFiResult."
    limit = 50

    def _current_domain(self):
        try:
            return Site.objects.get_current().domain
        except Exception:
            return 'localhost'

    def feed_url(self):
        return f"https://{self._current_domain()}/feed/"

    def link(self):
        return f"https://{self._current_domain()}/"

    def _absolute_link_for(self, item):
        domain = self._current_domain()
        if hasattr(item, 'get_absolute_url'):
            try:
                rel = item.get_absolute_url()
                if rel:
                    if not rel.startswith('/'):
                        rel = '/' + rel
                    return f"https://{domain}{rel}"
            except Exception as e:
                _dlog("get_absolute_url error: %r", e)
        if hasattr(item, 'slug'):
            try:
                slug = getattr(item, 'slug')
                if slug:
                    prefix = item.__class__.__name__.lower()
                    return f"https://{domain}/{prefix}/{slug}/"
            except Exception as e:
                _dlog("slug fallback error: %r", e)
        try:
            return f"https://{domain}/{item.__class__.__name__.lower()}/{getattr(item, 'pk', '')}/"
        except Exception as e:
            _dlog("final link fallback failed: %r", e)
            return f"https://{domain}/"

    def _get_image_url(self, item):
        domain = self._current_domain()
        for f in IMAGE_FIELD_CANDIDATES:
            if hasattr(item, f):
                try:
                    val = getattr(item, f)
                    if hasattr(val, 'url') and val.url:
                        url = val.url
                        if url.startswith('/'):
                            return f'https://{domain}{url}'
                        return url
                    if isinstance(val, str) and val:
                        return val
                except Exception as e:
                    _dlog("image read error (%s): %r", f, e)
        return f"https://{domain}/static/logo/wifiresult-logo.png"

    def items(self):
        raw = list(chain(
            Job.objects.all(),
            Result.objects.all(),
            Admitcard.objects.all(),
            Govtupdate.objects.all(),
        ))

        filtered = []
        for obj in raw:
            dt = pick_date(obj)
            if not dt:
                _dlog("skip no-date: %r", obj)
                continue
            if not is_published(obj):
                _dlog("skip not-published: %r", obj)
                continue
            link = self._absolute_link_for(obj)
            if not link:
                _dlog("skip no-link: %r", obj)
                continue
            filtered.append((dt, link, obj))

        filtered.sort(key=lambda t: t[0], reverse=True)

        seen = set()
        unique = []
        for dt, link, obj in filtered:
            if link in seen:
                _dlog("duplicate skipped: %s", link)
                continue
            seen.add(link)
            unique.append(obj)
            if len(unique) >= self.limit:
                break

        _dlog("final feed items: %d", len(unique))
        return unique

    def item_title(self, item):
        for f in ('title', 'name', 'headline'):
            if hasattr(item, f):
                try:
                    v = getattr(item, f)
                    if v:
                        return str(v)
                except Exception:
                    pass
        return f"{item.__class__.__name__} #{getattr(item, 'pk', '')}"

    def item_description(self, item):
        # use description field (or fallbacks) — this will be used as discover_description
        for f in ('description', 'content', 'summary', 'excerpt', 'body'):
            if hasattr(item, f):
                try:
                    v = getattr(item, f)
                    if v:
                        return strip_tags(str(v))[:800]
                except Exception:
                    pass
        return ''

    def item_link(self, item):
        return self._absolute_link_for(item)

    def item_pubdate(self, item):
        dt = pick_date(item)
        if not dt:
            return None
        try:
            # FORCE UTC for feed stability (Google-friendly)
            return dt.astimezone(timezone.utc)
        except Exception:
            try:
                return timezone.make_aware(dt).astimezone(timezone.utc)
            except Exception:
                return dt

    def item_guid(self, item):
        link = self._absolute_link_for(item)
        if link:
            return link
        return f"{self._current_domain()}/{item.__class__.__name__.lower()}/{getattr(item, 'pk', '')}/"

    def item_extra_kwargs(self, item):
        image_url = self._get_image_url(item)

        # try to detect width/height if stored
        w = None; h = None
        try:
            if hasattr(item, 'image_width') and hasattr(item, 'image_height'):
                w = getattr(item, 'image_width')
                h = getattr(item, 'image_height')
        except Exception:
            pass

        # NOTE: author and category removed as requested
        return {
            'discover_title': self.item_title(item),
            'discover_media': image_url,
            'discover_media_width': w,
            'discover_media_height': h,
            # use description instead of summary
            'discover_description': (self.item_description(item) or '')[:1000],
            # explicit link/guid/pubdate so add_item_elements can emit them
            'discover_link': self._absolute_link_for(item),
            'discover_guid': self.item_guid(item),
            'discover_pubdate': self.item_pubdate(item),
        }
