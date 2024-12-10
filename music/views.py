from django.shortcuts import render, redirect, get_object_or_404
from .models import Music


def home(request):
    return render(request, 'index.html')


def music_list(request):
    music = Music.objects.all()
    ctx = {'music': music}
    return render(request, 'music/music-list.html', ctx)


def music_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        data = request.POST.get('data')
        genre = request.POST.get('genre')
        if title and artist and data and genre:
            Music.objects.create(
                title = title,
                artist = artist,
                data = data,
                genre = genre,
        )
        return redirect('music:list')
    return render(request, 'music/music-form.html')


def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)
    ctx = {'music': music}
    return render(request, 'music/detail.html', ctx)

def music_update(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        data = request.POST.get('data')
        genre = request.POST.get('genre')
        if title and artist and data and genre:
            music.title = title
            music.artist = artist
            music.data = data
            music.genre = genre
            music.save()
            return redirect(music.get_detail_url())
    ctx = {'music': music}
    return render(request, 'music/music-form.html', ctx)



def music_delete(request, pk):
    music = get_object_or_404(Music, pk=pk)
    music.delete()
    return redirect('music:list')

