from django.shortcuts import render, redirect
from .forms import TextInputForm
from .models import Text

def word_counter(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            text_instance = form.save()

            # Count words in the entered text
            word_count = len(text_instance.content.split())

            # Add the word count to the model instance and save it
            text_instance.word_count = word_count
            text_instance.save()

            return redirect('word_counter')
    else:
        form = TextInputForm()

    texts = Text.objects.all()
    return render(request, 'wordcounterapp/word_counter.html', {'form': form, 'texts': texts})
