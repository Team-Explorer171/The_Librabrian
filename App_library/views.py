from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Sum
from datetime import date
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import UpdateView

from App_library.models import Book, Category, Student, Borrow
from App_library.forms import *


# Create your views here.
def index(request):
    return render(request, "App_library/Home.html")


@login_required
def categories(request):
    if request.method == "POST":
        title = request.POST.get('title')
        cat = Category(title=title)
        cat.save()
        return HttpResponseRedirect(reverse('App_library:categories'))
    all_categories = Category.objects.all()
    return render(request, "App_library/category.html", context={"categories": all_categories})


@login_required
def delete_category(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('App_library:categories'))


@login_required
def edit_category(request, id):
    category = Category.objects.filter(id=id).get()
    if request.method == 'POST':
        cat_title = request.POST.get('title')
        category.title = cat_title
        category.save()
        return HttpResponseRedirect(reverse('App_library:categories'))
    return render(request, 'App_library/edit_category.html', context={'category': category})


def books(request):
    form = AddBookForm()
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    all_books = Book.objects.all()
    all_categories = Category.objects.all()
    return render(request, "App_library/books.html", {"books": all_books, "categories": all_categories, 'form': form})


def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookEditForm(instance=book)
    if request.method == "POST":
        form = BookEditForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_library:books'))
    return render(request, 'App_library/book_edit.html', context={'form': form})


def delete_book(request, id):
    book = Book.objects.filter(id=id).get()
    book.delete()
    return redirect("/books")


def students(request):
    if request.method == "POST":
        sid = request.POST["sid"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        department = request.POST["department"]
        section = request.POST["section"]
        year = request.POST["year"]

        student = Student(student_id=sid, firstname=firstname, lastname=lastname, department=department,
                          section=section, year=year)
        student.save()
        return redirect("/students")
    all_students = Student.objects.all()
    return render(request, "App_library/students.html", context={"students": all_students})


def borrow(request):
    # if request.method == "POST":
    #     student_id = request.POST['student_id']
    #     student = Student.objects.get(id=student_id)
    #     print(student)
    #     status = "Borrowed"
    #     books_id = request.POST.getlist('selector')
    #     for book_id in books_id:
    #         book = Book.objects.get(id=book_id)
    #         b = Borrow(qty=1, status=status)
    #         b.save()
    #         b.student = student
    #         b.book = book
    #         return redirect("/borrow")
    form = BookBorrowForm()
    if request.method == "POST":
        form = BookBorrowForm(request.POST)
        if form.is_valid():
            bro = form.save(commit=False)
            bro.status = "Borrowed"
            bro.save()
            return HttpResponseRedirect(reverse('App_library:borrow'))
    _students = Student.objects.all()
    _books = Book.objects.all()
    datas = []
    for book in _books:
        left = Borrow.objects.filter(status="Borrowed", book__title=book.title).aggregate(Sum('qty'))
        if left['qty__sum'] is None:
            l = 0
        else:
            l = int(left['qty__sum'])
        datas.append(book.available - l)
    all_datum = zip(_books, datas)
    return render(request, "App_library/borrow.html", {"datas": all_datum, "students": students, 'form': form})


def returning(request):
    if request.method == "POST":
        b_id = int(request.POST["borrow_id"])
        _borrow = Borrow.objects.get(id=b_id)
        _borrow.date = datetime.now()
        _borrow.status = "Returned"
        _borrow.save()
        return HttpResponseRedirect(reverse('App_library:returning'))
    borrows = Borrow.objects.all()
    return render(request, "App_library/return.html", {"borrows": borrows})
