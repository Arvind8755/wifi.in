# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse, NoReverseMatch
from django.db.models import Max, Q
import datetime
from django.utils import timezone
from .models import Job, Result, Admitcard, Govtupdate


def _latest_content_lastmod():
    dates = []
    for Model in (Job, Result, Admitcard, Govtupdate):
        try:
            # only consider published items for lastmod
            qs = _published_qs(Model)
            dt = qs.aggregate(m=Max("published_date"))["m"]
            if dt:
                dates.append(dt)
        except Exception:
            pass
    return max(dates) if dates else timezone.now()


def _published_qs(Model):
    """
    Try to return a queryset containing only published items.
    Probes common field names: 'status' (value 'published'), 'published' boolean,
    'is_published' boolean, 'draft' boolean (exclude True), or fallbacks to all().
    """
    qs = Model.objects.all()
    # Try status='published'
    try:
        # Some models have a 'status' field with published/draft string
        if "status" in [f.name for f in Model._meta.get_fields()]:
            return qs.filter(status__iexact="published")
    except Exception:
        pass

    # Try boolean 'published'
    try:
        if "published" in [f.name for f in Model._meta.get_fields()]:
            return qs.filter(published=True)
    except Exception:
        pass

    # Try boolean 'is_published'
    try:
        if "is_published" in [f.name for f in Model._meta.get_fields()]:
            return qs.filter(is_published=True)
    except Exception:
        pass

    # Try 'draft' boolean field and exclude draft=True
    try:
        if "draft" in [f.name for f in Model._meta.get_fields()]:
            return qs.filter(draft=False)
    except Exception:
        pass

    # If none of the above fields found, try common conventions:
    # - if there is a 'status' but values differ, at least exclude 'draft' if present
    try:
        if "status" in [f.name for f in Model._meta.get_fields()]:
            # exclude common draft-like values
            return qs.exclude(status__in=["draft", "pending", "private"])
    except Exception:
        pass

    # Fallback: return all (you may want to change this to return none())
    return qs


