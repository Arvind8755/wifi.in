from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from bs4 import BeautifulSoup
from django.urls import reverse
import html
from django.utils.html import strip_tags

from django_ckeditor_5.fields import CKEditor5Field


class Job(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    description = models.TextField()
    tag = models.CharField(max_length=250)
    category = models.CharField(max_length=100, blank=True, null=True)
    h1 = CKEditor5Field('h1', config_name='default')  # 'default' वही config_name है
    author = CKEditor5Field('author', config_name='default')  # 'default' वही config_name है
    extra_information = CKEditor5Field('extra_information', config_name='default')  # 'default' वही config_name है

    overview = CKEditor5Field('overview', config_name='default')  # 'default' वही config_name है

    important_dates = CKEditor5Field('important_dates', config_name='default')  # 'default' वही config_name है

    vacancy_details = CKEditor5Field('vacancy_details', config_name='default')  # 'default' वही config_name है

    eligibillity_criteria = CKEditor5Field('eligibillity_criteria', config_name='default')  # 'default' वही config_name है

    application_fee = CKEditor5Field('application_fee', config_name='default')  # 'default' वही config_name है

    selection_process = CKEditor5Field('selection_process', config_name='default')  # 'default' वही config_name है

    salary_structure = CKEditor5Field('salary_structure', config_name='default')  # 'default' वही config_name है

    How_to_appply = CKEditor5Field('How_to_appply', config_name='default')  # 'default' वही config_name है

    important_link = CKEditor5Field('important_link', config_name='default')  # 'default' वही config_name है

    faq_q1 = models.CharField(max_length=555, blank=True, null=True)
    faq_a1 = models.TextField(blank=True, null=True)
    faq_q2 = models.CharField(max_length=555, blank=True, null=True)
    faq_a2 = models.TextField(blank=True, null=True)
    faq_q3 = models.CharField(max_length=555, blank=True, null=True)
    faq_a3 = models.TextField(blank=True, null=True)
    faq_q4 = models.CharField(max_length=555, blank=True, null=True)
    faq_a4 = models.TextField(blank=True, null=True)
    faq_q5 = models.CharField(max_length=555, blank=True, null=True)
    faq_a5 = models.TextField(blank=True, null=True)
    faq_q6 = models.CharField(max_length=555, blank=True, null=True)
    faq_a6 = models.TextField(blank=True, null=True)
    faq_q7 = models.CharField(max_length=555, blank=True, null=True)
    faq_a7 = models.TextField(blank=True, null=True)
    faq_q8 = models.CharField(max_length=555, blank=True, null=True)
    faq_a8 = models.TextField(blank=True, null=True)
    faq_q9 = models.CharField(max_length=555, blank=True, null=True)
    faq_a9 = models.TextField(blank=True, null=True)
    faq_q10 = models.CharField(max_length=555, blank=True, null=True)
    faq_a10 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=1000,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")

    
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
# ⭐ New Field Added (Draft / Published)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    @property
    def clean_h1(self):
        if not self.h1:
            return ""
        return html.unescape(strip_tags(self.h1))


    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug": self.slug})  # /latest-jobs/<slug>/

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:250]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Result(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    description = models.TextField()
    tag = models.CharField(max_length=250)
    category = models.CharField(max_length=100, blank=True, null=True)
    h1 = CKEditor5Field('h1', config_name='default')  # 'default' वही config_name है
    author = CKEditor5Field('author', config_name='default')  # 'default' वही config_name है
    extra_information = CKEditor5Field('extra_information', config_name='default')  # 'default' वही config_name है

    overview = CKEditor5Field('overview', config_name='default')  # 'default' वही config_name है

    important_dates = CKEditor5Field('important_dates', config_name='default')  # 'default' वही config_name है

    vacancy_details = CKEditor5Field('vacancy_details', config_name='default')  # 'default' वही config_name है

    salary_structure = CKEditor5Field('salary_structure', config_name='default')  # 'default' वही config_name है

    eligibillity_criteria = CKEditor5Field('eligibillity_criteria', config_name='default')  # 'default' वही config_name है

    application_fee = CKEditor5Field('application_fee', config_name='default')  # 'default' वही config_name है

    selection_process = CKEditor5Field('selection_process', config_name='default')  # 'default' वही config_name है

    download_result = CKEditor5Field('download_result', config_name='default')  # 'default' वही config_name है

    cutoff_Marks = CKEditor5Field('cutoff_Marks', config_name='default')  # 'default' वही config_name है

    important_link = CKEditor5Field('important_link', config_name='default')  # 'default' वही config_name है

    faq_q1 = models.CharField(max_length=555, blank=True, null=True)
    faq_a1 = models.TextField(blank=True, null=True)
    faq_q2 = models.CharField(max_length=555, blank=True, null=True)
    faq_a2 = models.TextField(blank=True, null=True)
    faq_q3 = models.CharField(max_length=555, blank=True, null=True)
    faq_a3 = models.TextField(blank=True, null=True)
    faq_q4 = models.CharField(max_length=555, blank=True, null=True)
    faq_a4 = models.TextField(blank=True, null=True)
    faq_q5 = models.CharField(max_length=555, blank=True, null=True)
    faq_a5 = models.TextField(blank=True, null=True)
    faq_q6 = models.CharField(max_length=555, blank=True, null=True)
    faq_a6 = models.TextField(blank=True, null=True)
    faq_q7 = models.CharField(max_length=555, blank=True, null=True)
    faq_a7 = models.TextField(blank=True, null=True)
    faq_q8 = models.CharField(max_length=555, blank=True, null=True)
    faq_a8 = models.TextField(blank=True, null=True)
    faq_q9 = models.CharField(max_length=555, blank=True, null=True)
    faq_a9 = models.TextField(blank=True, null=True)
    faq_q10 = models.CharField(max_length=555, blank=True, null=True)
    faq_a10 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=1000,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")

    
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    @property
    def clean_h1(self):
        if not self.h1:
            return ""
        return html.unescape(strip_tags(self.h1))


    def get_absolute_url(self):
        return reverse("result_detail", kwargs={"slug": self.slug})  # /results/<slug>/

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:250]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    


