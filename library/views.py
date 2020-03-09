from django.shortcuts import render
from django.views.generic import TemplateView

from library.models import Book


class LibraryView(TemplateView):
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
