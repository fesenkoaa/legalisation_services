from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib import messages

import requests
from .config import token, chat_id


class MainPageView(View):

    def get(self, request):
        page_obj = Article.objects.all()[:3]
        image = AppImage.objects.all()

        chapters = Category.objects.all().order_by('id')
        want = Category.objects.filter(chapter='want').order_by('place')
        already = Category.objects.filter(chapter='already').order_by('place')

        context = {
            'page_obj': page_obj,
            'chapters': chapters,
            'want': want,
            'already': already,
            'image': image
        }
        return render(request, 'main.html', context)


class AdvisesPageView(ListView):

    model = Advises
    template_name = 'articles.html'
    paginate_by = 5

    chapters = Category.objects.all()
    want = Category.objects.filter(chapter='want')
    already = Category.objects.filter(chapter='already')
    extra_context = {
        'chapters': chapters,
        'want': want,
        'already': already
    }

    # def get(self, request):
    #     page_obj = Advises.objects.all()
    #
    #     chapters = Category.objects.all()
    #     want = Category.objects.filter(chapter='want')
    #     already = Category.objects.filter(chapter='already')
    #
    #     context = {
    #         'page_obj': page_obj,
    #         'chapters': chapters,
    #         'want': want,
    #         'already': already
    #     }
    #     return render(request, 'articles.html', context)


class AllArticlesPageView(ListView):

    model = Article
    template_name = 'articles.html'
    paginate_by = 5

    chapters = Category.objects.all()
    want = Category.objects.filter(chapter='want')
    already = Category.objects.filter(chapter='already')
    extra_context = {
        'chapters': chapters,
        'want': want,
        'already': already
    }


class ChooseCategoryPageView(View):

    def get(self, request):
        chapters = Category.objects.all()
        want = Category.objects.filter(chapter='want')
        already = Category.objects.filter(chapter='already')

        context = {
            'chapters': chapters,
            'want': want,
            'already': already
        }
        return render(request, 'categories.html', context)


class CategoryArticlePageView(View):

    def get(self, request, pk):
        page_obj = Article.objects.filter(category=pk)

        chapters = Category.objects.all()
        want = Category.objects.filter(chapter='want')
        already = Category.objects.filter(chapter='already')

        context = {
            'page_obj': page_obj,
            'chapters': chapters,
            'want': want,
            'already': already
        }
        return render(request, 'articles.html', context)


class TheArticlePageView(View):

    def get(self, request, pk):
        page_obj = Article.objects.filter(id=pk).first()
        form = ReviewsForm

        chapters = Category.objects.all()
        want = Category.objects.filter(chapter='want')
        already = Category.objects.filter(chapter='already')

        context = {
            'page_obj': page_obj,
            'chapters': chapters,
            'want': want,
            'already': already,
            'from': form
        }
        return render(request, 'article.html', context)


class ReviewsPageView(View):

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
        return render(request, 'reviews.html', context)

    def post(self, request):
        page_obj = Reviews.objects.all().order_by('-time')

        chapters = Category.objects.all()
        want = Category.objects.filter(chapter='want')
        already = Category.objects.filter(chapter='already')

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

            messages.success(request, 'ваш комментарий был отправлен')
            return HttpResponseRedirect(reverse('ru:reviews'))

        return render(request, 'reviews.html', context)


class ContactPageView(View):

    def get(self, request):
        form = ContactForm

        chapters = Category.objects.all()
        want = Category.objects.filter(chapter='want')
        already = Category.objects.filter(chapter='already')

        context = {
            'chapters': chapters,
            'want': want,
            'already': already,
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request):
        form = ContactForm

        chapters = Category.objects.all()
        want = Category.objects.filter(chapter='want')
        already = Category.objects.filter(chapter='already')

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

            msg = f'TTC SERVICE : CONTACT (ru)\n\n' \
                  f'auth: {auth}\n' \
                  f'phone: {phone}\n' \
                  f'message: \n\n' \
                  f'"{message}"'
            send = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}')

            print(f'    echo:  {auth} ({phone}) want to contact "TTConsulting Documents"')

            messages.success(request, 'мы вам позвоним')
            return HttpResponseRedirect(reverse('ru:contact'))

        return render(request, 'contact.html', context)


class ServicesPageView(View):

    def get(self, request):
        work = Services.objects.filter(category=1)
        family = Services.objects.filter(category=2)
        other = Services.objects.filter(category=3)

        chapters = Category.objects.all()
        want = Category.objects.filter(chapter='want')
        already = Category.objects.filter(chapter='already')
        context = {
            'chapters': chapters,
            'want': want,
            'already': already,

            'work': work,
            'family': family,
            'other': other
        }

        return render(request, 'services.html', context)