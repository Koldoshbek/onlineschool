from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from library.models import Book


class LibraryView(LoginRequiredMixin, TemplateView):
    template_name = 'library/all_books.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        search_by_barcode = request.GET.get('barcode')
        search_by_name = request.GET.get('name')
        search_by_writer = request.GET.get('writer')

        if search_by_barcode:
            books = books.filter(barcode=search_by_barcode)
        if search_by_name:
            books = books.filter(name__icontains=search_by_name)
        if search_by_writer:
            books = books.filter(writer__icontains=search_by_writer)

        context = {
            'books': books,
        }
        return render(request, self.template_name, context)


class AddBookView(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('library')
    template_name = 'library/add_book.html'