class IndexSitemap(Sitemap):
    protocol = "https"
    changefreq = "daily"
    priority = 0.90
    sitemap_template = "sitemaps/post_sitemap.xml"

    # STATIC/LIST URLs
    def items(self):
        return [
            "/",    # Home      
            "/rojgar-result/",   
            "/free-job-alert/",
            "/result-bharat/",
            "/sarkari-jobs/",
            "/bihar-help/",
            "/latest-jobs/",          # Jobs list page
            "/search/",
            "/signup/",
            "/login/",
            "/all-india-govt-jobs/", # all india govt job page
            "/govt-jobs-today/",
            "/vacancy/",
            "/online-form/",
            "/sarkari-result-2025/",
            "/sarkari-naukri/",
            "/results/",       # Results list page
            "/sarkari-result/",  # all sarkari result page
            "/sarkari-result-2024/",
            "/board-result/",
            "/iti-result/",
            "/admit-card/",    # Admit Card list page
            "/exam-date/",
            "/sarkari-exam/",
            "/govt-updates/",  # Govt Updates list page
            "/admission/",
            "/answer-key/",
            "/scholarship/",
            "/sarkari-yojana/",
            "/syllabus/",
            "/contact-us/",
            "/about-us/",
            "/disclaimer",
            "/privacy-policy/",
            "/dmca/",
            "/hyperlink-policy/",
            "/terms-and-conditions/",
            "/editorial-policy/",
            "/fact-checking-and-corrections-policy/",
            "/advertising-policy/",
            "/grievance-officer/",
            "/cookie-policy/",
            "/sitemap.html/",
            "/authors/",
            "/authors/rajeshvari/",
            "/authors/sakshi/,"
            "/state-government-jobs/",
            "/andhra-pradesh-govt-jobs/",
            "/arunachal-pradesh-govt-jobs/",
            "/assam-govt-jobs/",
            "/bihar-govt-jobs/",
            "/chhattisgarh-govt-jobs/",
            "/delhi-govt-jobs/",
            "/goa-govt-jobs/",
            "/gujarat-govt-jobs/",
            "/haryana-govt-jobs/",
            "/himachal-pradesh-govt-jobs/",
            "/jammu-kashmir-govt-jobs/",
            "/jharkhand-govt-jobs/",
            "/karnataka-govt-jobs/",
            "/kerala-govt-jobs/",
            "/madhya-pradesh-govt-jobs/",
            "/maharashtra-govt-jobs/",
            "/manipur-govt-jobs/",
            "/meghalaya-govt-jobs/",
            "/mizoram-govt-jobs/",
            "/nagaland-govt-jobs/",
            "/odisha-govt-jobs/",
            "/punjab-govt-jobs/",
            "/rajasthan-govt-jobs/",
            "/sikkim-govt-jobs/",
            
            "/latest-result/",
            "/sarkari-result-2024/",
            "/latest-sarkari-result/",
            "/board-result/",
            "/wifi-result/",
            "/fast/",
            "/wifi-result-online/",
            "/careerwill-sarkari-result/",
            "/careers/",
            "/iti-result/",
            "/ncvtmis/",
            "/scvt/",
            "/admit-card/",    # Admit Card list page
            "/exam-date/",
            "/sarkari-exam/",
            "/govt-updates/",  # Govt Updates list page
            "/admission/",
            "/answer-key/",
            "/scholarship/",
            "/sarkari-yojana/",
            "/syllabus/",
            "/latest-news/",
            "/latest-sarkari-news/",
            "/sarkari-result-new-update/",
            "/blog/",
            "/contact-us/",
            "/about-us/",
            "/disclaimer",
            "/privacy-policy/",
            "/dmca/",
            "/hyperlink-policy/",
            "/terms-and-conditions/",
            "/editorial-policy/",
            "/fact-checking-and-corrections-policy/",
            "/advertising-policy/",
            "/grievance-officer/",
            "/cookie-policy/",
            "/sitemap.html/",
            "/authors/",
            "/authors/arvind-pal/",
            "/authors/rohan-sharma/",
            "/authors/priya-patel/",
            "/authors/neha-gupta/",
            "/about-founder-arvind-pal/",
            "/state-government-jobs/",
            "/andhra-pradesh-govt-jobs/",
            "/arunachal-pradesh-govt-jobs/",
            "/assam-govt-jobs/",
            "/bihar-govt-jobs/",
            "/chhattisgarh-govt-jobs/",
            "/delhi-govt-jobs/",
            "/goa-govt-jobs/",
            "/gujarat-govt-jobs/",
            "/haryana-govt-jobs/",
            "/himachal-pradesh-govt-jobs/",
            "/jammu-kashmir-govt-jobs/",
            "/jharkhand-govt-jobs/",
            "/karnataka-govt-jobs/",
            "/kerala-govt-jobs/",
            "/madhya-pradesh-govt-jobs/",
            "/maharashtra-govt-jobs/",
            "/manipur-govt-jobs/",
            "/meghalaya-govt-jobs/",
            "/mizoram-govt-jobs/",
            "/nagaland-govt-jobs/",
            "/odisha-govt-jobs/",
            "/punjab-govt-jobs/",
            "/rajasthan-govt-jobs/",
            "/sikkim-govt-jobs/",
            "/tamil-nadu-govt-jobs/",
            "/telangana-govt-jobs/",
            "/tripura-govt-jobs/",
            "/up-govt-jobs/",
            "/uttarakhand-govt-jobs/",
            "/west-bengal-govt-jobs/",
            "/andaman-nicobar-govt-jobs/",
            "/chandigarh-govt-jobs/",
            "/dadra-nagar-haveli-govt-jobs/",
            "/daman-diu-govt-jobs/",
            "/ladakh-govt-jobs/",
            "/lakshadweep-govt-jobs/",
            "/puducherry-govt-jobs/",
            "/central-govt-jobs/",
            "/all-education/",
            "/8th-pass-jobs/",
            "/10th-pass-jobs/",
            "/12th-pass-jobs/",
            "/graduation-job/",
            "/post-graduation/",
            "/diploma-jobs/",
            "/engineering-jobs/",
            "/medical-jobs/",
            "/iti-govt-jobs/",
            "/apprentice-job/",
            "/all-category-jobs/",
            "/railway-jobs/",
            "/bank-jobs/",
            "/defense-jobs/",
            "/police-jobs/",
            "/up-police/",
            "/delhi-police/",
            "/rajasthan-police/",
            "/ssc-jobs/",
            "/upsc-job/",
            "/government-teacher-jobs/",
            "/government-jobs/",
            "/jobs-by-education/",
            "/exam-results/",
            "/exam-dates/",
            "/education/",
            "/today-news/",
            "/india-results/",
            "/all-psc-in-india/", #all psc
            "/appsc-jobs/",
            "/arunachal-appsc-jobs/",
            "/assam-apsc-jobs/",
            "/bpsc-jobs/",
            "/cgpsc-jobs/",
            "/goa-psc-jobs/",
            "/gujarat-gpsc-jobs/",
            "/hpsc-jobs/",
            "/hppsc-jobs/",
            "/jkpsc-jobs/",
            "/jpsc-jobs/",
            "/kpsc-jobs/",
            "/kerala-psc-jobs/",
            "/mppsc-jobs/",
            "/mpsc-jobs/",
            "/manipur-psc-jobs/",
            "/meghalaya-psc-jobs/",
            "/mizoram-psc-jobs/",
            "/nagaland-psc-jobs/",
            "/opsc-jobs/",
            "/punjab-ppsc-jobs/",
            "/rpsc-jobs/",
            "/sikkim-psc-jobs/",
            "/tnpsc-jobs/",
            "/telangana-tspsc-jobs/",
            "/tripura-tpsc-jobs/",
            "/uppsc-jobs/",
            "/ukpsc-jobs/",
            "/west-bengal-wbpsc-jobs/",
            "/subscriber/",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # index-sitemap.xml में हर URL के लिए lastmod चाहिए → global latest दे देते हैं
        self._global_lastmod = _latest_content_lastmod()

    def location(self, item):
        return item
    
    # 🔥 Special rule → Home page = priority 1.0
    def priority(self, item):
        if item == "/":
            return 1.0
        return 0.9

    def lastmod(self, item):
        return self._global_lastmod

    # main index (sitemap.xml) में इस child के <lastmod> के लिए
    def get_latest_lastmod(self):
        return self._global_lastmod


class PostSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.8
    sitemap_template = "sitemaps/post_sitemap.xml"

    def items(self):
        # use _published_qs for each model so drafts are excluded
        jobs = list(_published_qs(Job))
        results = list(_published_qs(Result))
        admits = list(_published_qs(Admitcard))
        updates = list(_published_qs(Govtupdate))
        notifications = list(_published_qs(Notification))

        merged = jobs + results + admits + updates + notifications

        # sort by published_date (or fallback to now)
        def _key(x):
            return getattr(x, "published_date", None) or timezone.now()

        merged.sort(key=_key, reverse=True)
        return merged

    def lastmod(self, obj):
        # Prefer published_date or other date fields as in original
        for field in ("published_date", "updated_at", "modified", "created_at", "created"):
            if hasattr(obj, field):
                val = getattr(obj, field)
                if val:
                    return val
        return timezone.now()

    # main index (sitemap.xml) के लिए latest lastmod
    def get_latest_lastmod(self):
        return _latest_content_lastmod()

    def location(self, obj):
        # 1) get_absolute_url() safe
        if hasattr(obj, "get_absolute_url"):
            try:
                url = obj.get_absolute_url()
                if url:
                    return url
            except Exception:
                pass

        # model name, slug, pk fallbacks
        model = obj.__class__.__name__.lower()
        slug = getattr(obj, "slug", None)

        if slug:
            pattern = f"{model}_detail"
            try:
                return reverse(pattern, kwargs={"slug": slug})
            except NoReverseMatch:
                pass
            for ns in ("core", "main", "app"):
                try:
                    return reverse(f"{ns}:{pattern}", kwargs={"slug": slug})
                except NoReverseMatch:
                    continue

        base_map = {
            "job": "job",
            "result": "result",
            "admitcard": "admit-card",
            "govtupdate": "govt-update",
            "notification": "notification",
        }
        base = base_map.get(model, model)
        if slug:
            return f"/{base}/{slug}/"
        if getattr(obj, "pk", None) is not None:
            return f"/{base}/{obj.pk}/"
        return f"/{base}/"

    # ---------- Images for each item ----------
    def _images_for(self, obj):
        candidates = ("image", "featured_image", "thumbnail", "og_image", " image")
        caption_fields = ("image_caption", "title", "headline", "name", "image_alt")

        images = []
        for field in candidates:
            if hasattr(obj, field):
                f = getattr(obj, field)
                url = None
                try:
                    url = getattr(f, "url", None)
                except Exception:
                    url = None
                if not url and isinstance(f, str):
                    url = f
                if url:
                    cap = None
                    for cf in caption_fields:
                        if hasattr(obj, cf):
                            cap = getattr(obj, cf)
                            if cap:
                                break
                    images.append({"loc": url, "caption": cap})
                    break
        return images

    def get_urls(self, page=1, site=None, protocol=None):
        urls = super().get_urls(page=page, site=site, protocol=protocol)
        page_items = list(self.paginator.page(page).object_list)
        for i, info in enumerate(urls):
            obj = page_items[i]
            info["images"] = self._images_for(obj)
        return urls











# # sitemaps.py
# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse, NoReverseMatch
# from django.db.models import Max
# from django.utils import timezone
# from .models import Job, Result, Admitcard, Govtupdate, Notification


# def _latest_content_lastmod():
#     dates = []
#     for Model in (Job, Result, Admitcard, Govtupdate, Notification):
#         try:
#             dt = Model.objects.aggregate(m=Max("published_date"))["m"]
#             if dt:
#                 dates.append(dt)
#         except Exception:
#             pass
#     return max(dates) if dates else timezone.now()


# class IndexSitemap(Sitemap):
#     protocol = "https"
#     changefreq = "daily"
#     priority = 1.0
#     sitemap_template = "sitemaps/post_sitemap.xml"

#     # STATIC/LIST URLs
#     def items(self):
#         return [
#             "/",    # Home      
#             "/rojgar-result/",  
#             "/fast-job/",    
#             "/free-job-alert/",
#             "/result-bharat/",
#             "/sarkari-jobs/",
#             "/careerpower",
#             "/bihar-help/",
#             "/free-job-alert-2024/",
#             "/tools/",
#             "/tools/age-calculator/",
#             "/tools/image-resizer/",
#             "/tools/pdf-resizer/",
#             "/latest-jobs/",          # Jobs list page
#             "/recruitment/",
#             "/search/",
#             "/signup/",
#             "/login/",
#             "/all-india-govt-jobs/", # all india govt job page
#             "/latest-government-jobs/",
#             "/govt-jobs-today/",
#             "/vacancy/",
#             "/online-form/",
#             "/sarkari-result-2025/",
#             "/latest-jobs-sarkari-result/",
#             "/sarkari-result-upcoming-vacancy/",
#             "/sarkari-naukri/",
#             "/results/",       # Results list page
#             "/sarkari-result/",  # all sarkari result page
#             "/latest-result/",
#             "/sarkari-result-2024/",
#             "/latest-sarkari-result/",
#             "/board-result/",
#             "/wifi-result/",
#             "/fast/",
#             "/wifi-result-online/",
#             "/careerwill-sarkari-result/",
#             "/careers/",
#             "/iti-result/",
#             "/ncvtmis/",
#             "/scvt/",
#             "/admit-card/",    # Admit Card list page
#             "/exam-date/",
#             "/sarkari-exam/",
#             "/govt-updates/",  # Govt Updates list page
#             "/admission/",
#             "/answer-key/",
#             "/scholarship/",
#             "/sarkari-yojana/",
#             "/syllabus/",
#             "/latest-news/",
#             "/latest-sarkari-news/",
#             "/sarkari-result-new-update/",
#             "/blog/",
#             "/contact-us/",
#             "/about-us/",
#             "/disclaimer",
#             "/privacy-policy/",
#             "/dmca/",
#             "/hyperlink-policy/",
#             "/terms-and-conditions/",
#             "/editorial-policy/",
#             "/fact-checking-and-corrections-policy/",
#             "/advertising-policy/",
#             "/grievance-officer/",
#             "/cookie-policy/",
#             "/sitemap.html/",
#             "/authors/",
#             "/authors/arvind-pal/",
#             "/authors/rohan-sharma/",
#             "/authors/priya-patel/",
#             "/authors/neha-gupta/",
#             "/about-founder-arvind-pal/",
#             "/state-government-jobs/",
#             "/andhra-pradesh-govt-jobs/",
#             "/arunachal-pradesh-govt-jobs/",
#             "/assam-govt-jobs/",
#             "/bihar-govt-jobs/",
#             "/chhattisgarh-govt-jobs/",
#             "/delhi-govt-jobs/",
#             "/goa-govt-jobs/",
#             "/gujarat-govt-jobs/",
#             "/haryana-govt-jobs/",
#             "/himachal-pradesh-govt-jobs/",
#             "/jammu-kashmir-govt-jobs/",
#             "/jharkhand-govt-jobs/",
#             "/karnataka-govt-jobs/",
#             "/kerala-govt-jobs/",
#             "/madhya-pradesh-govt-jobs/",
#             "/maharashtra-govt-jobs/",
#             "/manipur-govt-jobs/",
#             "/meghalaya-govt-jobs/",
#             "/mizoram-govt-jobs/",
#             "/nagaland-govt-jobs/",
#             "/odisha-govt-jobs/",
#             "/punjab-govt-jobs/",
#             "/rajasthan-govt-jobs/",
#             "/sikkim-govt-jobs/",
#             "/tamil-nadu-govt-jobs/",
#             "/telangana-govt-jobs/",
#             "/tripura-govt-jobs/",
#             "/up-govt-jobs/",
#             "/uttarakhand-govt-jobs/",
#             "/west-bengal-govt-jobs/",
#             "/andaman-nicobar-govt-jobs/",
#             "/chandigarh-govt-jobs/",
#             "/dadra-nagar-haveli-govt-jobs/",
#             "/daman-diu-govt-jobs/",
#             "/ladakh-govt-jobs/",
#             "/lakshadweep-govt-jobs/",
#             "/puducherry-govt-jobs/",
#             "/central-govt-jobs/",
#             "/all-education/",
#             "/8th-pass-jobs/",
#             "/10th-pass-jobs/",
#             "/12th-pass-jobs/",
#             "/graduation-job/",
#             "/post-graduation/",
#             "/diploma-jobs/",
#             "/engineering-jobs/",
#             "/medical-jobs/",
#             "/iti-govt-jobs/",
#             "/apprentice-job/",
#             "/all-category-jobs/",
#             "/railway-jobs/",
#             "/bank-jobs/",
#             "/defense-jobs/",
#             "/police-jobs/",
#             "/up-police/",
#             "/delhi-police/",
#             "/rajasthan-police/",
#             "/ssc-jobs/",
#             "/upsc-job/",
#             "/government-teacher-jobs/",
#             "/government-jobs/",
#             "/jobs-by-education/",
#             "/exam-results/",
#             "/exam-dates/",
#             "/education/",
#             "/today-news/",
#             "/india-results/",
#             "/all-psc-in-india/", #all psc
#             "/appsc-jobs/",
#             "/arunachal-appsc-jobs/",
#             "/assam-apsc-jobs/",
#             "/bpsc-jobs/",
#             "/cgpsc-jobs/",
#             "/goa-psc-jobs/",
#             "/gujarat-gpsc-jobs/",
#             "/hpsc-jobs/",
#             "/hppsc-jobs/",
#             "/jkpsc-jobs/",
#             "/jpsc-jobs/",
#             "/kpsc-jobs/",
#             "/kerala-psc-jobs/",
#             "/mppsc-jobs/",
#             "/mpsc-jobs/",
#             "/manipur-psc-jobs/",
#             "/meghalaya-psc-jobs/",
#             "/mizoram-psc-jobs/",
#             "/nagaland-psc-jobs/",
#             "/opsc-jobs/",
#             "/punjab-ppsc-jobs/",
#             "/rpsc-jobs/",
#             "/sikkim-psc-jobs/",
#             "/tnpsc-jobs/",
#             "/telangana-tspsc-jobs/",
#             "/tripura-tpsc-jobs/",
#             "/uppsc-jobs/",
#             "/ukpsc-jobs/",
#             "/west-bengal-wbpsc-jobs/",
#             "/notifications/",
#             "/fastjobsearchers/",
#             "/sarkari/",
#             "/result-sarkari/",
#             "/subscriber/",

#         ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # index-sitemap.xml में हर URL के लिए lastmod चाहिए → global latest दे देते हैं
#         self._global_lastmod = _latest_content_lastmod()

#     def location(self, item):
#         return item

#     # प्रत्येक URL का <lastmod>
#     def lastmod(self, item):
#         return self._global_lastmod

#     # main index (sitemap.xml) में इस child के <lastmod> के लिए
#     def get_latest_lastmod(self):
#         return self._global_lastmod


# class PostSitemap(Sitemap):
#     protocol = "https"
#     changefreq = "daily"
#     priority = 0.8
#     # image-enabled custom template
#     sitemap_template = "sitemaps/post_sitemap.xml"

#     def items(self):
#         jobs = Job.objects.all().filter(status='published')
#         results = Result.objects.all()
#         admits = Admitcard.objects.all()
#         updates = Govtupdate.objects.all()
#         notifications = Notification.objects.all()
#         merged = list(jobs) + list(results) + list(admits) + list(updates) + list(notifications)

#         def _key(x):
#             return getattr(x, "published_date", None)  
#         merged.sort(key=_key, reverse=True)
#         return merged

#     def lastmod(self, obj):
#         return getattr(obj, "published_date", None)

#     # main index (sitemap.xml) में इस child के <lastmod> के लिए
#     def get_latest_lastmod(self):
#         return _latest_content_lastmod()

#     def location(self, obj):
#         # 1) get_absolute_url() safe
#         if hasattr(obj, "get_absolute_url"):
#             try:
#                 url = obj.get_absolute_url()
#                 if url:
#                     return url
#             except Exception:
#                 pass

#         # "job" / "result" / "admitcard" / "govtupdate"
#         model = obj.__class__.__name__.lower()
#         slug = getattr(obj, "slug", None)
#         pk = getattr(obj, "pk", None)

#         # 2) reverse tries
#         if slug:
#             pattern = f"{model}_detail"
#             try:
#                 return reverse(pattern, kwargs={"slug": slug})
#             except NoReverseMatch:
#                 pass
#             for ns in ("core", "main", "app"):
#                 try:
#                     return reverse(f"{ns}:{pattern}", kwargs={"slug": slug})
#                 except NoReverseMatch:
#                     continue

#         # 3) hard-coded fallback
#         base_map = {
#             "job": "job",
#             "result": "result",
#             "admitcard": "admit-card",
#             "govtupdate": "govt-update",
#             "notification": "notification",
#         }
#         base = base_map.get(model, model)
#         if slug:
#             return f"/{base}/{slug}/"
#         if pk is not None:
#             return f"/{base}/{pk}/"
#         return f"/{base}/"

#     # ---------- Images for each item ----------
#     def _images_for(self, obj):
#         """
#         अपनी models के field नाम के हिसाब से इसमें बदलाव करें:
#         - ImageField: image / featured_image / thumbnail / og_image
#         - Caption: image_caption / title / headline
#         Multiple images चाहें तो list बढ़ा सकते हैं।
#         """
#         candidates = ("image", "featured_image",
#                       "thumbnail", "og_image", " image")
#         caption_fields = ("image_caption", "title",
#                           "headline", "name", "image_alt")

#         images = []
#         for field in candidates:
#             if hasattr(obj, field):
#                 f = getattr(obj, field)
#                 url = None
#                 try:
#                     # ImageField/FileField
#                     url = getattr(f, "url", None)
#                 except Exception:
#                     url = None
#                 if not url and isinstance(f, str):
#                     url = f  # अगर string URL stored है

#                 if url:
#                     cap = None
#                     for cf in caption_fields:
#                         if hasattr(obj, cf):
#                             cap = getattr(obj, cf)
#                             if cap:
#                                 break
#                     images.append({"loc": url, "caption": cap})
#                     break  # एक primary image काफी है; ज़रूरत हो तो हटाएं
#         return images

#     # Django default get_urls() को extend करके image data inject करें
#     def get_urls(self, page=1, site=None, protocol=None):
#         urls = super().get_urls(page=page, site=site, protocol=protocol)
#         # current page के objects
#         page_items = list(self.paginator.page(page).object_list)
#         for i, info in enumerate(urls):
#             obj = page_items[i]
#             info["images"] = self._images_for(obj)  # list of dicts
#         return urls

#     def items(self):
#         items = list(Job.objects.all()) + list(Result.objects.all()) + \
#             list(Admitcard.objects.all()) + list(Govtupdate.objects.all()) + list(Notification.objects.all())
#         # latest first; None होने पर now()
#         items.sort(key=lambda x: getattr(x, "published_date", None)
#                    or timezone.now(), reverse=True)
#         return items

#     def lastmod(self, obj):
#         for field in ("updated_at", "modified", "published_date", "created_at", "created"):
#             if hasattr(obj, field):
#                 val = getattr(obj, field)
#                 if val:
#                     return val
#         return timezone.now()

#     def location(self, obj):
#         # try get_absolute_url()
#         if hasattr(obj, "get_absolute_url"):
#             try:
#                 url = obj.get_absolute_url()
#                 if url:
#                     return url
#             except Exception:
#                 pass

#         # reverse by common names
#         model = obj._meta.model_name
#         slug = getattr(obj, "slug", None)
#         if slug:
#             for name in (f"{model}_detail", f"core:{model}_detail", f"main:{model}_detail", f"app:{model}_detail"):
#                 try:
#                     return reverse(name, kwargs={"slug": slug})
#                 except NoReverseMatch:
#                     pass

#         # hard-coded fallback
#         base_map = {"job": "job", "result": "result",
#                     "admitcard": "admit-card", "govtupdate": "govt-update", "notification": "notification"}
#         base = base_map.get(model, model)
#         if slug:
#             return f"/{base}/{slug}/"
#         return f"/{base}/{getattr(obj, 'pk', '')}/"


# #  news_sitemap


