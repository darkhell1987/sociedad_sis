from django.db import models
#from django.ratings.fields import RatingField
#from django.forms.util import flatatt
# Create your models here.

class entrada(models.Model):
    titulo=models.CharField(max_length=100)
    imagen=models.FileField(upload_to='img_entrada')
    comentario = models.TextField()
    fecha_entrada=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.titulo
class Comentar(models.Model):
    requerir = models.ForeignKey(entrada)
    fechacreado = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    mensaje = models.TextField()

    def __unicode__(self):
        return '%s %s ' %(self.requerir,self.mensaje)

#class misclases(model.Model):
 #   rating = RatingField(range=5)