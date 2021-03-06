from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Quiz
from django.contrib import messages

# to show all quiz questions from db
# split betwee pages 5 p.p
def quiz_page(request):
    quizes = Quiz.objects.all()
    paginator = Paginator(quizes, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        quizes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        quizes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        quizes = paginator.page(paginator.num_pages)

    return render(request, 'quiz.html', {"quizes": quizes})


# Quiz question with answers
# previous next allows to move from one question to another
def quiz_answer(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    form = None
    if request.method == 'POST':

        messages.success(request, "Answer: ")
    
    nextquestion = Quiz.objects.filter(id__gt=quiz.id).order_by('id').first()
    previousquestion = Quiz.objects.filter(
        id__lt=quiz.id).order_by('id').last()

    return render(request, "answer.html", {'quiz': quiz, 'form': form,
                                           'nextquestion': nextquestion,
                                           'previousquestion':
                                           previousquestion})
