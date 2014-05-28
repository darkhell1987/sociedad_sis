from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.template import RequestContext
from models import *
from forms import *
from sociedad.settings import RUTA_PROYECTO
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import os
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
import time
from calendar import month_name
from django.forms import ModelForm
from django.core.context_processors import csrf
# Create your views here.
                #para el raiting con estrellas
                #from django.utils.emcoding import StrAndUnicode, force_unicode
                #from django.utils.html import conditional_escape
                #from django.utils.safestring import mark_safe

                #def tag(self):
                #    if 'id' in self.attrs:
                #        self.attrs['id'] = '%s_%s' %(self.attrs['id'],self.index)
                #        final_attrs = dict(self.attrs,type ='radio', name = self.name, value = self.choice_value)
                #    if self.is_checked():
                #        final_attrs['checked'] = 'checked'
                #    return mark_safe(u'<input%s />' % flatatt(final_attrs))
                #def render(self):
                #    return mark_safe(u'\n%s\n' % u'\n'.join([u'%s' % force_unicode(w) for w in self]))

                #def save(self , *args, **kwargs):
                #    myobject.rating.add(score=self.rating, user = self.user, ip_address = self.ip_address)
                #    super(CommentWithRating, self).save(*args, **kwargs)
                #fin de las estrellas

def registro(request):
	if request.method == 'POST':
		formulario=UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=UserCreationForm()
	return render_to_response('registro.html',{'formulario':formulario},RequestContext(request))

def index(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response ('noactivo.html',context_instance = RequestContext(request))
            else:
                return render_to_response ('nousuario.html',context_instance = RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response(("index.html","base.html"),{'formulario':formulario},RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario=request.user
    return render_to_response('privado.html',{'usuario':usuario},RequestContext(request))


@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


def noticias(request):
	return render_to_response("noticias.html",{},RequestContext(request))

#================================  BLOG ======================================#
def poncomentario(request, pk):
    p = request.POST

    if 'mensaje' in p:
        autor = "Anonimo"
        if p["autor"]: autor = p["autor"]
        comentario = Comentar(requerir=entrada.objects.get(pk=int(pk)))
        cf = FormularioComentario(p, instance=comentario)
        cf.fields["autor"].required = False

        comentario = cf.save(commit=False)
        comentario.autor = autor
        comentario.save()
    return HttpResponseRedirect(reverse("sociedad.apps.blog.views.Entrada", args=[pk]))

def mkmonth_lst():
    if not entrada.objects.count(): return[]

    year, month = time.localtime()[:2]
    first = entrada.objects.order_by("fecha_entrada")[0]
    fyear = first.fecha_entrada.year
    fmonth = first.fecha_entrada.month
    months = []

    for y in range(year,fyear-1,-1):
        start,end = 12,0
        if y == year:start = month
        if y == fyear: end = fmonth -1

        for m in range(start,end,-1):
            months.append((y,m,month_name[m]))
        
    return months

def month(request,year,month):
    ontrada = entrada.objects.filter(fecha__year=year,fecha__month=month)
    return render_to_response("blog.html",dict(entrada_list=ontrada,usuario=request.user,month=mkmonth_lst(),archive=True))

def Entrada(request, pk):
    identrada = entrada.objects.get(pk=int(pk))
    comentario = Comentar.objects.filter(requerir = identrada)
    d = dict(entrada= identrada,comentario = comentario,form=FormularioComentario(),usuario=request.user)
    d.update(csrf(request))
    return render_to_response("entrada.html",d)

def blog(request):
    intrada = entrada.objects.all().order_by("-fecha_entrada")
    paginator = Paginator(intrada,3)

    try: pagina = int(request.GET.get("page",'1'))
    except ValueError: pagina = 1

    try:
        intrada = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        intrada = paginator.page(paginator.num_pages)
    return render_to_response("blog.html",dict(entrada = intrada, usuario=request.user,entrada_list = intrada.object_list,months=mkmonth_lst()))

#====================================END BLOG====================================#

#====================================BIBLIOTECA====================================#
def biblioteca(request):
	return render_to_response("biblioteca.html",{},RequestContext(request))
#====================================END BIBLIOTECA====================================#

#====================================ACERCA DE====================================#
def acercade(request):
	return render_to_response("acercade.html",{},RequestContext(request))
#====================================END ACERCA DE====================================#

#====================================PERFIL====================================#
def perfil(request):
    if request.method == 'POST':
        entradas=FormularioEntrada(request.POST, request.FILES)
        print entradas
        if entradas.is_valid():
            entradas.save()
            return HttpResponseRedirect("/blog")
    else: 
        print request.POST
        entradas=FormularioEntrada()
    return render_to_response("perfil.html",{"entradas":entradas},context_instance = RequestContext(request))
#====================================END PERFIL====================================#

