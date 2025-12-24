from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Job, Result, Admitcard, Govtupdate, Boxname, JobComment, ResultComment, AdmitcardComment, GovtupdateComment 
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.text import slugify
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render

from django.db.models import Q
from django.contrib.auth.decorators import login_required
current_time = timezone.now()
from django.conf import settings



# Create your views here.

# @login_required(login_url='signup')


def home(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:20]           
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:20]
    admitcards = Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:20]
    govtupdates = Govtupdate.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:20]
    boxnames = Boxname.objects.all().order_by("-published_date")
    # 2) chain se sabko jod do
    mixed_objects = list(chain(jobs, results, admitcards, govtupdates))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:16]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "admitcards": admitcards,
        "govtupdates": govtupdates,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    # ✅ sirf teen arguments
    return render(request, "mainfile/index.html", context)

def rojgarresult(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    admitcards = Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    govtupdates = Govtupdate.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    boxnames = Boxname.objects.all().order_by("-published_date")
    # 2) chain se sabko jod do
    mixed_objects = list(chain(jobs, results, admitcards, govtupdates))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:15]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "admitcards": admitcards,
        "govtupdates": govtupdates,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    return render (request, "jobs/rojgarresult.html", context)


def Sarkari(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    admitcards = Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    govtupdates = Govtupdate.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    boxnames = Boxname.objects.all().order_by("-published_date")

    # 2) chain se sabko jod do
    mixed_objects = list(chain(jobs, results, admitcards, govtupdates))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:12]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "admitcards": admitcards,
        "govtupdates": govtupdates,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    return render (request, "jobs/Sarkari.html", context)



def freejobalert(request):
    jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:10]
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    admitcards = Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    govtupdates = Govtupdate.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    boxnames = Boxname.objects.all().order_by("-published_date")

    # 2) chain se sabko jod do
    mixed_objects = list(chain(jobs, results, admitcards, govtupdates))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:16]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "admitcards": admitcards,
        "govtupdates": govtupdates,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    return render (request, "jobs/freejobalert.html", context)

def sarkarijobs(request):
    jobs = Job.objects.all().order_by("-published_date")[:10]
    # jobs = Job.objects.filter(is_active=True).order_by('-published_date')[:3]
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    admitcards = Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    govtupdates = Govtupdate.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    boxnames = Boxname.objects.all().order_by("-published_date")
    # 2) chain se sabko jod do
    mixed_objects = list(chain(jobs, results, admitcards, govtupdates))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:15]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "admitcards": admitcards,
        "govtupdates": govtupdates,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    return render (request, "jobs/sarkarijobs.html", context)

def biharhelp(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:15]
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:15]
    admitcards = Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:15]
    boxnames = Boxname.objects.all().order_by("-published_date")

    # 2) chain se sabko jod do
    mixed_objects = list(chain(jobs, results, admitcards))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:15]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "admitcards": admitcards,
        # "govtupdates": govtupdates,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    # ✅ sirf teen arguments
    return render(request, "jobs/biharhelp.html", context)


def resultbharat(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    admitcards = Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    govtupdates = Govtupdate.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:10]
    boxnames = Boxname.objects.all().order_by("-published_date")

    # 2) chain se sabko jod do
    mixed_objects = list(chain(jobs, results, admitcards))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:15]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "admitcards": admitcards,
        "govtupdates": govtupdates,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    return render (request, "jobs/resultbharat.html", context)

def sarkariresult(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:20]
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:20]
    govtupdates = Govtupdate.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:20]
    boxnames = Boxname.objects.all().order_by("-published_date")

        # 2) chain se sabko jod do
    mixed_objects = list(chain(jobs, results, govtupdates))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:20]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "govtupdates": govtupdates,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    return render (request, "results/sarkariresult.html", context)

def all_india_govt_jobs(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:20]
    boxnames = Boxname.objects.all().order_by("-published_date")

    mixed_objects = list(chain(jobs))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:15]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    return render (request, "jobs/allindiagovtjobs.html", context)

def sarkariresult2025(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:30]
    results = Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")[:30]
    boxnames = Boxname.objects.all().order_by("-published_date")

    mixed_objects = list(chain(jobs, results))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:9]

    context = {
        "published_time": timezone.now(),
        "modified_time": timezone.now(),
        "jobs": jobs,
        "results": results,
        "boxnames": boxnames,
        "latest_posts": latest_posts,
    }
    return render (request, "jobs/sarkariresult2025.html", context)


def job(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
    latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
    
    paginator = Paginator(jobs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    jobs = Job.objects.all()           
    mixed_objects = list(chain(jobs))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
    latest_posts = mixed_objects[:7]

    return render(request, "jobs/job.html", {"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates, "page_obj": page_obj, "latest_posts": latest_posts,})

def govtjobstoday(request):
    jobs = Job.objects.all().filter(status='published', is_active=True).order_by("-published_date")
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
    latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
    
    mixed_objects = list(chain(jobs))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    latest_posts = mixed_objects[:9]

    return render(request, 'jobs/govtjobstoday.html', {"jobs": jobs, "latest_results": latest_results, "latest_admitcards": 
    latest_admitcards, 'latest_govtupdates': latest_govtupdates, "latest_posts": latest_posts,})

def vacancy(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:9]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:9]  # latest 10 job
    jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")
    paginator = Paginator(jobs, 30, orphans=1) # प्रति पेज 20 jobs दिखाने के लिए (2 बहुत कम है)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    jobs = Job.objects.all()           
    mixed_objects = list(chain(jobs))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    latest_posts = mixed_objects[:10]

    return render(request, 'jobs/vacancy.html', {"jobs": jobs, "page_obj":page_obj,  "latest_posts": latest_posts, "latest_results": latest_results, "latest_admitcards": latest_admitcards})

def onlineform(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:8]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:8]  # latest 10 job
    jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")
    paginator = Paginator(jobs, 20, orphans=1) # प्रति पेज 20 jobs दिखाने के लिए (2 बहुत कम है)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    jobs = Job.objects.all()           
    mixed_objects = list(chain(jobs))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    latest_posts = mixed_objects[:13]

    return render(request, 'jobs/onlineform.html', {"jobs": jobs, "page_obj":page_obj, "latest_posts": latest_posts, "latest_results": latest_results, "latest_admitcards": latest_admitcards})

def sarkarinokri(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:8]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:8]  # latest 10 job
    jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")
    paginator = Paginator(jobs, 35, orphans=1) # प्रति पेज 35 jobs दिखाने के लिए (2 बहुत कम है)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    jobs = Job.objects.all()           
    mixed_objects = list(chain(jobs))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
    mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    latest_posts = mixed_objects[:7]

    return render(request, 'jobs/sarkarinokri.html', {"jobs": jobs, "page_obj":page_obj, "latest_posts": latest_posts, "latest_results": latest_results, "latest_admitcards": latest_admitcards})


# job slug & comment
def job_detail(request, slug):
    jobs = get_object_or_404(Job, slug=slug, is_active=True)
    latest_jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    
    if request.method == "POST":
        comment=JobComment()
        comment.user= request.user
        comment.job = jobs
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = JobComment.objects.filter(job=jobs).order_by('-created_at')
    comment_count = comments.count()
    return render(request, "jobs/job_details.html", {"jobs": jobs, "latest_jobs":latest_jobs, "latest_results": latest_results, "latest_admitcards": latest_admitcards, "comments": comments, "comment_count": comment_count})


# job copy
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Job
from .forms import JobForm

class JobPostCreateView(CreateView):
    model = Job
    form_class = JobForm
    template_name = "jobs/jobpost_form.html"  # <- folder ke hisab se
    success_url = reverse_lazy("job")         # <- URL name match

    def get(self, request, *args, **kwargs):
        self.object = None
        last = Job.objects.order_by('-id').first()
        if last:
            skip = {"id", "pk", "slug", "published_date"}
            field_names = [
                f.name for f in Job._meta.fields
                if f.editable and not f.auto_created and f.name not in skip
            ]
            data = {name: getattr(last, name) for name in field_names}
            form = self.form_class(instance=Job(**data))
        else:
            form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))



#sitemap.html----

def html_sitemap(request):
  jobs = Job.objects.all().order_by("-published_date")
  return render(request, 'mainfile/sitemap.html',{'jobs':jobs})



def result(request):
  results=Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]

  paginator = Paginator(results, 20, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  results = Result.objects.all()           
  mixed_objects = list(chain(results))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
  mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
  latest_posts = mixed_objects[:7]
  return render(request, 'results/result.html',{ "results": results, "latest_jobs": latest_jobs, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates, "page_obj":page_obj, "latest_posts": latest_posts,})


def sarkariresult2024(request):
  results=Result.objects.all().filter(status='published', is_active=True).order_by("-published_date")
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(results, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

      # 2) chain se sabko jod do
  mixed_objects = list(chain(results))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
  mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
  latest_posts = mixed_objects[:15]
  return render(request, 'results/sarkariresult2024.html',{ "results": results, "latest_jobs": latest_jobs, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates, "page_obj":page_obj, 'latest_posts': latest_posts})


def result_detail(request, slug):
    results = get_object_or_404(Result, slug=slug, is_active=True)
    latest_jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job

    if request.method == "POST":
        comment=ResultComment()
        comment.user= request.user
        comment.result = results
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = ResultComment.objects.filter(result=results).order_by('-created_at')
    comment_count = comments.count()
    return render(request, "results/result_details.html", {"results": results, "latest_jobs":latest_jobs, "latest_results": latest_results, "latest_admitcards": latest_admitcards, "comments": comments, "comment_count": comment_count})


def boardresult(request):
  qs = Result.objects.filter(is_active=True).filter(
        Q(category__icontains="board") | Q(category__icontains="board")
    ).order_by("-published_date")
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf boardresult category wali jobs lao
  boardresult = Result.objects.filter(
        category__icontains="board"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'results/boardresult.html',  {"posts": qs, "latest_jobs": latest_jobs, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates, "page_obj":page_obj,"latest_posts": boardresult,})


def itiresult(request):

  qs = Result.objects.filter(is_active=True).filter(
        Q(category__icontains="itiresult") | Q(category__icontains="itiresult")
    ).order_by("-published_date")
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  # Sirf itiresult category wali jobs lao
  jobs_itiresult = Result.objects.filter(
        category__icontains="itiresult"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'results/itiresult.html',  {"posts": qs, "latest_jobs": latest_jobs, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates, "page_obj":page_obj,"latest_posts": jobs_itiresult})

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Result
from .forms import ResultForm  # अगर आपने custom form बनाया है तो

class ResultPostCreateView(CreateView):
    model = Result
    form_class = ResultForm   # या फिर fields = "__all__" भी रख सकते हैं
    template_name = "results/resultPost_form.html"
    success_url = reverse_lazy("result")  # ये आपके list page ka URL name होना चाहिए

    def get(self, request, *args, **kwargs):
        self.object = None
        last = Result.objects.order_by('-id').first()
        if last:
            skip = {"id", "pk", "slug", "published_date"}  # अपनी model fields के अनुसार adjust करें
            field_names = [
                f.name for f in Result._meta.fields
                if f.editable and not f.auto_created and f.name not in skip
            ]
            data = {name: getattr(last, name) for name in field_names}
            form = self.form_class(instance=Result(**data))
        else:
            form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))





