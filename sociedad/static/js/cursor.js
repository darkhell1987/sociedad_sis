mensaje = 'Ing. Sistemas | UATF';
font = 'MONOTIPE CORSIVA,Arial';
size = 2;
color = '#fafacd';
velocidad = 0.5;
n4 = (document.layers);
ie = (document.all);
n6 = (document.getElementById);
mensaje = mensaje.split('');
n = mensaje.length;
a = size*10;
ymouse = 0;
xmouse = 0;
props = "<font face="+font+" color="+color+" size="+size+" style='text-shadow:0px 5px 5px black'>";
if (n4)
{
for ( i = 0; i < n; i++)
document.write('<layer left="0" top="0" width="+a+" name="n4mensaje'+i+'" height="+a+"><center>'+props+mensaje[i]+'</font></center></layer>');
}
else if (ie)
{
document.write('<div id="padre" style="position:absolute;top:0px;left:0px"><div style="position:relative">');
for (i=0; i < n; i++)
document.write('<div id="iemensaje" style="position:absolute;top:0px;left:0;height:'+a+';width:'+a+';text-align:center">'+props+mensaje[i]+'</font></div>');
document.write('</div></div>');
}
else if (n6)
{
document.write('<div id="padre" style="position:absolute;top:0px;left:0px"><div style="position:relative">');
for (i = 0; i < n; i++)
document.write('<div id="iemensaje'+i+'" style="position:absolute;top:0px;left:0;height:'+a+';width:'+a+';text-align:center">'+props+mensaje[i]+'</font></div>');
document.write('</div></div>');
}
if(n4)
window.captureEvents(Event.MOUSEMOVE);
function Mouse(evento)
{
if(ie)
{
xmouse = event.x+20;
ymouse = event.y+20;
}
else if(n4 || n6)
{
xmouse = evento.pageX+20;
ymouse = evento.pageY+20;
}
}
if(n4)
window.onMouseMove = Mouse
else if(ie || n6)
document.onmousemove = Mouse;
y = new Array();
x = new Array();
Y = new Array();
X = new Array();
Yaux = new Array();
Xaux = new Array();
for (i=0; i < n; i++)
{
y[i] = 0;
x[i] = 0;
Y[i] = 0;
X[i] = 0;
Yaux[i] = 0;
Xaux[i] = 0;
}
function asigna()
{
if (ie)
padre.style.top = document.body.scrollTop;
for (i = 0; i < n; i++)
{
if(n4)
{
document.layers['n4mensaje'+i].top = y[i];
document.layers['n4mensaje'+i].left = x[i]+(i*(a/2));
}
else if(ie)
{
iemensaje[i].style.top = y[i];
iemensaje[i].style.left = x[i]+(i*(a/2));
}
else if(n6)
{
eval("document.getElementById('iemensaje"+i+"').style.top = '"+y[i]+"px'");
eval("document.getElementById('iemensaje"+i+"').style.left = '"+(x[i]+(i*(a/2)))+"px'");
}
}
}
function ondula()
{
y[0]=Math.round(Y[0] +=((ymouse)-Y[0])*velocidad);
x[0]=Math.round(X[0] +=((xmouse)-X[0])*velocidad);
for (var i = 1; i < n; i++)
{
Yaux[i] = Math.round(Y[i]);
Xaux[i ]= Math.round(X[i]);
y[i] = Math.round(Y[i]=Yaux[i]+(y[i-1]-Y[i])*velocidad);
x[i] = Math.round(X[i]=Xaux[i]+(x[i-1]-X[i])*velocidad);
}
asigna();
setTimeout('ondula()',50);
}
window.onload = ondula;