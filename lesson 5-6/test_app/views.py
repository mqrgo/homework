from django.shortcuts import render
from django.db.models import Sum, Avg, Q, Count, F, Min, Max
from test_app.models import Author, Book



# Create your views here.
# def date_time_response(request):
#     return render(request, 'test_app/index.html')

# def test_upload(request):
#     if request.method == 'POST':
#         form = AddAuthorForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             author = Author(**cd)
#             author.save()
#     else:
#         form = AddAuthorForm()
#     return render(request, 'test_app/upload_test.html', {'form': form})


def index(request):
    #1 all()
    all_authors = Author.objects.all()
    
    #2 get()
    single_author = Author.objects.get(first_name='Николай', last_name='Гоголь')
    
    #3 filter()
    oscars_books = Book.objects.filter(author__last_name='Уальд')
    
    #4 count()
    num_books = Book.objects.all().count()
    
    #5 exclude()
    authors_except_russia = Author.objects.exclude(where_from='RU')
    
    #6 order_by()
    authors_order_by_date = Author.objects.all().order_by('-birth_date', 'first_name')
    
    #7 first()
    first_book = Book.objects.first()
    
    #8 __month
    books_published_in_may = Book.objects.filter(published__month=5)
    
    #9 __startswith
    books_that_starts_with_b = Book.objects.filter(name__startswith='Б')
    
    #10 Sum()
    sum_of_books = Book.objects.aggregate(total=Sum('price'))
    
    #11 Avg()
    avg_books_sum = Book.objects.aggregate(avg=Avg('price'))
    
    #12 lowest price book
    lowest_price_book = Book.objects.order_by('price').first()
    
    #13 highest price book
    highest_price_book = Book.objects.order_by('-price').first()
    
    #14 __gt
    books_with_price_over = Book.objects.filter(price__gt=500).order_by('-price')
    
    #15 latest()
    latest_book_in_db = Book.objects.order_by('published').last()
    
    #16 доступ по внешнему ключу + distinct
    drama_authors = Author.objects.filter(book__genre='Dra').distinct()
    
    #17 __icontains
    books_that_contains = Book.objects.filter(name__icontains='ра')
    
    #18 __in
    book_with_price = Book.objects.filter(price__in=(450, 600, 3200)).order_by('-price')
   
    #19 __isnull
    books_with_covers = Book.objects.filter(cover__isnull=False)   
    
    #20 Q |
    q = Q(genre='Nov') | Q(genre='Poe')
    poe_nov_books = Book.objects.filter(q)
    
    #21 limit
    books_limit = Book.objects.all()[2:5]
    
    #22 annotate + Count
    author_book_count = Author.objects.annotate(count = Count('book')).order_by('-count')
    
    #23 F
    books_with_discount = Book.objects.annotate(price_with_disc=F('price') * 0.85 ).order_by('-price_with_disc')
    
    #24 exist?
    book_exist = Book.objects.filter(name='Одисей').exists()
    
    #25 diff
    price_diff = Book.objects.aggregate(diff=Max('price') - Min('price'))
    
    context = {
        'all_authors': all_authors,
        'single_author': single_author,
        'oscars_books': oscars_books,
        'num_books': num_books,
        'authors_except_russia': authors_except_russia,
        'authors_order_by_date': authors_order_by_date,
        'first_book': first_book,
        'books_published_in_may': books_published_in_may,
        'books_that_starts_with_b': books_that_starts_with_b,
        'sum_of_books': sum_of_books,
        'avg_books_sum': avg_books_sum,
        'lowest_price_book': lowest_price_book,
        'highest_price_book': highest_price_book,
        'books_with_price_over': books_with_price_over,
        'latest_book_in_db': latest_book_in_db,
        'drama_authors': drama_authors,
        'books_that_contains': books_that_contains,
        'book_with_price': book_with_price,
        'books_with_covers': books_with_covers,
        'poe_nov_books': poe_nov_books,
        'books_limit': books_limit,
        'author_book_count': author_book_count,
        'books_with_discount': books_with_discount,
        'book_exist': book_exist,
        'price_diff': price_diff,
    }
    return render(request, 'test_app/index.html', context)

    