class Admitcard(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
        
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    description = models.TextField()
    keywords = models.TextField(blank=True, help_text="Enter SEO keywords separated by comma. Example: government jobs, wb primary teacher, latest jobs 2025")
    tag = models.CharField(max_length=250)
    category = models.CharField(max_length=100, blank=True, null=True)
    h1 = CKEditor5Field('h1', config_name='default')  # 'default' वही config_name है
    author = CKEditor5Field('author', config_name='default')  # 'default' वही config_name है
    extra_information = CKEditor5Field('extra_information', config_name='default')  # 'default' वही config_name है

    overview = CKEditor5Field('overview', config_name='default')  # 'default' वही config_name है

    important_dates = CKEditor5Field('important_dates', config_name='default')  # 'default' वही config_name है

    vacancy_details = CKEditor5Field('vacancy_details', config_name='default')  # 'default' वही config_name है

    eligibillity_criteria = CKEditor5Field('eligibillity_criteria', config_name='default')  # 'default' वही config_name है

    application_fee = CKEditor5Field('application_fee', config_name='default')  # 'default' वही config_name है

    selection_process = CKEditor5Field('selection_process', config_name='default')  # 'default' वही config_name है

    salary_structure = CKEditor5Field('salary_structure', config_name='default')  # 'default' वही config_name है

    check_download = CKEditor5Field('check_download', config_name='default')  # 'default' वही config_name है

    important_link = CKEditor5Field('important_link', config_name='default')  # 'default' वही config_name है

    faq_q1 = models.CharField(max_length=555, blank=True, null=True)
    faq_a1 = models.TextField(blank=True, null=True)
    faq_q2 = models.CharField(max_length=555, blank=True, null=True)
    faq_a2 = models.TextField(blank=True, null=True)
    faq_q3 = models.CharField(max_length=555, blank=True, null=True)
    faq_a3 = models.TextField(blank=True, null=True)
    faq_q4 = models.CharField(max_length=555, blank=True, null=True)
    faq_a4 = models.TextField(blank=True, null=True)
    faq_q5 = models.CharField(max_length=555, blank=True, null=True)
    faq_a5 = models.TextField(blank=True, null=True)
    faq_q6 = models.CharField(max_length=555, blank=True, null=True)
    faq_a6 = models.TextField(blank=True, null=True)
    faq_q7 = models.CharField(max_length=555, blank=True, null=True)
    faq_a7 = models.TextField(blank=True, null=True)
    faq_q8 = models.CharField(max_length=555, blank=True, null=True)
    faq_a8 = models.TextField(blank=True, null=True)
    faq_q9 = models.CharField(max_length=555, blank=True, null=True)
    faq_a9 = models.TextField(blank=True, null=True)
    faq_q10 = models.CharField(max_length=555, blank=True, null=True)
    faq_a10 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=1000,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")

    
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    @property
    def clean_h1(self):
        if not self.h1:
            return ""
        return html.unescape(strip_tags(self.h1))


    def get_absolute_url(self):
        return reverse("admitcard_detail", kwargs={"slug": self.slug})  # /admit-card/<slug>/

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:250]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




