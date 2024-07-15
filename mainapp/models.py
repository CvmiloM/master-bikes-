from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('resuelto', 'Resuelto'),
        ('rechazado', 'Rechazado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado_actual = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.cliente.nombre}"

class HistorialReparacion(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    descripcion = models.TextField()
    repuestos_utilizados = models.TextField()
    tecnico = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reparación {self.id} - {self.solicitud.cliente.nombre}"



from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsuarioAdminManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class UsuarioAdmin(AbstractUser):
    # Añade campos personalizados aquí si es necesario
    pass

    # Añadir los related_name únicos
    groups = models.ManyToManyField(
        Group,
        related_name='usuarioadmin_groups',  # related_name único
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                    'granted to each of their groups.'),
        related_query_name='usuarioadmin'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarioadmin_user_permissions',  # related_name único
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuarioadmin'
    )

class RegistroEmail(models.Model):
    fecha_envio = models.DateTimeField(auto_now_add=True)
    asunto = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return f"Correo a {self.cliente.email} - {self.asunto} - {self.fecha_envio}"
    
