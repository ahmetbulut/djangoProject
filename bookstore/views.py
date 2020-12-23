from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from bookstore.models import Author, Book
from bookstore.forms import AuthorForm

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            a = Author(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/authors/')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def all_authors(request):
    authors_list = Author.objects.all()
    return render(request, "authors.html", {'authors_list': authors_list})

def author_search(request):
    result_set = Author.objects.filter(email__contains='boun.edu.tr', last_name__contains= 'G')
    return HttpResponse(result_set)

def search_form(request):
    return render(request, "search_form.html")

def search(request):
    errors = []
    if request.GET['q']:
        q = request.GET['q']
        print('query', q)
        if q == '':
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})

    return render(request, 'search_form.html', {'errors': errors})
