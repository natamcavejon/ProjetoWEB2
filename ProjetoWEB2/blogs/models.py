from django.db import models

class Blogs (models.Model):
    title=models.CharField(max_length=100)
    intro=models.TextField()
    noticia=models.TextField()
    img=models.CharField(max_length=500)
    img2=models.CharField(max_length=500)

    def _str_(self):
        return self.nome

class Coment(models.Model):
    nome=models.TextField()
    comentario=models.TextField()
    noticia= models.ForeignKey(Blogs,default="",on_delete=models.CASCADE,related_name="cmm")

    def _str_(self):
        return self.nome


# Create your models here.