def admitcard(request):
  admitcards=Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]

  paginator = Paginator(admitcards, 20, orphans=1) # प्रति पेज 20 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  admitcards = Admitcard.objects.all()           
  mixed_objects = list(chain(admitcards))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
  mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
  latest_posts = mixed_objects[:7]
  return render(request, 'admitcards/admitcard.html', {"admitcards": admitcards, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_govtupdates': latest_govtupdates,'page_obj':page_obj, "latest_posts": latest_posts,})

def examdate(request):
  admitcards=Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]

  paginator = Paginator(admitcards, 20, orphans=1) # प्रति पेज 20 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  admitcards = Admitcard.objects.all()           
  mixed_objects = list(chain(admitcards))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
  mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
  latest_posts = mixed_objects[:5]
  return render(request, 'admitcards/examdate.html', {"admitcards": admitcards, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_govtupdates': latest_govtupdates,'page_obj':page_obj, "latest_posts": latest_posts,})

def sarkariexam(request):
  admitcards=Admitcard.objects.all().filter(status='published', is_active=True).order_by("-published_date")
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:4]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]

  paginator = Paginator(admitcards, 20, orphans=1) # प्रति पेज 20 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  admitcards = Admitcard.objects.all()           
  mixed_objects = list(chain(admitcards))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
  mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
  latest_posts = mixed_objects[:4]
  return render(request, 'admitcards/sarkariexam.html', {"admitcards": admitcards, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_govtupdates': latest_govtupdates,'page_obj':page_obj, "latest_posts": latest_posts,})

def admitcard_detail(request, slug):
    admitcards = get_object_or_404(Admitcard, slug=slug, is_active=True)
    latest_jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 5 job
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 5 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 5 job

    if request.method == "POST":
        comment=AdmitcardComment()
        comment.user= request.user
        comment.admitcard = admitcards
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = AdmitcardComment.objects.filter(admitcard=admitcards).order_by('-created_at')
    comment_count = comments.count()

    return render(request, "admitcards/admitcard_details.html", {"admitcards": admitcards, "latest_jobs":latest_jobs, "latest_results": 
    latest_results, "latest_admitcards": latest_admitcards, "comments": comments, "comment_count": comment_count})


from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Admitcard
from .forms import AdmitcardForm  # अगर आपने custom form बनाया है तो

class AdmitcardPostCreateView(CreateView):
    model = Admitcard
    form_class = AdmitcardForm   # या फिर fields = "__all__" भी रख सकते हैं
    template_name = "admitcards/admitcardPost_form.html"
    success_url = reverse_lazy("result")  # ये आपके list page ka URL name होना चाहिए

    def get(self, request, *args, **kwargs):
        self.object = None
        last = Admitcard.objects.order_by('-id').first()
        if last:
            skip = {"id", "pk", "slug", "published_date"}  # अपनी model fields के अनुसार adjust करें
            field_names = [
                f.name for f in Admitcard._meta.fields
                if f.editable and not f.auto_created and f.name not in skip
            ]
            data = {name: getattr(last, name) for name in field_names}
            form = self.form_class(instance=Admitcard(**data))
        else:
            form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))



def govtupdates(request):
  govtupdates=Govtupdate.objects.all().filter(status='published', is_active=True).order_by("-published_date")
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]

  paginator = Paginator(govtupdates, 20, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)


  updates = Govtupdate.objects.all()
    # 2) chain se sabko jod do
  mixed_objects = list(chain(updates))
    # 3) sabko created_at ke hisaab se sort kar do (naya sabse upar)
  mixed_objects = sorted(
        mixed_objects,
        key=lambda obj: obj.published_date,
        reverse=True
    )
    # 4) agar 20 ya 30 hi dikhane hain:
  latest_posts = mixed_objects[:15]
  return render(request, 'govtupdates/govtupdates.html', {"govtupdates":govtupdates, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_admitcards': latest_admitcards, 'page_obj':page_obj, "latest_posts": latest_posts,})

def govt_update_detail(request, slug):
  govtupdates = get_object_or_404(Govtupdate, slug=slug, is_active=True)
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 5 job
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 5 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 5 job

  if request.method == "POST":
        comment=GovtupdateComment()
        comment.user= request.user
        comment.govtupdate = govtupdates
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

  comments = GovtupdateComment.objects.filter(govtupdate=govtupdates).order_by('-created_at')
  comment_count = comments.count()

  return render(request, 'govtupdates/govtupdates_details.html', {"govtupdates":govtupdates, "latest_jobs":latest_jobs, "latest_results": latest_results, "latest_admitcards": latest_admitcards, "comments": comments, "comment_count": comment_count})

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Govtupdate
from .forms import GovtupdateForm  # अगर आपने custom form बनाया है तो

class GovtupdatePostCreateView(CreateView):
    model = Govtupdate
    form_class = GovtupdateForm   # या फिर fields = "__all__" भी रख सकते हैं
    template_name = "govtupdates/govtupdatePost_form.html"
    success_url = reverse_lazy("govtupdates")  # ये आपके list page ka URL name होना चाहिए

    def get(self, request, *args, **kwargs):
        self.object = None
        last = Govtupdate.objects.order_by('-id').first()
        if last:
            skip = {"id", "pk", "slug", "published_date"}  # अपनी model fields के अनुसार adjust करें
            field_names = [
                f.name for f in Govtupdate._meta.fields
                if f.editable and not f.auto_created and f.name not in skip
            ]
            data = {name: getattr(last, name) for name in field_names}
            form = self.form_class(instance=Govtupdate(**data))
        else:
            form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))



