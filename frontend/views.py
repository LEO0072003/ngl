from django.shortcuts import redirect, render
from rest_framework.reverse import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.middleware.csrf import get_token
from user.models import UserAppDownload
from django.db.models import Sum
import requests as _requests
# Create your views here.
from django.views import View


class LandingPageView(LoginRequiredMixin, View):
    """Landing Page Login View"""
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', None)
        if q =='profile':
            return render(request, 'profile.html')

        if q =='apps':
            return render(request, 'add_app.html')

        if q =='points':
            app_download = UserAppDownload.objects.filter(user=request.user)
            total_points = app_download.aggregate(Sum('app__points'))
            return render(request, 'points.html', context=total_points)
        if q =='task':
            return render(request, 'task.html')
        return render(request, 'home.html')



class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class AppDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app_detail.html', context=kwargs)


class CreateAppView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):

        session = _requests.Session()

        session.cookies.update(request.COOKIES)
        post_data = request.POST
        files_data = request.FILES

        app_name = post_data.get('app_name')
        app_link = post_data.get('app_link')
        image = files_data.get('image')

        data = {
            'pic': image,
            'app_link': app_link,
            # 'sub_category'
        }

        files = {
            'image': image,  # Send the image file (ensure 'image' matches the form field name)
        }

        # Reverse the URL for the app-list endpoint
        url = reverse('app-list', request=request)  # 'app-list' should match your viewset's URL name

        csrf_token = request.COOKIES.get('csrftoken')

        # If you can't get the token from cookies, you can manually get it from the request object
        if not csrf_token:
            csrf_token = get_token(request)  # This retrieves the CSRF token if it's not in the cookies

        headers = {
            'X-CSRFToken': csrf_token,  # Include the CSRF token in the headers
            'Referer': request.META.get('HTTP_REFERER', ''),  # Optional, but can help with CSRF validation
        }
        # Perform the POST request to the external API (assuming you're posting to an API endpoint)
        req = session.post(url, data=data, files=files, headers=headers)

        # Print the status code and response from the API request
        # print(req.status_code)
        # print(req.text)