class Govtupdate(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    description = models.TextField()
    keywords = models.TextField(blank=True, help_text="Enter SEO keywords separated by comma. Example: government jobs, wb primary teacher, latest jobs 2025")
    tag = models.CharField(max_length=250)
    category = models.CharField(max_length=100, blank=True, null=True)
    h1 = CKEditor5Field('h1', config_name='default')  # 'default' वही config_name है
    author = CKEditor5Field('author', config_name='default')  # 'default' वही config_name है
    extra_information = CKEditor5Field('extra_information', config_name='default')  # 'default' वही config_name है

    overview = CKEditor5Field('overview', config_name='default')  # 'default' वही config_name है

    important_dates = CKEditor5Field('important_dates', config_name='default')  # 'default' वही config_name है

    details = CKEditor5Field('details', config_name='default')  # 'default' वही config_name है

    eligibillity_criteria = CKEditor5Field('eligibillity_criteria', config_name='default')  # 'default' वही config_name है

    syllabus = CKEditor5Field('syllabus', config_name='default')  # 'default' वही config_name है

    application_fee = CKEditor5Field('application_fee', config_name='default')  # 'default' वही config_name है

    # salary_structure = CKEditor5Field('salary_structure', config_name='default')  # 'default' वही config_name है

    # check_download = CKEditor5Field('check_download', config_name='default')  # 'default' वही config_name है

    selection_process = CKEditor5Field('selection_process', config_name='default')  # 'default' वही config_name है

    how_to_apply_online = CKEditor5Field('how_to_apply_online', config_name='default')  # 'default' वही config_name है

    important_link = CKEditor5Field('important_link', config_name='default')  # 'default' वही config_name है

    faq_q1 = models.CharField(max_length=555, blank=True, null=True)
    faq_a1 = models.TextField(blank=True, null=True)
    faq_q2 = models.CharField(max_length=555, blank=True, null=True)
    faq_a2 = models.TextField(blank=True, null=True)
    faq_q3 = models.CharField(max_length=555, blank=True, null=True)
    faq_a3 = models.TextField(blank=True, null=True)
    faq_q4 = models.CharField(max_length=555, blank=True, null=True)
    faq_a4 = models.TextField(blank=True, null=True)
    faq_q5 = models.CharField(max_length=555, blank=True, null=True)
    faq_a5 = models.TextField(blank=True, null=True)
    faq_q6 = models.CharField(max_length=555, blank=True, null=True)
    faq_a6 = models.TextField(blank=True, null=True)
    faq_q7 = models.CharField(max_length=555, blank=True, null=True)
    faq_a7 = models.TextField(blank=True, null=True)
    faq_q8 = models.CharField(max_length=555, blank=True, null=True)
    faq_a8 = models.TextField(blank=True, null=True)
    faq_q9 = models.CharField(max_length=555, blank=True, null=True)
    faq_a9 = models.TextField(blank=True, null=True)
    faq_q10 = models.CharField(max_length=555, blank=True, null=True)
    faq_a10 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=1000,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")

    
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    @property
    def clean_h1(self):
        if not self.h1:
            return ""
        return html.unescape(strip_tags(self.h1))


    def get_absolute_url(self):
        return reverse("govt-update-detail", kwargs={"slug": self.slug})  # /news/<slug>/

    def save(self, *args, **kwargs):
        # <span> टैग हटाने वाला कोड
        if self.content:
            soup = BeautifulSoup(self.content, "html.parser")
            for tag in soup.find_all("span"):
                tag.unwrap()  # span हटाकर अंदर का text रहने देगा
            self.content = str(soup)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:250]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Boxname(models.Model):
    title = models.CharField(max_length=550)
    box1 = CKEditor5Field('box1', config_name='default')  # 'default' वही config_name है
    published_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

#Job comment
class JobComment(models.Model):
    user =models.ForeignKey('auth.User', on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.comment
    
# Result comment

class ResultComment(models.Model):
    user =models.ForeignKey('auth.User', on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.comment
    
# Admitcard  comment
class AdmitcardComment(models.Model):
    user =models.ForeignKey('auth.User', on_delete=models.CASCADE)
    admitcard = models.ForeignKey(Admitcard, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.comment
    
#govt update comment
class GovtupdateComment(models.Model):
    user =models.ForeignKey('auth.User', on_delete=models.CASCADE)
    govtupdate = models.ForeignKey(Govtupdate, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.comment
    




    #pdf

from django.db import models
from django.utils import timezone
import uuid
import os

def pdf_upload_path(instance, filename):
    # unique filename to avoid collisions
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"{uuid.uuid4().hex}{ext}"
    return f'pdfs/{timezone.now().year}/{timezone.now().month}/{new_name}'

class PdfDocument(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to=pdf_upload_path)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filesize = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pdf and not self.filesize:
            try:
                self.filesize = self.pdf.size
            except Exception:
                self.filesize = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

from django.db import models

class Notification(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    keywords = models.TextField(blank=True, help_text="Enter SEO keywords separated by comma. Example: government jobs, wb primary teacher, latest jobs 2025")
    tag = models.CharField(max_length=250)
    author = CKEditor5Field('author', config_name='default')  # 'default' वही config_name है
    h1 = CKEditor5Field('h1', config_name='default')  # 'default' वही config_name है
    overview = CKEditor5Field('overview', config_name='default',  help_text="Yahan PDF ka text paste karein (clean / formatted).") 
    
    # PDF file
    pdf_file = models.FileField(
        upload_to="notifications_pdf/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse("notification_detail", kwargs={"slug": self.slug})  # /notification/<slug>/

    def __str__(self):
        return self.title

#subscriber

from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)  # Unique emails only
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Automatic timestamp

    def __str__(self):
        return self.email