def admission(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]

  qs = Govtupdate.objects.filter(is_active=True).filter(
        Q(category__icontains="admission") | Q(category__icontains="admission")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  # Sirf admission category wali jobs lao
  jobs_admission = Govtupdate.objects.filter(
        category__icontains="admission"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'govtupdates/admission.html',  {"posts": qs, "page_obj":page_obj, "latest_posts": jobs_admission, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_admitcards': latest_admitcards,})

def answerkey(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  qs = Govtupdate.objects.filter(is_active=True).filter(
        Q(category__icontains="answerkey") | Q(category__icontains="answerkey")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
 
   # Sirf answerkey category wali jobs lao
  jobs_answerkey = Govtupdate.objects.filter(
        category__icontains="answerkey"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'govtupdates/answerkey.html',  {"posts": qs, "page_obj":page_obj, "latest_posts": jobs_answerkey, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_admitcards': latest_admitcards,})

def sarkariyojna(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  qs = Govtupdate.objects.filter(is_active=True).filter(
        Q(category__icontains="sarkariyojana") | Q(category__icontains="sarkariyojna")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf sarkariyojana category wali jobs lao
  jobs_sarkariyojana = Govtupdate.objects.filter(
        category__icontains="sarkariyojana"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'govtupdates/sarkariyojna.html',  {"posts": qs, "page_obj":page_obj, "latest_posts": jobs_sarkariyojana, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_admitcards': latest_admitcards,})

def scholarship(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  qs = Govtupdate.objects.filter(is_active=True).filter(
        Q(category__icontains="scholarship") | Q(category__icontains="scholarship")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
   # Sirf scholarship category wali jobs lao
  jobs_scholarship = Govtupdate.objects.filter(
        category__icontains="scholarship"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'govtupdates/scholarship.html',  {"posts": qs, "page_obj":page_obj, "latest_posts": jobs_scholarship, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_admitcards': latest_admitcards,})

def syllabus(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:3]
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  qs = Govtupdate.objects.filter(is_active=True).filter(
        Q(category__icontains="syllabus") | Q(category__icontains="syllabus")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf syllabus category wali jobs lao
  jobs_syllabus = Govtupdate.objects.filter(
        category__icontains="syllabus"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'govtupdates/syllabus.html',  {"posts": qs, "page_obj":page_obj, "latest_posts": jobs_syllabus, "latest_jobs": latest_jobs, "latest_results": latest_results, 'latest_admitcards': latest_admitcards,})





def contact(request):
 latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
 latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
 return render(request, 'mainfile/contact.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

def about(request):
 latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
 latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
 return render(request, 'mainfile/about.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards,"today": date.today()})


def disclaimer(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
  return render(request, 'mainfile/disclaimer.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

def PrivacyPolicy(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
  return render(request, 'mainfile/PrivacyPolicy.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards,"today": date.today()})

def dmca(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
  return render(request, 'mainfile/dmca.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards, "today": date.today()})

def hyperlinkpolicy(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    return render(request, "mainfile/hyperlinkpolicy.html", {"latest_results": latest_results, "latest_admitcards": latest_admitcards})


def TermsConditions(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    return render(request, 'mainfile/TermsConditions.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards,  "today": date.today()}) 

def editorialpolicy(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    return render(request, 'mainfile/editorialpolicy.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

def FactCheckingPolicy(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    return render(request, 'mainfile/FactCheckingPolicy.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

def AdvertisingPolicy(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    return render(request, 'mainfile/AdvertisingPolicy.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

def grievanceofficer(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    return render(request, 'mainfile/grievanceofficer.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

def cookiepolicy(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    return render(request, 'mainfile/cookiepolicy.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

#  Authors 

def MeetTeam(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:7]  # latest 11 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:8]  # latest 11 job
  return render(request, 'author/MeetTeam.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

def arvind(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]  # latest 11 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]  # latest 11 job
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="arvind") | Q(category__icontains="arvind")
    ).order_by("-published_date")
  paginator = Paginator(qs, 22, orphans=1) 
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'author/arvind-author.html',  {"posts": qs, 'page_obj': page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards})

def priya(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]  # latest 11 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:7]  # latest 11 job
  qs = Govtupdate.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="priya") | Q(category__icontains="priya")
    ).order_by("-published_date")
  paginator = Paginator(qs, 22, orphans=1) 
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'author/PriyaPatel-author.html',{"posts": qs, 'page_obj': page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards})

def founder(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]  # latest 11 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]  # latest 11 job
  return render(request, 'author/founder.html',{"latest_results": latest_results, "latest_admitcards": latest_admitcards})

# all state government 

def all_state_govt_job(request):
 latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
 latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
 latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:15]  # latest 10 job
 return render(request, 'state/allstategovjob.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards,"latest_jobs":latest_jobs,})

def AndhraPradesh(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="andhrapradesh") | Q(category__icontains="andhrapradesh")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf andhrapradesh category wali jobs lao
  jobs_andhrapradesh = Job.objects.filter(
        category__icontains="andhrapradesh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/AndhraPradeshjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_andhrapradesh,})

def ArunachalPradesh(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="arunachalpradesh") | Q(category__icontains="arunachalpradesh")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf arunachalpradesh category wali jobs lao
  jobs_arunachalpradesh = Job.objects.filter(
        category__icontains="arunachalpradesh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/ArunachalPradeshjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_arunachalpradesh,})

def Assam(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="assam") | Q(category__icontains="assam")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf assam category wali jobs lao
  jobs_assam = Job.objects.filter(
        category__icontains="assam"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Assamjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_assam,})

def Bihar(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="bihar") | Q(category__icontains="bihar")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf bihar category wali jobs lao
  jobs_bihar = Job.objects.filter(
        category__icontains="bihar"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Biharjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_bihar,})

def Chhattisgarh(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="chhattisgarh") | Q(category__icontains="chhattisgarh")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf chhattisgarh category wali jobs lao
  jobs_chhattisgarh = Job.objects.filter(
        category__icontains="chhattisgarh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Chhattisgarhjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_chhattisgarh,})

def Delhi(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="delhi") | Q(category__icontains="delhi")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf delhi category wali jobs lao
  jobs_delhi = Job.objects.filter(
        category__icontains="delhi"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Delhijob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_delhi,})

def Goa(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="goa") | Q(category__icontains="goa")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf goa category wali jobs lao
  jobs_goa = Job.objects.filter(
        category__icontains="goa"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Goajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_goa,})

def Gujarat(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="gujarat") | Q(category__icontains="gujarat")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf gujarat category wali jobs lao
  jobs_gujarat = Job.objects.filter(
        category__icontains="gujarat"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Gujaratjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_gujarat,})

def Haryana(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="haryana") | Q(category__icontains="haryana")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf haryana category wali jobs lao
  jobs_haryana = Job.objects.filter(
        category__icontains="haryana"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Haryanajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_haryana,})

def HimachalPradesh(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="himachalpradesh") | Q(category__icontains="himachalpradesh")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf himachalpradesh category wali jobs lao
  jobs_himachalpradesh = Job.objects.filter(
        category__icontains="himachalpradesh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/HimachalPradesh.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_himachalpradesh,})

def JammuKashmir(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="jammukashmir") | Q(category__icontains="jammukashmir")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf jammukashmir category wali jobs lao
  jobs_jammukashmir = Job.objects.filter(
        category__icontains="jammukashmir"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/JammuKashmirjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_jammukashmir,})

def Jharkhand(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="jharkhand") | Q(category__icontains="jharkhand")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf jharkhand category wali jobs lao
  jobs_jharkhand = Job.objects.filter(
        category__icontains="jharkhand"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Jharkhandjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_jharkhand,})

def Karnataka(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="karnataka") | Q(category__icontains="karnataka")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf karnataka category wali jobs lao
  jobs_karnataka = Job.objects.filter(
        category__icontains="karnataka"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Karnatakajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_karnataka,})

def Kerala(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="kerala") | Q(category__icontains="kerala")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf kerala category wali jobs lao
  jobs_kerala = Job.objects.filter(
        category__icontains="kerala"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Keralajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_kerala,})

def MadhyaPradesh(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="madhyapradesh") | Q(category__icontains="madhyapradesh")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf madhyapradesh category wali jobs lao
  jobs_madhyapradesh = Job.objects.filter(
        category__icontains="madhyapradesh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/MadhyaPradeshjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_madhyapradesh,} )

def Maharashtra(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="maharashtra") | Q(category__icontains="maharashtra")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf maharashtra category wali jobs lao
  jobs_maharashtra = Job.objects.filter(
        category__icontains="maharashtra"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Maharashtrajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_maharashtra,} )

def Manipur(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="manipur") | Q(category__icontains="manipur")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf manipur category wali jobs lao
  jobs_manipur = Job.objects.filter(
        category__icontains="manipur"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Manipurjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_manipur,} )

def Meghalaya(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="meghalaya") | Q(category__icontains="meghalaya")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf meghalaya category wali jobs lao
  jobs_meghalaya = Job.objects.filter(
        category__icontains="meghalaya"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Meghalayajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_meghalaya,} )

def Mizoram(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="mizoram") | Q(category__icontains="mizoram")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf mizoram category wali jobs lao
  jobs_mizoram = Job.objects.filter(
        category__icontains="mizoram"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Mizoramjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_mizoram,} )

def Nagaland(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="nagaland") | Q(category__icontains="nagaland")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)


   # Sirf nagaland category wali jobs lao
  jobs_nagaland = Job.objects.filter(
        category__icontains="nagaland"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Nagalandjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_nagaland,} )

def Odisha(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="odisha") | Q(category__icontains="odisha")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf odisha category wali jobs lao
  jobs_odisha = Job.objects.filter(
        category__icontains="odisha"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Odishajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_odisha,} )

def Punjab(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="punjab") | Q(category__icontains="punjab")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf punjab category wali jobs lao
  jobs_punjab = Job.objects.filter(
        category__icontains="punjab"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Punjabjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_punjab,} )

def Rajasthan(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="rajasthan") | Q(category__icontains="rajasthan")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf rajasthan category wali jobs lao
  jobs_rajasthan = Job.objects.filter(
        category__icontains="rajasthan"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Rajasthanjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_rajasthan,} )

def Sikkim(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="sikkim") | Q(category__icontains="sikkim")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf sikkim category wali jobs lao
  jobs_sikkim = Job.objects.filter(
        category__icontains="sikkim"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Sikkimjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_sikkim,} )

def TamilNadu(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="tamilnadu") | Q(category__icontains="tamilnadu")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf tamilnadu category wali jobs lao
  jobs_tamilnadu = Job.objects.filter(
        category__icontains="tamilnadu"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/TamilNadujob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_tamilnadu,} )

def Telangana(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="telangana") | Q(category__icontains="telangana")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf telangana category wali jobs lao
  jobs_telangana = Job.objects.filter(
        category__icontains="telangana"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Telanganajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_telangana,} )

def Tripura(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="tripura") | Q(category__icontains="tripura")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf tripura category wali jobs lao
  jobs_tripura = Job.objects.filter(
        category__icontains="tripura"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Tripurajob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_tripura,} )

def upjob(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="up") | Q(category__icontains="up")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf upjob category wali jobs lao
  jobs_upjob = Job.objects.filter(
        category__icontains="up"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/upjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_upjob,} )

def Uttarakhand(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="uttarakhand") | Q(category__icontains="uttarakhand")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf uttarakhand category wali jobs lao
  jobs_uttarakhand = Job.objects.filter(
        category__icontains="uttarakhand"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Uttarakhandjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_uttarakhand,} )

def WestBengal(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="westbengal") | Q(category__icontains="westbengal")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf westbengal category wali jobs lao
  jobs_westbengal = Job.objects.filter(
        category__icontains="westbengal"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/WestBengal.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_westbengal,} )

def AndamanNicobar(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="andamannicobar") | Q(category__icontains="andamannicobar")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf andamannicobar category wali jobs lao
  jobs_andamannicobar = Job.objects.filter(
        category__icontains="andamannicobar"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/AndamanNicobar.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_andamannicobar,} )

def Chandigarh(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="chandigarh") | Q(category__icontains="chandigarh")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf chandigarh category wali jobs lao
  jobs_chandigarh = Job.objects.filter(
        category__icontains="chandigarh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Chandigarh.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_chandigarh,} )

def DadraNagarHaveli(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="dadranagarhaveli") | Q(category__icontains="dadranagarhaveli")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf dadranagarhaveli category wali jobs lao
  jobs_dadranagarhaveli = Job.objects.filter(
        category__icontains="dadranagarhaveli"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/DadraNagarHaveli.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_dadranagarhaveli,} )

def DamanDiu(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="damandiu") | Q(category__icontains="damandiu")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf damandiu category wali jobs lao
  jobs_damandiu = Job.objects.filter(
        category__icontains="damandiu"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/DamanDiu.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_damandiu,} )

def Ladakh(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="ladakh") | Q(category__icontains="ladakh")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf ladakh category wali jobs lao
  jobs_ladakh = Job.objects.filter(
        category__icontains="ladakh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Ladakh.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_ladakh,} )

def Lakshadweep(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="lakshadweep") | Q(category__icontains="lakshadweep")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf lakshadweep category wali jobs lao
  jobs_lakshadweep = Job.objects.filter(
        category__icontains="lakshadweep"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Lakshadweep.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_lakshadweep,} )

def Puducherry(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="puducherry") | Q(category__icontains="puducherry")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf puducherry category wali jobs lao
  jobs_puducherry = Job.objects.filter(
        category__icontains="puducherry"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'state/Puducherry.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_puducherry,} )


# Central Government jobs


def CentralGovtjob(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="centraljob") | Q(category__icontains="centralgovtjob")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:3]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:4]
  paginator = Paginator(qs, 1, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf centralgovt category wali jobs lao
  jobs_centralgovt = Job.objects.filter(
        category__icontains="centraljob"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:9]
  return render(request, 'centralgovtjob.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_centralgovt,})

# qualification

def all_education(request):
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    return render(request, "qualification/alleducation.html", {"latest_results": latest_results, "latest_admitcards": latest_admitcards,"latest_jobs":latest_jobs})


def EighthPassJob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="8th") | Q(category__icontains="8TH")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)


   # Sirf 8th category wali jobs lao
  jobs_8th = Job.objects.filter(
        category__icontains="8th"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]


  return render(request, 'qualification/EighthPassJob.html',  {"posts": qs , "page_obj":page_obj,"latest_posts": jobs_8th,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )


def tenthjob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="10th") | Q(category__icontains="10th")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)


   # Sirf 10th category wali jobs lao
  jobs_10th = Job.objects.filter(
        category__icontains="10th"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]


  return render(request, 'qualification/10thjob.html',  {"posts": qs , "page_obj":page_obj,"latest_posts": jobs_10th,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def twellthjob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="12th") | Q(category__icontains="12th")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf 10th category wali jobs lao
  jobs_10th = Job.objects.filter(
        category__icontains="12th"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'qualification/12thjob.html',  {"posts": qs , "page_obj":page_obj,"latest_posts": jobs_10th,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def graduationjob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="graduation") | Q(category__icontains="graduation")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf graduation category wali jobs lao
  jobs_graduation = Job.objects.filter(
        category__icontains="graduation"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'qualification/graduation.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_graduation,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def postgraduationjob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="postgraduation") | Q(category__icontains="postgraduation")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf postgraduation category wali jobs lao
  jobs_postgraduation = Job.objects.filter(
        category__icontains="postgraduation"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'qualification/postgraduation.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_postgraduation,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def diploma_jobs(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="diploma") | Q(category__icontains="diploma")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf diplomajobs category wali jobs lao
  jobs_diplomajobs = Job.objects.filter(
        category__icontains="diploma"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'qualification/diplomajobs.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_diplomajobs,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def engineering_jobs(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="engineering") | Q(category__icontains="engineering")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf engineering category wali jobs lao
  jobs_engineering = Job.objects.filter(
        category__icontains="engineering"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'qualification/engineeringjobs.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_engineering,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def medical_jobs(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="medical") | Q(category__icontains="medical")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf medical category wali jobs lao
  jobs_medical = Job.objects.filter(
        category__icontains="medical"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'qualification/medicaljobs.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_medical,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def itigovtjobs(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="iti") | Q(category__icontains="iti")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf iti category wali jobs lao
  jobs_iti = Job.objects.filter(
        category__icontains="iti"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'qualification/itigovtjobs.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_iti,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def apprenticejob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="apprentice") | Q(category__icontains="apprentice")
    ).order_by("-published_date")
  paginator = Paginator(qs, 10, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

     # Sirf apprenticejob category wali jobs lao
  jobs_apprenticejob = Job.objects.filter(
        category__icontains="apprentice"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'qualification/apprenticejob.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_apprenticejob,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )



# category jobs

def allcategoryjobs(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]  # latest 10 job
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]  # latest 10 job
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by("-published_date")[:15]  # latest 10 job
  return render(request, 'category/allcategoryjobs.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards,"latest_jobs":latest_jobs,})

def railwayjob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="railway") | Q(category__icontains="railway")
    ).order_by("-published_date")
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf railway category wali jobs lao
  jobs_railway = Job.objects.filter(
        category__icontains="railway"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'category/railwayjob.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_railway,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )


def bankjob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="bank") | Q(category__icontains="bank")
    ).order_by("-published_date")
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf bank category wali jobs lao
  jobs_bank = Job.objects.filter(
        category__icontains="bank"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:7]
  return render(request, 'category/bankjob.html', {"posts": qs,"page_obj":page_obj, "latest_posts": jobs_bank,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,})

def defensejob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="defense") | Q(category__icontains="defense")
    ).order_by("-published_date")
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf defense category wali jobs lao
  jobs_defense = Job.objects.filter(
        category__icontains="defense"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'category/defensejob.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_defense,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )


def policejobs(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:10]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="police") | Q(category__icontains="police")
    ).order_by("-published_date")
  paginator = Paginator(qs, 30, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf defense category wali jobs lao
  jobs_defense = Job.objects.filter(
        category__icontains="defense"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'category/policejobs.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_defense, "latest_jobs": latest_jobs, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )


def uppolice(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:10]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="uppolice") | Q(category__icontains="defense")
    ).order_by("-published_date")
  paginator = Paginator(qs, 30, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf defense category wali jobs lao
  jobs_defense = Job.objects.filter(
        category__icontains="defense"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:6]
  return render(request, 'category/uppolice.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_defense, "latest_jobs": latest_jobs, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def delhipolice(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:10]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="delhipolice") | Q(category__icontains="Delhipolice")
    ).order_by("-published_date")
  paginator = Paginator(qs, 30, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf defense category wali jobs lao
  jobs_defense = Job.objects.filter(
        category__icontains="defense"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:6]
  return render(request, 'category/delhipolice.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_defense, "latest_jobs": latest_jobs, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )

def rajasthanpolice(request):
  latest_jobs = Job.objects.filter(status='published', is_active=True).order_by('-published_date')[:10]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="rajasthanpolice") | Q(category__icontains="rajasthanpolice")
    ).order_by("-published_date")
  paginator = Paginator(qs, 30, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf defense category wali jobs lao
  jobs_defense = Job.objects.filter(
        category__icontains="defense"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:6]
  return render(request, 'category/rajasthanpolice.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_defense, "latest_jobs": latest_jobs, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,} )




def sscjob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="ssc") | Q(category__icontains="ssc", )
    ).order_by("-published_date")
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf ssc category wali jobs lao
  jobs_ssc = Job.objects.filter(
        category__icontains="ssc"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:6]
  return render(request, 'category/sscjob.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_ssc,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,})

def upscjob(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:12]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="upsc") | Q(category__icontains="upsc")
    ).order_by("-published_date")
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf upsc category wali jobs lao
  jobs_upsc = Job.objects.filter(
        category__icontains="upsc"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'category/upscjob.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_upsc,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,})

def government_teacher_jobs(request):
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="teacher") | Q(category__icontains="teacher")
    ).order_by("-published_date")
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 results दिखाने के लिए  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
    # Sirf teacher category wali jobs lao
  jobs_teacher = Job.objects.filter(
        category__icontains="teacher"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:10]
  return render(request, 'category/governmentteacherjobs.html',  {"posts": qs, "page_obj":page_obj,"latest_posts": jobs_teacher,"latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,})


# singup login

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if not uname or not email or not pass1 or not pass2:
            messages.error(request, "All fields are required.")
            return redirect('signup')
        

        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists. Try a different one.")
            return redirect('signup')  # या उसी पेज पर वापस रेंडर करें

        if User.objects.filter(email=email).exists():                   
            messages.error(request, "Email already exists")               
            return redirect('signup')  # या उसी पेज पर वापस रेंडर करें      

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        # 4) ✅ Create the user first
        user = User.objects.create_user(username=uname, email=email, password=pass1)

        
        # ✅ Auto-login after signup
        authed = authenticate(request, username=uname, password=pass1)
        if authed is not None:
            login(request, authed)
        return redirect('home')
    
    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    
    return render(request, 'singup/singup.html', {"latest_results": latest_results, "latest_admitcards": latest_admitcards})

def LogoutPage(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')   # ✅ logout के बाद signup पेज पर


from . forms import CreateUserForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm  # LoginForm के लिए
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def LoginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()           # ✅ form से user मिल जाता है
            auth_login(request, user)        # ✅ alias इस्तेमाल करें
            nxt = request.GET.get("next") or request.POST.get("next")
            return redirect(nxt or "home")
        messages.error(request, "Invalid credentials.")
        return redirect("login")
    else:
        form = AuthenticationForm(request)

    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]  # latest 10 job

    return render(request, "singup/login.html", {"latest_results": latest_results, "latest_admitcards": latest_admitcards, "form": form, "next": request.GET.get("next", "")})




# views.py  search bar ke leye--
from datetime import datetime
from django.shortcuts import render
from django.db.models import Q
from django.utils.timezone import make_aware, get_current_timezone

# 👇 अपने असली मॉडल import करें
from .models import Job, Result, Admitcard, Govtupdate

# ---------- CONFIG: अपने field names यहाँ एडजस्ट करें ----------
# Note: सभी models में date field "published_date" माना है (आपके Job में यही है)
# अगर किसी model में अलग नाम है, नीचे उसी key में बदल दें.
MODEL_CONFIG = {
    "job": {
        "model": Job,
        "date_field": "published_date",  # ✅ FIX
        # आपकी schema के हिसाब से useful searchable fields
        "content_fields": [
            "title", "description", "selection_process",
            "eligibillity_criteria", "important_dates", "vacancy_details",
            "How_to_appply", "extra_information", "tag"
        ],
        "category_field": "category",
        "url_fallback": lambda obj: getattr(obj, "get_absolute_url", None)() if hasattr(obj, "get_absolute_url")
                          else f"/latest-jobs/{getattr(obj,'slug',obj.pk)}/",
        "snippet_fields": ["description", "selection_process", "important_dates"],
        "type_label": "job",
    },
    "result": {
        "model": Result,
        "date_field": "published_date",  # ✅ change here if different
        "content_fields": ["title", "description", "extra_information", "tag"],
        "category_field": "category",
        "url_fallback": lambda obj: getattr(obj, "get_absolute_url", None)() if hasattr(obj, "get_absolute_url")
                          else f"/results/{getattr(obj,'slug',obj.pk)}/",
        "snippet_fields": ["description"],
        "type_label": "result",
    },
    "admitcard": {
        "model": Admitcard,
        "date_field": "published_date",  # ✅ change here if different
        "content_fields": ["title", "description", "important_dates", "tag"],
        "category_field": "category",
        "url_fallback": lambda obj: getattr(obj, "get_absolute_url", None)() if hasattr(obj, "get_absolute_url")
                          else f"/admit-card/{getattr(obj,'slug',obj.pk)}/",
        "snippet_fields": ["description", "important_dates"],
        "type_label": "admit card",
    },
    "govtupdate": {
        "model": Govtupdate,
        "date_field": "published_date",  # ✅ change here if different
        "content_fields": ["title","description", "extra_information", "tag"],
        "category_field": "category",
        "url_fallback": lambda obj: getattr(obj, "get_absolute_url", None)() if hasattr(obj, "get_absolute_url")
                          else f"/govt-updates/{getattr(obj,'slug',obj.pk)}/",
        "snippet_fields": ["description"],
        "type_label": "govtupdate",
    },
}

# ---------- Helpers ----------

def _get_attr_any(obj, fields, default=""):
    """पहला उपलब्ध attribute value दे देता है (जो truthy हो)."""
    for f in fields:
        if hasattr(obj, f):
            val = getattr(obj, f)
            if val:
                return val
    return default

def _get_date(obj, date_field):
    """date/datetime normalize."""
    if not date_field or not hasattr(obj, date_field):
        return None
    val = getattr(obj, date_field)
    return val

def _build_item(obj, cfg, q_tokens):
    """Model object -> unified dict (title, url, category, type, date, snippet, score)."""
    title = _get_attr_any(obj, ["title", "name"]) or str(obj)
    url = cfg["url_fallback"](obj)

    category = None
    cat_field = cfg.get("category_field")
    if cat_field and hasattr(obj, cat_field):
        category = getattr(obj, cat_field) or None

    date_val = _get_date(obj, cfg.get("date_field"))

    # snippet
    raw_text = _get_attr_any(obj, cfg.get("snippet_fields", [])) or ""
    snippet = raw_text.strip()
    if len(snippet) > 260:
        snippet = snippet[:257].rstrip() + "..."

    # relevance score (simple heuristic)
    hay_title = (title or "").lower()
    hay_body = (raw_text or "").lower()
    score = 0.0
    for t in q_tokens:
        if t in hay_title:
            score += 5
        if t in hay_body:
            score += 2
        if hay_title.startswith(t):
            score += 1
    # recency boost (last 30 days ~ +1.5)
    if date_val:
        try:
            now = datetime.now(get_current_timezone())
        except Exception:
            now = datetime.now()
        try:
            dt = date_val
            # if naive, make aware
            if hasattr(now, "tzinfo") and now.tzinfo and getattr(dt, "tzinfo", None) is None:
                dt = make_aware(dt, now.tzinfo)  # best-effort
            days_old = (now - dt).days
            if days_old <= 30:
                score += 1.5
        except Exception:
            pass

    return {
        "title": title,
        "url": url,
        "category": category,
        "type": cfg["type_label"],
        "date": date_val,
        "snippet": snippet,
        "score": score,
    }

def _tokenize(q):
    return [t for t in (q or "").lower().strip().replace("-", " ").split() if t]


# ---------- The Search View ----------
def search(request):
    """
    GET params:
      q            -> search text
      category     -> filter (optional)
      type         -> one of: job, result, admitcard, govtupdate (optional)
      date_from    -> YYYY-MM-DD (optional)
      date_to      -> YYYY-MM-DD (optional)
      sort         -> relevance | date_desc | date_asc (default: relevance)
      page         -> int (default: 1)
      per_page     -> int (default: 10)
    """
    q = (request.GET.get("q") or "").strip()
    category = (request.GET.get("category") or "").strip()
    content_type = (request.GET.get("type") or "").strip().lower()  # job/result/admitcard/govtupdate
    date_from = (request.GET.get("date_from") or "").strip()
    date_to = (request.GET.get("date_to") or "").strip()
    sort = (request.GET.get("sort") or "relevance").strip().lower()
    page = int(request.GET.get("page") or 1)
    per_page = int(request.GET.get("per_page") or 20)

    q_tokens = _tokenize(q)

    # Which models to search?
    type_keys = [content_type] if content_type in MODEL_CONFIG else list(MODEL_CONFIG.keys())

    results = []

    for key in type_keys:
        cfg = MODEL_CONFIG[key]
        Model = cfg["model"]
        qs = Model.objects.all()

        # Category filter (if model में category field exist)
        cat_field = cfg.get("category_field")
        if category and cat_field:
            qs = qs.filter(**{f"{cat_field}__icontains": category})

        # Date range (works for DateField and DateTimeField)
        date_field = cfg.get("date_field")
        if date_field:
            if date_from:
                qs = qs.filter(**{f"{date_field}__gte": date_from})
            if date_to:
                qs = qs.filter(**{f"{date_field}__lte": date_to})

        # Text search across content_fields with OR
        if q_tokens:
            content_q = Q()
            for fld in cfg.get("content_fields", []):
                content_q |= Q(**{f"{fld}__icontains": q})
            if not content_q.children:
                content_q = Q(title__icontains=q)
            qs = qs.filter(content_q)

        # Build unified items & score
        for obj in qs:
            results.append(_build_item(obj, cfg, q_tokens))

    # Sorting
    if sort == "date_desc":
        results.sort(key=lambda x: (x["date"] is not None, x["date"]), reverse=True)
    elif sort == "date_asc":
        results.sort(key=lambda x: (x["date"] is None, x["date"]))
    else:
        # default relevance, then date desc
        results.sort(key=lambda x: (x["score"], x["date"] or datetime.min), reverse=True)

    # Pagination
    paginator = Paginator(results, per_page)
    page_obj = paginator.get_page(page)

    latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]  # latest 10 job
    latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:7]  # latest 10 job

    context = {
        "q": q,
        "category": category,
        "content_type": content_type,
        "date_from": date_from,
        "date_to": date_to,
        "sort": sort,
        "page_obj": page_obj,
        "total": paginator.count,
        "page": page_obj.number,
        "pages": paginator.num_pages,
        "per_page": per_page,
        # summary string for UI
        "results_start": (page_obj.start_index() if paginator.count else 0),
        "results_end": (page_obj.end_index() if paginator.count else 0),
        "latest_results": latest_results, "latest_admitcards": latest_admitcards
    }
    return render(request, "mainfile/search.html", context)





# sitemap.xml
from django.http import HttpResponse
from django.utils import timezone

def sitemap_index_custom(request):
    # आज की तारीख (YYYY-MM-DD)
    lastmod = timezone.now().date().isoformat()

    # Absolute URLs बनाएं (slash की गड़बड़ से बचने के लिए rstrip)
    index_url = request.build_absolute_uri("/pages-sitemap.xml/").rstrip("/")
    post_url  = request.build_absolute_uri("/posts-sitemap.xml/").rstrip("/")
    news_url  = request.build_absolute_uri("/news-sitemap.xml/").rstrip("/")

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>{index_url}</loc>
    <lastmod>{lastmod}</lastmod>
  </sitemap>
  <sitemap>
    <loc>{post_url}</loc>
    <lastmod>{lastmod}</lastmod>
  </sitemap>
   <sitemap>
    <loc>{news_url}</loc>
    <lastmod>{lastmod}</lastmod>
  </sitemap>
</sitemapindex>'''
    return HttpResponse(xml, content_type="application/xml")



















#  latest new 
import re
from datetime import datetime, date
from urllib.parse import urljoin




PLACEHOLDER = "https://via.placeholder.com/160x120.png?text=News"

# -------- date patterns (English months) --------
DATE_PATTERNS = [
    r"\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+(\d{4})\b",          # 08 Nov 2025
    r"\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
    r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b",                                                    # 08/11/2025 or 08-11-2025
    r"\b(\d{4})-(\d{2})-(\d{2})\b",                                                              # 2025-11-08
]

MONTH_MAP = {
    "jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"sept":9,"oct":10,"nov":11,"dec":12
}

# -------- which field me HTML dates ho sakti hain --------
HTML_DATE_FIELDS = ["important_dates", "content", "description", "body", "details"]

# -------- image helpers (same as pehle wale) --------
MODEL_IMAGE_FIELDS = {
    Job:        ["image", "thumbnail", "thumb", "featured_image", "logo", "poster", "job_image", "job_photo"],
    Result:     ["image", "thumbnail", "thumb", "featured_image", "poster", "result_image"],
    Admitcard:  ["image", "thumbnail", "thumb", "featured_image", "poster", "admit_image"],
    Govtupdate: ["image", "thumbnail", "thumb", "featured_image", "poster", "update_image"],
}
MODEL_HTML_FIELDS = {
    Job:        ["content", "description", "body", "details", "important_dates"],
    Result:     ["content", "description", "body", "details", "important_dates"],
    Admitcard:  ["content", "description", "body", "details", "important_dates"],
    Govtupdate: ["content", "description", "body", "details", "important_dates"],
}

IMG_SRC_REGEX = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

def _first_attr(obj, names):
    for n in names:
        if hasattr(obj, n):
            v = getattr(obj, n)
            if v:
                return v
    return None

def _build_abs(request, url_or_path: str) -> str | None:
    if not url_or_path:
        return None
    u = str(url_or_path).strip()
    if u.startswith(("http://", "https://", "//")):
        return u
    media_prefix = (settings.MEDIA_URL or "/media/").rstrip("/") + "/"
    if u.startswith(media_prefix) or u.startswith("/media/"):
        return request.build_absolute_uri(u)
    joined = urljoin(settings.MEDIA_URL or "/media/", u.lstrip("/"))
    return request.build_absolute_uri(joined)

def _extract_img_from_html(request, obj):
    html_text = _first_attr(obj, MODEL_HTML_FIELDS.get(type(obj), []))
    if not isinstance(html_text, str):
        return None
    m = IMG_SRC_REGEX.search(html_text)
    return _build_abs(request, m.group(1)) if m else None

def _thumb_url(request, obj):
    for field in MODEL_IMAGE_FIELDS.get(type(obj), []):
        if hasattr(obj, field):
            val = getattr(obj, field)
            if not val:
                continue
            if hasattr(val, "url"):
                try:
                    return _build_abs(request, val.url)
                except Exception:
                    pass
            if isinstance(val, str):
                return _build_abs(request, val)
    for meth in ("get_image_url", "get_thumbnail_url"):
        if hasattr(obj, meth):
            try:
                mval = getattr(obj, meth)()
                if mval:
                    return _build_abs(request, mval)
            except Exception:
                pass
    return _extract_img_from_html(request, obj)

# ---------- DATE PARSER from HTML (important_dates etc.) ----------
def _parse_dates_from_text(txt: str):
    if not txt or not isinstance(txt, str):
        return []

    found = []

    # 1) "08 Nov 2025" / "08 November 2025"
    for pat in DATE_PATTERNS[:2]:
        for m in re.finditer(pat, txt, re.IGNORECASE):
            d = int(m.group(1))
            mon = m.group(2).lower()
            y = int(m.group(3))
            # short or long month names:
            if mon.isalpha():
                mon_num = MONTH_MAP.get(mon[:4].replace("t","t")) or MONTH_MAP.get(mon[:3]) or MONTH_MAP.get(mon)
            else:
                mon_num = None
            if mon_num:
                try:
                    found.append(date(y, mon_num, d))
                except ValueError:
                    pass

    # 2) "08/11/2025" or "08-11-2025"  -> assume DD/MM/YYYY (govt format)
    for m in re.finditer(DATE_PATTERNS[2], txt):
        d = int(m.group(1)); mon = int(m.group(2)); y = int(m.group(3))
        # if looks like MM/DD/YYYY (rare in India) you can flip if needed
        try:
            found.append(date(y, mon, d))
        except ValueError:
            pass

    # 3) "2025-11-08"
    for m in re.finditer(DATE_PATTERNS[3], txt):
        y = int(m.group(1)); mon = int(m.group(2)); d = int(m.group(3))
        try:
            found.append(date(y, mon, d))
        except ValueError:
            pass

    return found

def _pick_dt_from_html(obj):
    # Try important_dates/content fields in priority
    for field in HTML_DATE_FIELDS:
        if hasattr(obj, field):
            txt = getattr(obj, field)
            if not isinstance(txt, str):
                continue
            ds = _parse_dates_from_text(txt)
            if ds:
                # pick the latest date present in the text
                last = max(ds)
                # make aware datetime at 00:00 local
                dt = datetime(last.year, last.month, last.day)
                return timezone.make_aware(dt) if timezone.is_naive(dt) else dt
    return None

def _coerce_dt(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return timezone.make_aware(value) if timezone.is_naive(value) else value
    if isinstance(value, date):
        dt = datetime(value.year, value.month, value.day)
        return timezone.make_aware(dt)
    return None

# ---- add this EXACT name ----
DATE_FIELD_CANDIDATES = [
    "published_date",            # <-- your field
    "updated_at", "updated", "modified", "last_updated",
    "publish_date", "published_at", "posted_on", "post_date", "news_date",
    "created_at", "created", "created_on", "date",
]


def _pick_dt(obj):
    # 1) Try explicit date/datetime fields on model
    for f in DATE_FIELD_CANDIDATES:
        if hasattr(obj, f):
            dt = _coerce_dt(getattr(obj, f))
            if dt:
                return dt
    # 2) Parse from important_dates / content HTML
    return _pick_dt_from_html(obj)

def _title(obj):
    return _first_attr(obj, ["title", "name", "heading", "post_title"]) or "(Untitled)"

def _url(obj):
    if hasattr(obj, "get_absolute_url"):
        try:
            u = obj.get_absolute_url()
            if u:
                return u
        except Exception:
            pass
    return "#"








#education

from django.urls import reverse, NoReverseMatch

PLACEHOLDER = "https://via.placeholder.com/160x120.png?text=News"

DATE_PATTERNS = [
    r"\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+(\d{4})\b",
    r"\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
    r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b",
    r"\b(\d{4})-(\d{2})-(\d{2})\b",
]

MONTH_MAP = {
    "jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"sept":9,"oct":10,"nov":11,"dec":12
}

HTML_DATE_FIELDS = ["important_dates", "content", "description", "body", "details"]

MODEL_IMAGE_FIELDS = {
    Job:        ["image", "thumbnail", "thumb", "featured_image", "logo", "poster", "job_image", "job_photo"],
    Result:     ["image", "thumbnail", "thumb", "featured_image", "poster", "result_image"],
    Admitcard:  ["image", "thumbnail", "thumb", "featured_image", "poster", "admit_image"],
    Govtupdate: ["image", "thumbnail", "thumb", "featured_image", "poster", "update_image"],
}
MODEL_HTML_FIELDS = {
    Job:        ["content", "description", "body", "details", "important_dates"],
    Result:     ["content", "description", "body", "details", "important_dates"],
    Admitcard:  ["content", "description", "body", "details", "important_dates"],
    Govtupdate: ["content", "description", "body", "details", "important_dates"],
}

IMG_SRC_REGEX = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

def _first_attr(obj, names):
    for n in names:
        if hasattr(obj, n):
            v = getattr(obj, n)
            if v:
                return v
    return None

def _build_abs(request, url_or_path: str) -> str | None:
    if not url_or_path:
        return None
    u = str(url_or_path).strip()
    if u.startswith(("http://", "https://", "//")):
        return u
    media_prefix = (settings.MEDIA_URL or "/media/").rstrip("/") + "/"
    if u.startswith(media_prefix) or u.startswith("/media/"):
        return request.build_absolute_uri(u)
    joined = urljoin(settings.MEDIA_URL or "/media/", u.lstrip("/"))
    return request.build_absolute_uri(joined)

def _extract_img_from_html(request, obj):
    html_text = _first_attr(obj, MODEL_HTML_FIELDS.get(type(obj), []))
    if not isinstance(html_text, str):
        return None
    m = IMG_SRC_REGEX.search(html_text)
    return _build_abs(request, m.group(1)) if m else None

def _thumb_url(request, obj):
    for field in MODEL_IMAGE_FIELDS.get(type(obj), []):
        if hasattr(obj, field):
            val = getattr(obj, field)
            if not val:
                continue
            if hasattr(val, "url"):
                try:
                    return _build_abs(request, val.url)
                except Exception:
                    pass
            if isinstance(val, str):
                return _build_abs(request, val)
    for meth in ("get_image_url", "get_thumbnail_url"):
        if hasattr(obj, meth):
            try:
                mval = getattr(obj, meth)()
                if mval:
                    return _build_abs(request, mval)
            except Exception:
                pass
    return _extract_img_from_html(request, obj)

def _parse_dates_from_text(txt: str):
    if not txt or not isinstance(txt, str):
        return []
    found = []
    for pat in DATE_PATTERNS[:2]:
        for m in re.finditer(pat, txt, re.IGNORECASE):
            d = int(m.group(1)); mon = m.group(2).lower(); y = int(m.group(3))
            mon_num = MONTH_MAP.get(mon[:4]) or MONTH_MAP.get(mon[:3]) or MONTH_MAP.get(mon)
            if mon_num:
                try: found.append(date(y, mon_num, d))
                except ValueError: pass
    for m in re.finditer(DATE_PATTERNS[2], txt):
        d = int(m.group(1)); mon = int(m.group(2)); y = int(m.group(3))
        try: found.append(date(y, mon, d))
        except ValueError: pass
    for m in re.finditer(DATE_PATTERNS[3], txt):
        y = int(m.group(1)); mon = int(m.group(2)); d = int(m.group(3))
        try: found.append(date(y, mon, d))
        except ValueError: pass
    return found

def _pick_dt_from_html(obj):
    for field in HTML_DATE_FIELDS:
        if hasattr(obj, field):
            txt = getattr(obj, field)
            if not isinstance(txt, str):
                continue
            ds = _parse_dates_from_text(txt)
            if ds:
                last = max(ds)
                dt = datetime(last.year, last.month, last.day)
                return timezone.make_aware(dt) if timezone.is_naive(dt) else dt
    return None

def _coerce_dt(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return timezone.make_aware(value) if timezone.is_naive(value) else value
    if isinstance(value, date):
        dt = datetime(value.year, value.month, value.day)
        return timezone.make_aware(dt)
    return None

DATE_FIELD_CANDIDATES = [
    "published_date",
    "updated_at", "updated", "modified", "last_updated",
    "publish_date", "published_at", "posted_on", "post_date", "news_date",
    "created_at", "created", "created_on", "date",
]

def _pick_dt(obj):
    for f in DATE_FIELD_CANDIDATES:
        if hasattr(obj, f):
            dt = _coerce_dt(getattr(obj, f))
            if dt:
                return dt
    return _pick_dt_from_html(obj)

def _title(obj):
    return _first_attr(obj, ["title", "name", "heading", "post_title"]) or "(Untitled)"

def _slug(obj):
    return _first_attr(obj, ["slug", "permalink", "url_slug"])

# URL names (अगर आपके urls.py में अलग हैं, यहाँ बदल दें)
TYPE_URLNAME = {
    "Jobs":        "job_detail",
    "Results":     "result_detail",
    "Admit Cards": "admitcard_detail",
    "Govt Updates":"govtupdate_detail",
}
# Hard-coded path prefixes (reverse fail होने पर)
TYPE_PREFIX = {
    "Jobs":        "/latest-jobs/",
    "Results":     "/results/",
    "Admit Cards": "/admit-card/",
    "Govt Updates":"/govt-updates/",
}

def _url_for_type(label, obj):
    # 1) get_absolute_url()
    if hasattr(obj, "get_absolute_url"):
        try:
            u = obj.get_absolute_url()
            if u: return u, None
        except Exception as e:
            # continue to fallbacks
            pass

    # 2) direct fields: url/link
    direct = _first_attr(obj, ["url", "link", "external_url"])
    if isinstance(direct, str) and direct.strip():
        return direct.strip(), None

    # 3) reverse by name + slug
    slg = _slug(obj)
    if slg:
        try:
            urlname = TYPE_URLNAME.get(label)
            if urlname:
                return reverse(urlname, kwargs={"slug": slg}), None
        except NoReverseMatch as e:
            # 4) prefix + slug
            prefix = TYPE_PREFIX.get(label)
            if prefix:
                return f"{prefix}{slg}/", None
        except Exception as e:
            prefix = TYPE_PREFIX.get(label)
            if prefix:
                return f"{prefix}{slg}/", f"reverse-error:{e}"

    # 5) give up
    return "#", "no-url-and-no-slug"


#today news
from django.urls import reverse, NoReverseMatch

PLACEHOLDER = "https://via.placeholder.com/160x120.png?text=News"

DATE_PATTERNS = [
    r"\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+(\d{4})\b",
    r"\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
    r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b",
    r"\b(\d{4})-(\d{2})-(\d{2})\b",
]

MONTH_MAP = {
    "jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"sept":9,"oct":10,"nov":11,"dec":12
}

HTML_DATE_FIELDS = ["important_dates", "content", "description", "body", "details"]

MODEL_IMAGE_FIELDS = {
    Job:        ["image", "thumbnail", "thumb", "featured_image", "logo", "poster", "job_image", "job_photo"],
    Result:     ["image", "thumbnail", "thumb", "featured_image", "poster", "result_image"],
    Admitcard:  ["image", "thumbnail", "thumb", "featured_image", "poster", "admit_image"],
    Govtupdate: ["image", "thumbnail", "thumb", "featured_image", "poster", "update_image"],
}
MODEL_HTML_FIELDS = {
    Job:        ["content", "description", "body", "details", "important_dates"],
    Result:     ["content", "description", "body", "details", "important_dates"],
    Admitcard:  ["content", "description", "body", "details", "important_dates"],
    Govtupdate: ["content", "description", "body", "details", "important_dates"],
}

IMG_SRC_REGEX = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

def _first_attr(obj, names):
    for n in names:
        if hasattr(obj, n):
            v = getattr(obj, n)
            if v:
                return v
    return None

def _build_abs(request, url_or_path: str) -> str | None:
    if not url_or_path:
        return None
    u = str(url_or_path).strip()
    if u.startswith(("http://", "https://", "//")):
        return u
    media_prefix = (settings.MEDIA_URL or "/media/").rstrip("/") + "/"
    if u.startswith(media_prefix) or u.startswith("/media/"):
        return request.build_absolute_uri(u)
    joined = urljoin(settings.MEDIA_URL or "/media/", u.lstrip("/"))
    return request.build_absolute_uri(joined)

def _extract_img_from_html(request, obj):
    html_text = _first_attr(obj, MODEL_HTML_FIELDS.get(type(obj), []))
    if not isinstance(html_text, str):
        return None
    m = IMG_SRC_REGEX.search(html_text)
    return _build_abs(request, m.group(1)) if m else None

def _thumb_url(request, obj):
    for field in MODEL_IMAGE_FIELDS.get(type(obj), []):
        if hasattr(obj, field):
            val = getattr(obj, field)
            if not val:
                continue
            if hasattr(val, "url"):
                try:
                    return _build_abs(request, val.url)
                except Exception:
                    pass
            if isinstance(val, str):
                return _build_abs(request, val)
    for meth in ("get_image_url", "get_thumbnail_url"):
        if hasattr(obj, meth):
            try:
                mval = getattr(obj, meth)()
                if mval:
                    return _build_abs(request, mval)
            except Exception:
                pass
    return _extract_img_from_html(request, obj)

def _parse_dates_from_text(txt: str):
    if not txt or not isinstance(txt, str):
        return []
    found = []
    for pat in DATE_PATTERNS[:2]:
        for m in re.finditer(pat, txt, re.IGNORECASE):
            d = int(m.group(1)); mon = m.group(2).lower(); y = int(m.group(3))
            mon_num = MONTH_MAP.get(mon[:4]) or MONTH_MAP.get(mon[:3]) or MONTH_MAP.get(mon)
            if mon_num:
                try: found.append(date(y, mon_num, d))
                except ValueError: pass
    for m in re.finditer(DATE_PATTERNS[2], txt):
        d = int(m.group(1)); mon = int(m.group(2)); y = int(m.group(3))
        try: found.append(date(y, mon, d))
        except ValueError: pass
    for m in re.finditer(DATE_PATTERNS[3], txt):
        y = int(m.group(1)); mon = int(m.group(2)); d = int(m.group(3))
        try: found.append(date(y, mon, d))
        except ValueError: pass
    return found

def _pick_dt_from_html(obj):
    for field in HTML_DATE_FIELDS:
        if hasattr(obj, field):
            txt = getattr(obj, field)
            if not isinstance(txt, str):
                continue
            ds = _parse_dates_from_text(txt)
            if ds:
                last = max(ds)
                dt = datetime(last.year, last.month, last.day)
                return timezone.make_aware(dt) if timezone.is_naive(dt) else dt
    return None

def _coerce_dt(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return timezone.make_aware(value) if timezone.is_naive(value) else value
    if isinstance(value, date):
        dt = datetime(value.year, value.month, value.day)
        return timezone.make_aware(dt)
    return None

DATE_FIELD_CANDIDATES = [
    "published_date",
    "updated_at", "updated", "modified", "last_updated",
    "publish_date", "published_at", "posted_on", "post_date", "news_date",
    "created_at", "created", "created_on", "date",
]

def _pick_dt(obj):
    for f in DATE_FIELD_CANDIDATES:
        if hasattr(obj, f):
            dt = _coerce_dt(getattr(obj, f))
            if dt:
                return dt
    return _pick_dt_from_html(obj)

def _title(obj):
    return _first_attr(obj, ["title", "name", "heading", "post_title"]) or "(Untitled)"

def _slug(obj):
    return _first_attr(obj, ["slug", "permalink", "url_slug"])

# URL names (अगर आपके urls.py में अलग हैं, यहाँ बदल दें)
TYPE_URLNAME = {
    "Jobs":        "job_detail",
    "Results":     "result_detail",
    "Admit Cards": "admitcard_detail",
    "Govt Updates":"govtupdate_detail",
}
# Hard-coded path prefixes (reverse fail होने पर)
TYPE_PREFIX = {
    "Jobs":        "/latest-jobs/",
    "Results":     "/results/",
    "Admit Cards": "/admit-card/",
    "Govt Updates":"/govt-updates/",
}

def _url_for_type(label, obj):
    # 1) get_absolute_url()
    if hasattr(obj, "get_absolute_url"):
        try:
            u = obj.get_absolute_url()
            if u: return u, None
        except Exception as e:
            # continue to fallbacks
            pass

    # 2) direct fields: url/link
    direct = _first_attr(obj, ["url", "link", "external_url"])
    if isinstance(direct, str) and direct.strip():
        return direct.strip(), None

    # 3) reverse by name + slug
    slg = _slug(obj)
    if slg:
        try:
            urlname = TYPE_URLNAME.get(label)
            if urlname:
                return reverse(urlname, kwargs={"slug": slg}), None
        except NoReverseMatch as e:
            # 4) prefix + slug
            prefix = TYPE_PREFIX.get(label)
            if prefix:
                return f"{prefix}{slg}/", None
        except Exception as e:
            prefix = TYPE_PREFIX.get(label)
            if prefix:
                return f"{prefix}{slg}/", f"reverse-error:{e}"

    # 5) give up
    return "#", "no-url-and-no-slug"


#indian results

from django.urls import reverse, NoReverseMatch

PLACEHOLDER = "https://via.placeholder.com/160x120.png?text=News"

DATE_PATTERNS = [
    r"\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+(\d{4})\b",
    r"\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
    r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b",
    r"\b(\d{4})-(\d{2})-(\d{2})\b",
]

MONTH_MAP = {
    "jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"sept":9,"oct":10,"nov":11,"dec":12
}

HTML_DATE_FIELDS = ["important_dates", "content", "description", "body", "details"]

MODEL_IMAGE_FIELDS = {
    Job:        ["image", "thumbnail", "thumb", "featured_image", "logo", "poster", "job_image", "job_photo"],
    Result:     ["image", "thumbnail", "thumb", "featured_image", "poster", "result_image"],
    Admitcard:  ["image", "thumbnail", "thumb", "featured_image", "poster", "admit_image"],
    Govtupdate: ["image", "thumbnail", "thumb", "featured_image", "poster", "update_image"],
}
MODEL_HTML_FIELDS = {
    Job:        ["content", "description", "body", "details", "important_dates"],
    Result:     ["content", "description", "body", "details", "important_dates"],
    Admitcard:  ["content", "description", "body", "details", "important_dates"],
    Govtupdate: ["content", "description", "body", "details", "important_dates"],
}

IMG_SRC_REGEX = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

def _first_attr(obj, names):
    for n in names:
        if hasattr(obj, n):
            v = getattr(obj, n)
            if v:
                return v
    return None

def _build_abs(request, url_or_path: str) -> str | None:
    if not url_or_path:
        return None
    u = str(url_or_path).strip()
    if u.startswith(("http://", "https://", "//")):
        return u
    media_prefix = (settings.MEDIA_URL or "/media/").rstrip("/") + "/"
    if u.startswith(media_prefix) or u.startswith("/media/"):
        return request.build_absolute_uri(u)
    joined = urljoin(settings.MEDIA_URL or "/media/", u.lstrip("/"))
    return request.build_absolute_uri(joined)

def _extract_img_from_html(request, obj):
    html_text = _first_attr(obj, MODEL_HTML_FIELDS.get(type(obj), []))
    if not isinstance(html_text, str):
        return None
    m = IMG_SRC_REGEX.search(html_text)
    return _build_abs(request, m.group(1)) if m else None

def _thumb_url(request, obj):
    for field in MODEL_IMAGE_FIELDS.get(type(obj), []):
        if hasattr(obj, field):
            val = getattr(obj, field)
            if not val:
                continue
            if hasattr(val, "url"):
                try:
                    return _build_abs(request, val.url)
                except Exception:
                    pass
            if isinstance(val, str):
                return _build_abs(request, val)
    for meth in ("get_image_url", "get_thumbnail_url"):
        if hasattr(obj, meth):
            try:
                mval = getattr(obj, meth)()
                if mval:
                    return _build_abs(request, mval)
            except Exception:
                pass
    return _extract_img_from_html(request, obj)

def _parse_dates_from_text(txt: str):
    if not txt or not isinstance(txt, str):
        return []
    found = []
    for pat in DATE_PATTERNS[:2]:
        for m in re.finditer(pat, txt, re.IGNORECASE):
            d = int(m.group(1)); mon = m.group(2).lower(); y = int(m.group(3))
            mon_num = MONTH_MAP.get(mon[:4]) or MONTH_MAP.get(mon[:3]) or MONTH_MAP.get(mon)
            if mon_num:
                try: found.append(date(y, mon_num, d))
                except ValueError: pass
    for m in re.finditer(DATE_PATTERNS[2], txt):
        d = int(m.group(1)); mon = int(m.group(2)); y = int(m.group(3))
        try: found.append(date(y, mon, d))
        except ValueError: pass
    for m in re.finditer(DATE_PATTERNS[3], txt):
        y = int(m.group(1)); mon = int(m.group(2)); d = int(m.group(3))
        try: found.append(date(y, mon, d))
        except ValueError: pass
    return found

def _pick_dt_from_html(obj):
    for field in HTML_DATE_FIELDS:
        if hasattr(obj, field):
            txt = getattr(obj, field)
            if not isinstance(txt, str):
                continue
            ds = _parse_dates_from_text(txt)
            if ds:
                last = max(ds)
                dt = datetime(last.year, last.month, last.day)
                return timezone.make_aware(dt) if timezone.is_naive(dt) else dt
    return None

def _coerce_dt(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return timezone.make_aware(value) if timezone.is_naive(value) else value
    if isinstance(value, date):
        dt = datetime(value.year, value.month, value.day)
        return timezone.make_aware(dt)
    return None

DATE_FIELD_CANDIDATES = [
    "published_date",
    "updated_at", "updated", "modified", "last_updated",
    "publish_date", "published_at", "posted_on", "post_date", "news_date",
    "created_at", "created", "created_on", "date",
]

def _pick_dt(obj):
    for f in DATE_FIELD_CANDIDATES:
        if hasattr(obj, f):
            dt = _coerce_dt(getattr(obj, f))
            if dt:
                return dt
    return _pick_dt_from_html(obj)

def _title(obj):
    return _first_attr(obj, ["title", "name", "heading", "post_title"]) or "(Untitled)"

def _slug(obj):
    return _first_attr(obj, ["slug", "permalink", "url_slug"])

# URL names (अगर आपके urls.py में अलग हैं, यहाँ बदल दें)
TYPE_URLNAME = {
    "Jobs":        "job_detail",
    "Results":     "result_detail",
    "Admit Cards": "admitcard_detail",
    "Govt Updates":"govtupdate_detail",
}
# Hard-coded path prefixes (reverse fail होने पर)
TYPE_PREFIX = {
    "Jobs":        "/latest-jobs/",
    "Results":     "/results/",
    "Admit Cards": "/admit-card/",
    "Govt Updates":"/govt-updates/",
}

def _url_for_type(label, obj):
    # 1) get_absolute_url()
    if hasattr(obj, "get_absolute_url"):
        try:
            u = obj.get_absolute_url()
            if u: return u, None
        except Exception as e:
            # continue to fallbacks
            pass

    # 2) direct fields: url/link
    direct = _first_attr(obj, ["url", "link", "external_url"])
    if isinstance(direct, str) and direct.strip():
        return direct.strip(), None

    # 3) reverse by name + slug
    slg = _slug(obj)
    if slg:
        try:
            urlname = TYPE_URLNAME.get(label)
            if urlname:
                return reverse(urlname, kwargs={"slug": slg}), None
        except NoReverseMatch as e:
            # 4) prefix + slug
            prefix = TYPE_PREFIX.get(label)
            if prefix:
                return f"{prefix}{slg}/", None
        except Exception as e:
            prefix = TYPE_PREFIX.get(label)
            if prefix:
                return f"{prefix}{slg}/", f"reverse-error:{e}"

    # 5) give up
    return "#", "no-url-and-no-slug"

# All psc state  ----

def psc_all_states(request):
    return render(request, "psc/psc-all-states.html")

# def appsc(request):
#     return render(request, "psc/appsc.html")

def appsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="appsc") | Q(category__icontains="appsc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]

  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf andhrapradesh category wali jobs lao
  jobs_andhrapradesh = Job.objects.filter(
        category__icontains="andhrapradesh"    
    ).order_by("-published_date")[:5]
  return render(request, 'psc/appsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_andhrapradesh,})

def arunachal_appsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="arunachal psc") | Q(category__icontains="arunachal psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf arunachalpradesh category wali jobs lao
  jobs_arunachalpradesh = Job.objects.filter(
        category__icontains="arunachalpradesh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'PSC/ArunachalPPSC.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_arunachalpradesh,})


def apsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="assam psc") | Q(category__icontains="assam psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf assam category wali jobs lao
  jobs_assam = Job.objects.filter(
        category__icontains="assam"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/apsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_assam,})



def bpsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="bihar psc") | Q(category__icontains="bihar psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf bihar category wali jobs lao
  jobs_bihar = Job.objects.filter(
        category__icontains="bihar"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/bpsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_bihar,})


def cgpsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="chandigarh psc") | Q(category__icontains="chandigarh psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf chandigarh category wali jobs lao
  jobs_chandigarh = Job.objects.filter(
        category__icontains="chandigarh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/cgpsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_chandigarh,} )


def goapsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="goa psc") | Q(category__icontains="goa psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf goa category wali jobs lao
  jobs_goa = Job.objects.filter(
        category__icontains="goa"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/goa.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_goa,})

def gpsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="gujarat psc") | Q(category__icontains="gujarat psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf gujarat category wali jobs lao
  jobs_gujarat = Job.objects.filter(
        category__icontains="gujarat"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/gpsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_gujarat,})


def hpsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="haryana psc") | Q(category__icontains="haryana psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf haryana category wali jobs lao
  jobs_haryana = Job.objects.filter(
        category__icontains="haryana"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/hpsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_haryana,})


def hppsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="himachalpradesh psc") | Q(category__icontains="himachalpradesh psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf himachalpradesh category wali jobs lao
  jobs_himachalpradesh = Job.objects.filter(
        category__icontains="himachalpradesh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/hppsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_himachalpradesh,})

def jkpsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="jammukashmir psc") | Q(category__icontains="jammukashmir psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf jammukashmir category wali jobs lao
  jobs_jammukashmir = Job.objects.filter(
        category__icontains="jammukashmir"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/jkpsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_jammukashmir,})

def jpsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="jharkhand psc") | Q(category__icontains="jharkhand psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf jharkhand category wali jobs lao
  jobs_jharkhand = Job.objects.filter(
        category__icontains="jharkhand"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/jpsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_jharkhand,})

def kpsc(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="karnataka psc") | Q(category__icontains="karnataka psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf karnataka category wali jobs lao
  jobs_karnataka = Job.objects.filter(
        category__icontains="karnataka"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/kpsc.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_karnataka,})


def kerala_job(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="kerala psc") | Q(category__icontains="kerala psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf kerala category wali jobs lao
  jobs_kerala = Job.objects.filter(
        category__icontains="kerala"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/kerala_job.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_kerala,})


def mppsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="madhyapradesh psc") | Q(category__icontains="madhyapradesh psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf madhyapradesh category wali jobs lao
  jobs_madhyapradesh = Job.objects.filter(
        category__icontains="madhyapradesh"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/mppsc-jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_madhyapradesh,} )


def mpsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="maharashtra psc") | Q(category__icontains="maharashtra psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf maharashtra category wali jobs lao
  jobs_maharashtra = Job.objects.filter(
        category__icontains="maharashtra"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/mpsc-jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_maharashtra,} )


def manipur_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="manipur psc") | Q(category__icontains="manipur psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf manipur category wali jobs lao
  jobs_manipur = Job.objects.filter(
        category__icontains="manipur"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/manipur_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_manipur,} )


def meghalaya_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="meghalaya psc") | Q(category__icontains="meghalaya psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf meghalaya category wali jobs lao
  jobs_meghalaya = Job.objects.filter(
        category__icontains="meghalaya"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/meghalaya_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_meghalaya,} )


def mizoram_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="mizoram psc") | Q(category__icontains="mizoram psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf mizoram category wali jobs lao
  jobs_mizoram = Job.objects.filter(
        category__icontains="mizoram"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/mizoram_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_mizoram,} )

def nagaland_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="nagaland psc") | Q(category__icontains="nagaland psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)


   # Sirf nagaland category wali jobs lao
  jobs_nagaland = Job.objects.filter(
        category__icontains="nagaland"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/nagaland_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_nagaland,} )


def opsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="odisha psc") | Q(category__icontains="odisha psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf odisha category wali jobs lao
  jobs_odisha = Job.objects.filter(
        category__icontains="odisha"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/opsc_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_odisha,} )


def punjab_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="punjab psc") | Q(category__icontains="punjab psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf punjab category wali jobs lao
  jobs_punjab = Job.objects.filter(
        category__icontains="punjab"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/punjab_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_punjab,} )

def rpsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="rajasthan psc") | Q(category__icontains="rajasthan psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf rajasthan category wali jobs lao
  jobs_rajasthan = Job.objects.filter(
        category__icontains="rajasthan"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/rpsc_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_rajasthan,} )

def sikkim_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="sikkim psc") | Q(category__icontains="sikkim psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf sikkim category wali jobs lao
  jobs_sikkim = Job.objects.filter(
        category__icontains="sikkim"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/sikkim_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_sikkim,} )



def tnpsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="tamilnadu psc") | Q(category__icontains="tamilnadu psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf tamilnadu category wali jobs lao
  jobs_tamilnadu = Job.objects.filter(
        category__icontains="tamilnadu"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/tnpsc_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_tamilnadu,} )

def telangana_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="telangana psc") | Q(category__icontains="telangana psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf telangana category wali jobs lao
  jobs_telangana = Job.objects.filter(
        category__icontains="telangana"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/telangana_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_telangana,} )

def tripura_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="tripura psc") | Q(category__icontains="tripura psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf tripura category wali jobs lao
  jobs_tripura = Job.objects.filter(
        category__icontains="tripura"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/tripura_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_tripura,} )


def uppsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="up psc") | Q(category__icontains="up psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf upjob category wali jobs lao
  jobs_upjob = Job.objects.filter(
        category__icontains="up"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/uppsc_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_upjob,} )


def ukpsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="uttarakhand psc") | Q(category__icontains="uttarakhand psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf uttarakhand category wali jobs lao
  jobs_uttarakhand = Job.objects.filter(
        category__icontains="uttarakhand"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/ukpsc_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_uttarakhand,} )


def wbpsc_jobs(request):
  qs = Job.objects.filter(status='published', is_active=True).filter(
        Q(category__icontains="westbengal psc") | Q(category__icontains="westbengal psc")
    ).order_by("-published_date")
  latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:5]
  latest_govtupdates = Govtupdate.objects.filter(status='published', is_active=True).order_by("-published_date")[:10]
  paginator = Paginator(qs, 20, orphans=1) # प्रति पेज 10 jobs दिखाने के लिए (2 बहुत कम है)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

   # Sirf westbengal category wali jobs lao
  jobs_westbengal = Job.objects.filter(
        category__icontains="westbengal"   # agar field exact "10th" hai to category="10th" bhi chalega
    ).order_by("-published_date")[:5]
  return render(request, 'psc/wbpsc_jobs.html',  {"posts": qs, "page_obj":page_obj, "latest_results": latest_results, "latest_admitcards": latest_admitcards, 'latest_govtupdates': latest_govtupdates,"latest_posts": jobs_westbengal,} )

def custom_404(request, exception=None):
     return redirect("/")  # Home page par redirect

# 500 error page

def custom_500(request):
    # 500 ke liye direct render (no exception param)
    return render(request, "mainfile/500.html", status=500)


#subscriber

from django.shortcuts import render, redirect
from .forms import SubscriberForm

latest_results = Result.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]  # latest 10 job
latest_admitcards = Admitcard.objects.filter(status='published', is_active=True).order_by("-published_date")[:6]  # latest 10 job

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()  # Direct DB mein save
            return redirect('/sarkari-result-2024/')  # Success page par redirect (niche banayenge)
    else:
        form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form, "latest_results": latest_results, "latest_admitcards": latest_admitcards, "today": date.today()})

