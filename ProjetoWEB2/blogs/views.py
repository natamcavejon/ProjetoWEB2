from django.shortcuts import render,redirect
from .models import Blogs,Coment
from .forms import Comentarios

def home(request): # Cria a home da APP
    
    blogs=Blogs.objects.all().order_by('-id')
    return render(request, 'home.html',{'blogs':blogs})

def noticia (request,id):
    noticia= Blogs.objects.get(id=id)
    coment = Coment.objects.all().filter(noticia=id)
    form = Comentarios(request.POST or None)

    if form.is_valid():
        coment= form.save(commit=False)
        coment.noticia_id=noticia.id
        coment.save()
        return redirect('noticias',id)
    return render(request,'noticias.html',{'noticia':noticia,'form':form,'comentarios':coment})


def listar_blogs(request):
    blogs=Blogs.objects.all()
    return render(request,'noticias.html',{'blogs':blogs})





# Create your views here.
