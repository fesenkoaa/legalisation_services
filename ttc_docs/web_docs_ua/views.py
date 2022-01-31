from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.contrib import messages
from web_docs.models import *
import requests
from config import token, chat_id


class UaMainPageView(View):

    def get(self, request):
        page_obj = ArticleUa.objects.all()[:5]

        chapters = CategoryUa.objects.all().order_by('id')
        want = CategoryUa.objects.filter(chapter='want').order_by('place')
        already = CategoryUa.objects.filter(chapter='already').order_by('place')

        context = {
            'page_obj': page_obj,
            'chapters': chapters,
            'want': want,
            'already': already
        }
        return render(request, 'ua-main.html', context)


class UaAdvisesPageView(ListView):

    model = AdvisesUa
    template_name = 'ua-articles.html'
    paginate_by = 5

    chapters = CategoryUa.objects.all()
    want = CategoryUa.objects.filter(chapter='want')
    already = CategoryUa.objects.filter(chapter='already')
    extra_context = {
        'chapters': chapters,
        'want': want,
        'already': already
    }

    # def get(self, request):
    #     page_obj = AdvisesUa.objects.all()
    #
    #     chapters = CategoryUa.objects.all()
    #     want = CategoryUa.objects.filter(chapter='want')
    #     already = CategoryUa.objects.filter(chapter='already')
    #
    #     context = {
    #         'page_obj': page_obj,
    #         'chapters': chapters,
    #         'want': want,
    #         'already': already
    #     }
    #     return render(request, 'ua-articles.html', context)


class UaAllArticlesPageView(ListView):

    model = ArticleUa
    template_name = 'ua-articles.html'
    paginate_by = 5

    chapters = CategoryUa.objects.all()
    want = CategoryUa.objects.filter(chapter='want')
    already = CategoryUa.objects.filter(chapter='already')
    extra_context = {
        'chapters': chapters,
        'want': want,
        'already': already
    }


class UaChooseCategoryPageView(View):

    def get(self, request):
        chapters = CategoryUa.objects.all()
        want = CategoryUa.objects.filter(chapter='want')
        already = CategoryUa.objects.filter(chapter='already')

        context = {
            'chapters': chapters,
            'want': want,
            'already': already
        }
        return render(request, 'ua-categories.html', context)


class UaCategoryArticlePageView(View):

    def get(self, request, pk):
        page_obj = ArticleUa.objects.filter(category=pk)

        chapters = CategoryUa.objects.all()
        want = CategoryUa.objects.filter(chapter='want')
        already = CategoryUa.objects.filter(chapter='already')

        context = {
            'page_obj': page_obj,
            'chapters': chapters,
            'want': want,
            'already': already
        }
        return render(request, 'ua-articles.html', context)


class UaTheArticlePageView(View):

    def get(self, request, pk):
        page_obj = ArticleUa.objects.filter(id=pk).first()

        chapters = CategoryUa.objects.all()
        want = CategoryUa.objects.filter(chapter='want')
        already = CategoryUa.objects.filter(chapter='already')

        context = {
            'page_obj': page_obj,
            'chapters': chapters,
            'want': want,
            'already': already
        }
        return render(request, 'ua-article.html', context)


class UaReviewsPageView(View):

    def get(self, request):
        page_obj = Reviews.objects.all().order_by('-time')
        form = ReviewsForm

        chapters = Category.objects.all()
        want = Category.objects.filter(chapter='want')
        already = Category.objects.filter(chapter='already')

        context = {
            'page_obj': page_obj,
            'chapters': chapters,
            'want': want,
            'already': already,
            'form': form
        }
        return render(request, 'ua-reviews.html', context)

    def post(self, request):
        page_obj = Reviews.objects.all().order_by('-time')
        form = ReviewsForm

        chapters = CategoryUa.objects.all()
        want = CategoryUa.objects.filter(chapter='want')
        already = CategoryUa.objects.filter(chapter='already')

        form = ReviewsForm(request.POST)
        context = {
            'page_obj': page_obj,
            'chapters': chapters,
            'want': want,
            'already': already,
            'form': form
        }

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            auth = form.cleaned_data['auth']
            print(f'    echo:  {auth} {email} send new comment')

            messages.success(request, 'ваш коментар надіслано')
            return HttpResponseRedirect(reverse('ua:reviews'))

        return render(request, 'reviews.html', context)


class UaContactPageView(View):

    def get(self, request):
        form = ContactForm

        chapters = CategoryUa.objects.all()
        want = CategoryUa.objects.filter(chapter='want')
        already = CategoryUa.objects.filter(chapter='already')

        context = {
            'chapters': chapters,
            'want': want,
            'already': already,
            'form': form
        }
        return render(request, 'ua-contact.html', context)

    def post(self, request):
        form = ContactForm

        chapters = CategoryUa.objects.all()
        want = CategoryUa.objects.filter(chapter='want')
        already = CategoryUa.objects.filter(chapter='already')

        form = ContactForm(request.POST)
        context = {
            'chapters': chapters,
            'want': want,
            'already': already,
            'form': form
        }

        if form.is_valid():
            form.save()
            auth = form.cleaned_data['first_name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            msg = f'TTC SERVICE : CONTACT (ua)\n\n' \
                  f'auth: {auth}\n' \
                  f'phone: {phone}\n' \
                  f'message: \n\n' \
                  f'"{message}"'
            send = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}')

            print(f'    echo:  {auth} ({phone}) want to contact "TTConsulting Documents"')

            messages.success(request, 'ми вам зателефонуємо')
            return HttpResponseRedirect(reverse('ua:contact'))

        return render(request, 'ua-contact.html', context)


class UaServicesPageView(View):

    def get(self, request):
        work = Services.objects.filter(category=1)
        family = Services.objects.filter(category=2)
        other = Services.objects.filter(category=3)

        chapters = CategoryUa.objects.all()
        want = CategoryUa.objects.filter(chapter='want')
        already = CategoryUa.objects.filter(chapter='already')
        context = {
            'chapters': chapters,
            'want': want,
            'already': already,

            'work': work,
            'family': family,
            'other': other
        }

        return render(request, 'ua-services.html', context)