"""
URL configuration for wifiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from firstapp.sitemaps import IndexSitemap, PostSitemap
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render
from firstapp.views import sitemap_index_custom  # if you use a custom sitemap index view
# robots.txy
from django.http import HttpResponse
from django.urls import path, include, re_path
from django.views.static import serve


from firstapp.views_news_sitemap import news_sitemap


def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow:\n"
        "Sitemap: https://www.wifiresult.com/sitemap.xml\n"

    )
    return HttpResponse(content, content_type="text/plain")



# MAINTENANCE_MODE = True  # जब True होगा तब पूरी साइट बंद हो जाएगी
MAINTENANCE_MODE = False  # जब False होगा तब पूरी साइट open हो जाएगी
def maintenance_view(request):
    return render(request, "mainfile/maintenance.html", status=503)

if MAINTENANCE_MODE:
    urlpatterns = [
        path("", maintenance_view),
    ]
else:
 
    urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('firstapp.urls')),
    path("ckeditor5/", include("django_ckeditor_5.urls")),   # यह जरूरी है (image_upload आदि के लिए)
    path("robots.txt/", robots_txt, name="robots_txt"),
    path(
        "service-worker.js",
        TemplateView.as_view(
            template_name="service-worker.js",
            content_type="application/javascript",
        ),
        name="service_worker",
    ),
    # ... baaki URLs
    path("ads.txt/", TemplateView.as_view(template_name="mainfile/ads.txt", content_type="text/plain")),

    path("sitemap.xml/", sitemap_index_custom, name="sitemap-index"),
    path("sitemap-pages.xml/", sitemap, {"sitemaps": {"index": IndexSitemap}}, name="sitemap-index-only"),
    path("sitemap-posts.xml/", sitemap, {"sitemaps": {"post": PostSitemap}}, name="sitemap-post-only"),
    path("news-sitemap.xml/", news_sitemap, name="news-sitemap"),

]# development में media serve करने के लिए

# MEDIA (PDF, upload images, etc.)
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

# STATIC (CSS, JS, static images) – localhost par hi theek hai
urlpatterns += [
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]


# ✅ DEBUG True ho ya False – dono me static + media serve karega
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
# Custom handlers
# handler404 = "firstapp.views.custom_404"
handler500 = "firstapp.views.custom_500"