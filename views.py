from django.shortcuts import render

def quiz(request):
    if request.method == 'POST':
        score = 0
        # Check answers
        answer1 = request.POST.get('question1')
        if answer1 == '1':
            score += 5

        answer2 = request.POST.get('question2')
        if answer2 == '4':
            score += 5

        answer3 = request.POST.get('question3')
        if answer3 == '2':
            score += 5

        answer4 = request.POST.get('question4')
        if answer4 == '3':
            score += 5

        answer5 = request.POST.get('question5')
        if answer5 == '2':
            score += 5

        return render(request, 'quiz_result.html', {'score': score})
    else:
        return render(request, 'quiz.html')
