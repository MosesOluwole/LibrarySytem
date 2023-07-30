# library/views.py


from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book, Member, Borrow
from .forms import BookForm, MemberForm


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})


def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit_member.html', {'form': form, 'member': member})


def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'delete_member.html', {'member': member})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})


def borrow_book(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        member_id = request.POST['member_id']
        borrowed_date = timezone.now()  # Get the current date and time
        Borrow.objects.create(
            book_id=book_id, member_id=member_id, borrowed_date=borrowed_date)

    books = Book.objects.all()
    members = Member.objects.all()
    return render(request, 'borrow_book.html', {'books': books, 'members': members})


def return_book(request):
    if request.method == 'POST':
        borrow_id = request.POST['borrow_id']
        borrow = Borrow.objects.get(id=borrow_id)
        borrow.return_date = timezone.now()
        borrow.save()
    borrowed_books = Borrow.objects.filter(return_date=None)
    return render(request, 'return_book.html', {'borrowed_books': borrowed_books})
