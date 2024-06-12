from django.forms import ModelForm
from .models import *

class CreatePricing(ModelForm):
    class Meta:
        model = solicitud_cotizacion
        fields = ['producto', 'cantidad', 'unidad_medida', 'contacto', 'direccion_entrega', 'tipo_cotizacion_id', 'tipo_entrega_id']