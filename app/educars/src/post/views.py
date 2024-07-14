from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('#')  # Substitua pelo nome da URL de sucesso
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
