# family_members/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # Decorador para requerir inicio de sesión
from django.contrib import messages
from .models import FamilyMember
from .forms import FamilyMemberForm

@login_required # Solo usuarios logueados pueden acceder a esta vista
def member_list(request):
    members = FamilyMember.objects.all()
    context = {'members': members, 'title': 'Lista de Miembros de la Familia'}
    return render(request, 'family_members/member_list.html', context)

@login_required
def member_create(request):
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Miembro añadido exitosamente.')
            return redirect('member_list')
    else:
        form = FamilyMemberForm()
    context = {'form': form, 'title': 'Añadir Nuevo Miembro'}
    return render(request, 'family_members/member_form.html', context)

@login_required
def member_detail(request, pk):
    member = get_object_or_404(FamilyMember, pk=pk)
    context = {'member': member, 'title': f'Detalles de {member.first_name} {member.last_name}'}
    return render(request, 'family_members/member_detail.html', context)

@login_required
def member_update(request, pk):
    member = get_object_or_404(FamilyMember, pk=pk)
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Miembro actualizado exitosamente.')
            return redirect('member_detail', pk=member.pk)
    else:
        form = FamilyMemberForm(instance=member)
    context = {'form': form, 'title': f'Actualizar {member.first_name} {member.last_name}'}
    return render(request, 'family_members/member_form.html', context)

@login_required
def member_delete(request, pk):
    member = get_object_or_404(FamilyMember, pk=pk)
    if request.method == 'POST':
        member.delete()
        messages.info(request, 'Miembro eliminado exitosamente.')
        return redirect('member_list')
    context = {'member': member, 'title': f'Eliminar {member.first_name} {member.last_name}'}
    return render(request, 'family_members/member_confirm_delete.html', context)
