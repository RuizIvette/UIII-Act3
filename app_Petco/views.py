from django.shortcuts import render,redirect, get_object_or_404
from .models import Cliente # ¡Solo importamos Cliente!

# Create your views here.
def inicio_petco(request):
    # Esta es la vista para la página de inicio
    return render(request, 'inicio.html')

# ==========================================
# FUNCIONES CRUD PARA CLIENTES
# ==========================================

def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    context = {'clientes': clientes}
    return render(request, 'cliente/ver_clientes.html', context)

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        if nombre and apellido and email:
            try:
                Cliente.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono, direccion=direccion)
                return redirect('ver_clientes')
            except Exception as e:
                context = {'error': f'Ocurrió un error al guardar el cliente: {e}'}
                return render(request, 'cliente/agregar_cliente.html', context)
        else:
            context = {'error': 'Por favor, completa todos los campos obligatorios (Nombre, Apellido, Email).'}
            return render(request, 'cliente/agregar_cliente.html', context)
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        try:
            cliente.save()
            return redirect('ver_clientes')
        except Exception as e:
            context = {'cliente': cliente, 'error': f'Ocurrió un error al actualizar el cliente: {e}'}
            return render(request, 'cliente/actualizar_cliente.html', context)
    context = {'cliente': cliente}
    return render(request, 'cliente/actualizar_cliente.html', context)

def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        try:
            cliente.delete()
            return redirect('ver_clientes')
        except Exception as e:
            context = {'cliente': cliente, 'error': f'Ocurrió un error al eliminar el cliente: {e}'}
            return render(request, 'cliente/borrar_cliente.html', context)
    context = {'cliente': cliente}
    return render(request, 'cliente/borrar_cliente.html', context)