from django import forms
from .models import Job, Result, Admitcard, Govtupdate

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # लगभग सब भरवाना है, बस slug/published_date जैसी auto चीज़ें नहीं
        exclude = ["slug", "published_date"]  # जरूरत हो तो "is_active" भी exclude करें

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        # लगभग सब भरवाना है, बस slug/published_date जैसी auto चीज़ें नहीं
        exclude = ["slug", "published_date"]  # जरूरत हो तो "is_active" भी exclude करें

class AdmitcardForm(forms.ModelForm):
    class Meta:
        model = Admitcard
        # लगभग सब भरवाना है, बस slug/published_date जैसी auto चीज़ें नहीं
        exclude = ["slug", "published_date"]  # जरूरत हो तो "is_active" भी exclude करें

class GovtupdateForm(forms.ModelForm):
    class Meta:
        model = Govtupdate
        # लगभग सब भरवाना है, बस slug/published_date जैसी auto चीज़ें नहीं
        exclude = ["slug", "published_date"]  # जरूरत हो तो "is_active" भी exclude करें



# firstapp/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    # Optionally, widgets/labels customize कर सकते हैं
    pass



#pdf
from django import forms
from django.conf import settings
from .models import PdfDocument
import os

ALLOWED_EXTENSIONS = ['.pdf']

class PdfUploadForm(forms.ModelForm):
    class Meta:
        model = PdfDocument
        fields = ['title', 'pdf', 'description']

    def clean_pdf(self):
        f = self.cleaned_data.get('pdf')
        if not f:
            raise forms.ValidationError("Koi file upload nahi hui.")
        ext = os.path.splitext(f.name)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise forms.ValidationError("Sirf PDF file allowed hain.")
        max_size = getattr(settings, 'MAX_UPLOAD_SIZE', 10*1024*1024)
        if f.size > max_size:
            raise forms.ValidationError(f"File bahut badi hai. Max {max_size // (1024*1024)} MB.")
        # optional: basic content_type check
        if hasattr(f, 'content_type') and f.content_type not in ('application/pdf', 'application/octet-stream'):
            raise forms.ValidationError("Uploaded file ka MIME type PDF jaisa nahi lagta.")
        return f


#subscriber

from django import forms
from .models import Subscriber  # Model import karen

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']  # Sirf email field
        