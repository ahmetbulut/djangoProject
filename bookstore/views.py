from django.shortcuts import render, HttpResponse
from bookstore.models import Author

# Create your views here.
def add_author(request):
    # we are going to get this information via a web form.
    input_firstname = "Z"
    input_lastname = "G"
    input_email = "z.g@boun.edu.tr"

    a = Author(first_name=input_firstname, last_name=input_lastname, email=input_email)
    a.save()

    return HttpResponse(str(a) + ' saved to the database!')

def all_authors(request):
    authors_list = Author.objects.all()
    return render(request, "authors.html", {'authors_list': authors_list})

def author_search(request):
    result_set = Author.objects.filter(email__contains='boun.edu.tr', last_name__contains= 'G')
    return HttpResponse(result_set)