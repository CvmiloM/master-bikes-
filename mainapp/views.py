from django.shortcuts import render, get_object_or_404, redirect
from .models import Solicitud, Cliente, HistorialReparacion
from .forms import ConfirmarSolicitudForm, ClienteForm
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Cliente, Solicitud

def index(request):
    return render(request, 'index.html')
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'solicitudes.html', {'solicitudes': solicitudes})

def detalle_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.method == 'POST':
        form = ConfirmarSolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            solicitud = form.save()
            # Enviar correo electrónico
            if solicitud.estado_actual == 'resuelto':
                asunto = 'Confirmación de reparación'
                mensaje = f'Hola {solicitud.cliente.nombre},\n\nTu bicicleta puede ser reparada. Nos pondremos en contacto contigo pronto.'
            else:
                asunto = 'Rechazo de reparación'
                mensaje = f'Hola {solicitud.cliente.nombre},\n\nLamentamos informarte que tu bicicleta no puede ser reparada.'
            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [solicitud.cliente.email], fail_silently=False)
            return redirect('solicitudes')
    else:
        form = ConfirmarSolicitudForm(instance=solicitud)
    return render(request, 'detalle_solicitud.html', {'solicitud': solicitud, 'form': form})

# Definición de otras vistas aquí

def confirmar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.method == 'POST':
        solicitud.estado_actual = 'resuelto'
        solicitud.save()
        send_mail(
            'Confirmación de reparación',
            f'Hola {solicitud.cliente.nombre},\n\nTu bicicleta puede ser reparada. Nos pondremos en contacto contigo pronto.',
            settings.EMAIL_HOST_USER,
            ['ca.monge@duocuc.cl'],
            fail_silently=False,
        )
        return redirect('solicitudes')
    return render(request, 'confirmar_solicitud.html', {'solicitud': solicitud})

def rechazar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if request.method == 'POST':
        solicitud.estado_actual = 'rechazado'
        solicitud.save()
        send_mail(
            'Rechazo de reparación',
            f'Hola {solicitud.cliente.nombre},\n\nLamentamos informarte que tu bicicleta no puede ser reparada.',
            settings.EMAIL_HOST_USER,
            ['ca.monge@duocuc.cl'],
            fail_silently=False,
        )
        return redirect('solicitudes')
    return render(request, 'rechazar_solicitud.html', {'solicitud': solicitud})

#send_email

def send_email(email):
    send_mail(
        'Confirmación de reparación'
    )


# Elimina o agrega la definición de enviar_correo si es necesario

# mainapp/views.py

from django.shortcuts import render

def historial(request):
    return render(request, 'historial.html')



from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    decorated_view = user_passes_test(
        lambda user: user.is_staff,
        login_url='/login/'
    )(view_func)
    return decorated_view
