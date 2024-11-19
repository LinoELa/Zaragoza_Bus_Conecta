from django.shortcuts import render

# logIn - logOut 
from django.shortcuts import redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages


#Register User 
from .formularios import FormRegistro


from .models import historial 

# 13 E 
from .formularios import FormAgregar


# Scraping
from bs4 import BeautifulSoup
import requests
from django.shortcuts import get_object_or_404











# --------------------------------- INICIO  ----------------------------------------------#
def inicio(request):
    modelo_historial = historial.objects.all()
    
    return render(request, "inicio.html", {"modelo":modelo_historial})


# --------------------------------- HOME    ----------------------------------------------#
def home(request):
    return render(request, "home.html", {}) #Al iniciar seccion



# --------------------------------- INICIAR SESION ----------------------------------------------#

def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "¡Enhorabuena, has Iniciado Sesión!")

            return redirect("inicio")
        
        else:
            messages.error(request, "¡Error al Iniciar Sescion, Intenntelo de nuevo!")

    return render (request,"form_login.html", {})


# --------------------------------- CERRAR SESION ----------------------------------------------#
def logout_user(request):

    logout(request)
    messages.success(request, "Has Cerrado Sesion")

    return redirect ("home")


# --------------------------------- REGISTRO USUARIO ----------------------------------------------#


def register_user(request):

    if request.method == "POST":

        formulario_registro = FormRegistro(request.POST)

        if formulario_registro.is_valid():
            formulario_registro.save()

        
            # Conger la informacion del fomulario para  Autentificacion 
            nombre_ususario = formulario_registro.cleaned_data['username']
            password_usuario = formulario_registro.cleaned_data['password1']

            # Para que se autentifique he inicie sesion directamete 
            usuario = authenticate(username = nombre_ususario , password = password_usuario )

            login(request, usuario)


            messages.success(request, 'Registro con exito!')

            return redirect ('home')
    else:
        formulario_registro = FormRegistro()

        return render(request, 'register.html', {'formulario':formulario_registro})
    

    return render(request, 'register.html', {'formulario':formulario_registro})


# --------------------------------- BORRAR USUARIO ----------------------------------------------#

# 12  B
def borrar_user(request,pk):

    if request.user.is_authenticated:

        borrar = historial.objects.get(id=pk)
        borrar.delete()

        messages.success(request,'Registro eliminado!' )
        return redirect('inicio')
    else:
        messages.error(request, 'Debe iniciar sesión')
        return redirect('home')
    

# --------------------------------- AGREGAR CONTENIDO ----------------------------------------------#
    
# 13 B
def agregar_user(request):
    # 13 
    formulario_agregar = FormAgregar(request.POST or None)

    if request.user.is_authenticated:

        if request.method == 'POST':

            if formulario_agregar.is_valid():
                formulario_agregar.save()

                messages.success(request, 'Contenido Agregado')
                return redirect('inicio')
            
        return render (request, 'agregar.html', {'formulario':formulario_agregar}) 
    else:
        messages.error(request, 'Debe iniciar sesión')
        return redirect ('home')

# --------------------------------- ACTUALIZAR USER ----------------------------------------------#


# 14 B 
def actualizar_user(request, pk):


    if request.user.is_authenticated:

        id_modelo = historial.objects.get(id=pk)

                #  {POST} = Si hacen algo , {None} = Si no hacen nada  , {instance} = que aparezca el id a cambiar 
        formulario = FormAgregar(request.POST or None, instance=id_modelo)
        
        if formulario.is_valid():
            formulario.save()

            messages.success(request, 'Contenido Actualizado!')
            return redirect ('inicio')
        
        return render (request, 'actualizar.html', {'actualizar':formulario})
        
    else:
        messages.error(request, 'Debe iniciar sesión')
        return redirect ('home')


# -----------------------------------------------------LOGIN SOFTWARE -------------------------------------------------------------- #
#RECTORIZACION 
def obtener_datos_poste(poste_int):
    url = f"https://zaragoza-pasobus.avanzagrupo.com/frm_esquemaparadatime.php?poste={poste_int}"
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    datos = response.text
    soup = BeautifulSoup(datos, 'lxml')

    bus_web_apuntar = [
        td.get_text() for td in soup.find_all('td', class_='digital') 
        if not td.find('svg') and td.attrs and td.get_text().strip() != ''
    ]

    linea = bus_web_apuntar[0::3]
    destino = bus_web_apuntar[1::3]
    tiempo = bus_web_apuntar[2::3]

    return list(zip(linea, destino, tiempo))

# LOGICA 
def modelos_user(request, pk):
    if request.user.is_authenticated:
        
        modelo_individual = get_object_or_404(historial, id=pk)

        contexto = {
            'modelo_individual':modelo_individual,
        }

        for i in range (1 ,4): #porque solo hay 3 postes
            poste_string = getattr(modelo_individual , f"poste_{i}", None)

            if poste_string:
                try:
                    poste_int = int(poste_string)
                    datos = obtener_datos_poste(poste_int) 
                    contexto[f"datos_{i}"] = datos
                except ValueError:
                    print("f Error : 'poste_{i}' valor '{poste_string}' no es un numero entero ")
            
            else : 
                break

        return render (request, 'modelos.html',contexto)
    else:
        messages.error(request, 'Tienes que iniciar sesion')
        return redirect('inicio')


# -----------------------------------------------------LOGIC SOFTWARE -------------------------------------------------------------- #




