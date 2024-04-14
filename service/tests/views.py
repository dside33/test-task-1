from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, TestSet
from .forms import TestForm
from django.contrib.auth.decorators import login_required



@login_required(login_url='/users/login/')
def start_test(request):
    request.session['current_test_id'] = 1

    test_sets = TestSet.objects.all()

    return render(request, 'tests/test_main.html', {'sets': test_sets})
    # return redirect('test_detail', test_id=1)


@login_required(login_url='/users/login/')
def result_test(request, set_id):
    tests = TestSet.objects.filter(id=set_id).first().test.all()
    # tests = test_set.tests.all()

    return render(request, 'tests/result_test.html', {'tests': tests})


@login_required(login_url='/users/login/')
def test_view(request, set_id, test_id):
    if test_id != request.session['current_test_id']:
        return render(request, 'tests/test.html', {
            'isCurrent': False,
            'current_quest': request.session['current_test_id'],
        })
    
    test_set = get_object_or_404(TestSet, id=set_id)
    tests_in_set = test_set.test.all()
    test = get_object_or_404(tests_in_set, id=test_id)

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer.lower() == test.answer:
                test.isCorrect = True
                test.save()

            if test_id == tests_in_set.count():
                return redirect('result_tests', set_id=set_id)
            
            request.session['current_test_id'] += 1
            return redirect('test_detail', set_id=set_id, test_id=test_id + 1)  # Переходим к следующему тесту
    else:
        form = TestForm()

    return render(request, 'tests/test.html', {
        'form': form, 
        'test': test, 
        'isCurrent': True,
    })