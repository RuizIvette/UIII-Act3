from django.shortcuts import render,redirect, get_object_or_404
from .models import Cliente, Mascota # ¡Solo importamos Cliente!

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

# ==========================================
# FUNCIONES CRUD PARA MASCOTAS (NUEVO)
# ==========================================

def ver_mascotas(request):
    mascotas = Mascota.objects.select_related('cliente').all().order_by('nombre')
    context = {'mascotas': mascotas}
    return render(request, 'mascota/ver_mascotas.html', context)

def agregar_mascota(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre') # Necesitamos los clientes para el select
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        raza = request.POST.get('raza')
        cliente_id = request.POST.get('cliente') # Obtenemos el ID del cliente seleccionado

        if nombre and tipo and cliente_id:
            cliente = get_object_or_404(Cliente, pk=cliente_id) # Obtenemos la instancia del Cliente
            Mascota.objects.create(nombre=nombre, tipo=tipo, raza=raza, cliente=cliente)
            return redirect('ver_mascotas')
        else:
            context = {'error': 'Por favor, completa todos los campos obligatorios.', 'clientes': clientes}
            return render(request, 'mascota/agregar_mascota.html', context)
    context = {'clientes': clientes}
    return render(request, 'mascota/agregar_mascota.html', context)

def actualizar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    clientes = Cliente.objects.all().order_by('apellido', 'nombre') # Necesitamos todos los clientes
    if request.method == 'POST':
        mascota.nombre = request.POST.get('nombre')
        mascota.tipo = request.POST.get('tipo')
        mascota.raza = request.POST.get('raza')
        cliente_id = request.POST.get('cliente')

        if cliente_id:
            mascota.cliente = get_object_or_404(Cliente, pk=cliente_id)
        mascota.save()
        return redirect('ver_mascotas')
    context = {'mascota': mascota, 'clientes': clientes}
    return render(request, 'mascota/actualizar_mascota.html', context)

def borrar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('ver_mascotas')
    context = {'mascota': mascota}
    return render(request, 'mascota/borrar_mascota.html', context)