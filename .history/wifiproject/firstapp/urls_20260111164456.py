from django.urls import path
from . import views
from .views import JobPostCreateView, ResultPostCreateView, AdmitcardPostCreateView, GovtupdatePostCreateView
from .feeds import LatestAllFeed
from django.views.decorators.cache import cache_page
from .views import subscribe
from django.views.generic import RedirectView

urlpatterns = [
        path('', views.home, name='home'),
        path('feed/', (LatestAllFeed()), name='site_feed'),  # Feed 
        
        path('rojgar-result/', views.rojgarresult, name="rojgarresult"),
        path('free-job-alert/', views.freejobalert, name='freejobalert'),
        path('result-bharat/', views.resultbharat, name='resultbharat'),
        path('sarkari-jobs/', views.sarkarijobs, name='sarkarijobs'), # all sarkai jobs
        path("bihar-help/", views.biharhelp, name="biharhelp"),
        
        path("latest-jobs/job/", JobPostCreateView.as_view(), name="job_add"),
        path('latest-jobs/', views.job, name='job'),

        path('search/', views.search, name='search'),
        

        path('signup/',views.SignupPage,name='signup'),
        path('logout/',views.LogoutPage,name='logout'),
        path("login/", views.LoginPage, name="login"),

        

        path('all-india-govt-jobs/', views.all_india_govt_jobs, name='all_india_govt_jobs'), # allindiagovtjobs
        path('govt-jobs-today/', views.govtjobstoday, name='govtjobstoday'), # all  govt job today 
        path("latest-jobs/<slug:slug>/", views.job_detail, name="job_detail"),
        path('vacancy/', views.vacancy, name='vacancy'),
        path('online-form/', views.onlineform, name='onlineform'),
        path('sarkari-result-2025/', views.sarkariresult2025, name='sarkariresult2025'),
        path('sarkari-naukri/', views.sarkarinokri, name="sarkarinokri"),

        path('results/', views.result, name='result'),
        path("results/result/", ResultPostCreateView.as_view(), name="result_add"), 
        path('results/<slug:slug>/', views.result_detail, name='result_detail'),

        path('sarkari-result/', views.sarkariresult, name='sarkariresult'), # all sarkai results
        path('sarkari-result-2024/', views.sarkariresult2024, name='sarkariresult2024'), # sarkariresult2024
        path('board-result/', views.boardresult, name='boardresult'), # boardresult
        path('iti-result/', views.itiresult, name="itiresult"),
        

        path('admit-card/', views.admitcard, name='admitcard'),
        path('exam-date/', views.examdate, name='examdate'),
        path('sarkari-exam/', views.sarkariexam, name='sarkariexam'),
        path("admit-card/admitcard/", AdmitcardPostCreateView.as_view(), name="admitcard_add"),
        path('admit-card/<slug:slug>/', views.admitcard_detail, name='admitcard_detail'),

        path("govt-updates/", views.govtupdates, name='govtupdates'),
        path("govt-updates/govt/", GovtupdatePostCreateView.as_view(), name="govtupdate_add"),
        path("govt-updates/<path:slug>/", views.govt_update_detail, name="govt-update-detail"),

        path('admission/', views.admission, name='admission'),
        path('answer-key/', views.answerkey, name='answerkey'),
        path('scholarship/', views.scholarship, name='scholarship'),
        path('sarkari-yojana/', views.sarkariyojna, name='sarkariyojna'),
        path('syllabus/', views.syllabus, name='syllabus'),


        path('contact-us/', views.contact, name="contact"),
        path('about-us/', views.about, name='about'),
        path('disclaimer/', views.disclaimer, name='disclaimer'),
        path('privacy-policy/', views.PrivacyPolicy, name="PrivacyPolicy"),
        path('dmca/', views.dmca, name='dmca'),
        path('hyperlink-policy/', views.hyperlinkpolicy, name='hyperlinkpolicy'),
        path('terms-and-conditions/', views.TermsConditions, name='TermsConditions'),
        path('editorial-policy/', views.editorialpolicy, name='editorialpolicy'),
        path('fact-checking-and-corrections-policy/', views.FactCheckingPolicy, name='FactCheckingPolicy'),
        path('advertising-policy/', views.AdvertisingPolicy, name='AdvertisingPolicy'),
        path('grievance-officer/', views.grievanceofficer, name='grievanceofficer'),
        path('cookie-policy/', views.cookiepolicy, name='cookiepolicy'),
        path('sitemap.html/', views.html_sitemap, name='html_sitemap'),

# Author
        
        path('authors/', views.MeetTeam, name="MeetTeam"),
        path('authors/arvind-pal/', views.arvind, name='arvindpal'),
        path('authors/priya-patel/', views.priya, name='priya'),
      


#allstate
        path("state-government-jobs/", views.all_state_govt_job, name="all-state-govt-job"),
        path('andhra-pradesh-govt-jobs/', views.AndhraPradesh, name="AndhraPradesh"), 
        path('arunachal-pradesh-govt-jobs/', views.ArunachalPradesh, name='ArunachalPradesh'),
        path('assam-govt-jobs/', views.Assam, name='Assam'),
        path('bihar-govt-jobs/', views.Bihar, name="Bihar"),
        path('chhattisgarh-govt-jobs/', views.Chhattisgarh, name='Chhattisgarh'),
        path('delhi-govt-jobs/', views.Delhi, name='Delhi'),
        path('goa-govt-jobs/', views.Goa, name='Goa'),
        path('gujarat-govt-jobs/', views.Gujarat, name='Gujarat'),
        path('haryana-govt-jobs/', views.Haryana, name='Haryana'),
        path('himachal-pradesh-govt-jobs/', views.HimachalPradesh, name='HimachalPradesh'),
        path('jammu-kashmir-govt-jobs/', views.JammuKashmir, name='JammuKashmir'),
        path('jharkhand-govt-jobs/', views.Jharkhand, name='Jharkhand'),
        path('karnataka-govt-jobs/', views.Karnataka, name='Karnataka'),
        path('kerala-govt-jobs/', views.Kerala, name='Kerala'),
        path('madhya-pradesh-govt-jobs/', views.MadhyaPradesh, name="MadhyaPradesh"),
        path('maharashtra-govt-jobs/', views.Maharashtra, name='Maharashtra'),
        path('manipur-govt-jobs/', views.Manipur, name='Manipur'),
        path('meghalaya-govt-jobs/', views.Meghalaya, name='Meghalaya'),
        path('mizoram-govt-jobs/', views.Mizoram, name='Mizoram'),
        path('nagaland-govt-jobs/', views.Nagaland, name='Nagaland'),
        path('odisha-govt-jobs/', views.Odisha, name='Odisha'),
        path('punjab-govt-jobs/', views.Punjab, name='Punjab'),
        path('rajasthan-govt-jobs/', views.Rajasthan, name='Rajasthan'),
        path('sikkim-govt-jobs/', views.Sikkim, name='Sikkim'),
        path('tamil-nadu-govt-jobs/', views.TamilNadu, name='TamilNadu'),
        path('telangana-govt-jobs/', views.Telangana, name='Telangana'),
        path('tripura-govt-jobs/', views.Tripura, name='Tripura'),
        path('up-govt-jobs/', views.upjob, name='upjob'),
        path('uttarakhand-govt-jobs/', views.Uttarakhand, name='Uttarakhand'),
        path('west-bengal-govt-jobs/', views.WestBengal, name='WestBengal'),

        path('andaman-nicobar-govt-jobs/', views.AndamanNicobar, name='AndamanNicobar'),
        path('chandigarh-govt-jobs/', views.Chandigarh, name='Chandigarh'),
        path('dadra-nagar-haveli-govt-jobs/', views.DadraNagarHaveli, name='DadraNagarHaveli'),
        path('daman-diu-govt-jobs/', views.DamanDiu, name='DamanDiu'),
        path('ladakh-govt-jobs/', views.Ladakh, name='Ladakh'),
        path('lakshadweep-govt-jobs/', views.Lakshadweep, name='Lakshadweep'),
        path('puducherry-govt-jobs/', views.Puducherry, name='Puducherry'),
        

# central govt jobs
        path('central-govt-jobs/', views.CentralGovtjob, name='CentralGovtjob'),
        
#Qualification
        path("all-education/", views.all_education, name="all_education"),
        path("8th-pass-jobs/", views.EighthPassJob, name="EighthPassJob"),
        path('10th-pass-jobs/', views.tenthjob, name='tenthjob'),
        path('12th-pass-jobs/', views.twellthjob, name='twellthjob'),
        path('graduation-job/', views.graduationjob, name='graduationjob'),
        path('post-graduation/', views.postgraduationjob, name='postgraduaionjob'),
        path('diploma-jobs/', views.diploma_jobs, name='diploma_jobs'),
        path('engineering-jobs/', views.engineering_jobs, name='engineering_jobs'),
        path('medical-jobs/', views.medical_jobs, name='medical_jobs'),
        path('iti-govt-jobs/', views.itigovtjobs, name='itigovtjobs'),
        path('apprentice-job/', views.apprenticejob, name='apprenticejob'),
        

#category
        path('all-category-jobs/', views.allcategoryjobs, name='allcategoryjobs'),
        path('railway-jobs/', views.railwayjob, name='railwayjob'),
        path('bank-jobs/', views.bankjob, name='bankjob'),
        path('defense-jobs/', views.defensejob, name='defensejob'),
        path('police-jobs/', views.policejobs, name="policejobs"),
        path('up-police/', views.uppolice, name="uppolice"),
        path('delhi-police/', views.delhipolice, name="delhipolice"),
        path('rajasthan-police/', views.rajasthanpolice, name="rajasthanpolice"),
        path('ssc-jobs/', views.sscjob, name='sscjob'),
        path('upsc-job/', views.upscjob, name='upscjob'), 
        path('government-teacher-jobs/', views.government_teacher_jobs, name='government_teacher_jobs'),
        path('exam-results/', views.examresults, name="examresults"),
        path('exam-dates/', views.examdate, name="examdate"),

        
# All pcs state  ----

        path("all-psc-in-india/", views.psc_all_states, name="psc_all_states"),
        path("appsc-jobs/", views.appsc, name="appsc"),
        path("arunachal-appsc-jobs/", views.arunachal_appsc_jobs, name="arunachal_appsc_jobs"),
        path("assam-apsc-jobs/", views.apsc, name="apsc"),
        path("bpsc-jobs/", views.bpsc, name="bpsc"),
        path("cgpsc-jobs/", views.cgpsc, name="cgpsc"),
        path("goa-psc-jobs/", views.goapsc,  name="goapsc"),
        path("gujarat-gpsc-jobs/", views.gpsc, name="gpsc"),
        path("hpsc-jobs/", views.hpsc, name="hpsc"),
        path("hppsc-jobs/", views.hppsc, name="hppsc"),
        path("jkpsc-jobs/", views.jkpsc, name="jkpsc"),
        path("jpsc-jobs/", views.jpsc, name="jpsc"),
        path("kpsc-jobs/", views.kpsc, name="kpsc"),
        path("kerala-psc-jobs/", views.kerala_job, name="kerala_job"),
        path("mppsc-jobs/", views.mppsc_jobs, name="mppsc_jobs"),
        path("mpsc-jobs/", views.mpsc_jobs, name="mpsc_jobs"),
        path("manipur-psc-jobs/", views.manipur_jobs, name="manipur_jobs"),
        path("meghalaya-psc-jobs/", views.meghalaya_jobs, name="meghalaya_jobs"),
        path("mizoram-psc-jobs/", views.mizoram_jobs, name='mizoram_jobs'),
        path("nagaland-psc-jobs/", views.nagaland_jobs, name="nagaland_jobs"),
        path("opsc-jobs/", views.opsc_jobs, name="opsc_jobs"),
        path("punjab-ppsc-jobs/", views.punjab_jobs, name="punjab_jobs"),
        path("rpsc-jobs/", views.rpsc_jobs, name="rpsc_jobs"),
        path("sikkim-psc-jobs/", views.sikkim_jobs, name="sikkim_jobs"),
        path("tnpsc-jobs/", views.tnpsc_jobs, name="tnpsc_jobs"),
        path("telangana-tspsc-jobs/", views.telangana_jobs, name="telangana_jobs"),
        path("tripura-tpsc-jobs/", views.tripura_jobs, name="tripura_jobs"),
        path("uppsc-jobs/", views.uppsc_jobs, name="uppsc_jobs"),
        path("ukpsc-jobs/", views.ukpsc_jobs, name="ukpsc_jobs"),
        path("west-bengal-wbpsc-jobs/", views.wbpsc_jobs, name="wbpsc_jobs"),

        path('sarkari/', views.Sarkari, name="Sarkari"),

        path('subscriber/', subscribe, name='subscribe'),
] 

