# family_members/models.py

from django.db import models

class FamilyMember(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    relationship_choices = [
        ('PADRE', 'Padre'), ('MADRE', 'Madre'), ('HIJO', 'Hijo/a'),
        ('HERMANO', 'Hermano/a'), ('ABUELO', 'Abuelo/a'), ('TIO', 'Tío/a'),
        ('PRIMO', 'Primo/a'), ('OTRO', 'Otro'),
    ]
    relationship = models.CharField(
        max_length=20, choices=relationship_choices, default='OTRO', verbose_name="Relación"
    )
    birth_date = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Número de Teléfono")
    address = models.TextField(blank=True, null=True, verbose_name="Dirección")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.relationship})"

    class Meta:
        verbose_name = "Miembro de la Familia"
        verbose_name_plural = "Miembros de la Familia"
        ordering = ['last_name', 'first_name']
