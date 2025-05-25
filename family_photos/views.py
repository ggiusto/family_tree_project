# family_photos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FamilyPhoto
from .forms import FamilyPhotoForm

@login_required
def photo_list(request):
    photos = FamilyPhoto.objects.all()
    context = {'photos': photos, 'title': 'Fotos Familiares'}
    return render(request, 'family_photos/photo_list.html', context)

@login_required
def photo_upload(request):
    if request.method == 'POST':
        form = FamilyPhotoForm(request.POST, request.FILES) # Importante: request.FILES para la imagen
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user # Asigna el usuario logueado como quien subió la foto
            photo.save()
            messages.success(request, 'Foto subida exitosamente.')
            return redirect('photo_list')
    else:
        form = FamilyPhotoForm()
    context = {'form': form, 'title': 'Subir Nueva Foto'}
    return render(request, 'family_photos/photo_upload_form.html', context)

@login_required
def photo_detail(request, pk):
    photo = get_object_or_404(FamilyPhoto, pk=pk)
    context = {'photo': photo, 'title': f'Detalles de Foto: {photo.title if photo.title else photo.pk}'}
    return render(request, 'family_photos/photo_detail.html', context)

@login_required
def photo_update(request, pk):
    photo = get_object_or_404(FamilyPhoto, pk=pk)
    # Solo el autor o un superusuario pueden editar
    if request.user != photo.uploaded_by and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para editar esta foto.')
        return redirect('photo_detail', pk=photo.pk)

    if request.method == 'POST':
        form = FamilyPhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto actualizada exitosamente.')
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = FamilyPhotoForm(instance=photo)
    context = {'form': form, 'title': f'Editar Foto: {photo.title if photo.title else photo.pk}'}
    return render(request, 'family_photos/photo_upload_form.html', context) # Reutilizamos el formulario de subida

@login_required
def photo_delete(request, pk):
    photo = get_object_or_404(FamilyPhoto, pk=pk)
    # Solo el autor o un superusuario pueden eliminar
    if request.user != photo.uploaded_by and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para eliminar esta foto.')
        return redirect('photo_detail', pk=photo.pk)

    if request.method == 'POST':
        photo.delete()
        messages.info(request, 'Foto eliminada exitosamente.')
        return redirect('photo_list')
    context = {'photo': photo, 'title': f'Eliminar Foto: {photo.title if photo.title else photo.pk}'}
    return render(request, 'family_photos/photo_confirm_delete.html', context)
