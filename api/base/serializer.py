from rest_framework.serializers import ModelSerializer
from .models import Advocate,Company

class companyserializer(ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'
class advocatedserializer(ModelSerializer):
    company=companyserializer() #it shows company name
    class Meta: #why create meta class ?
        model=Advocate
        fields=['username','bio','company']