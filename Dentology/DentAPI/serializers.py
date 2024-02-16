from rest_framework import serializers
from mainapp.models import Patient
import bleach


#this will automatically serialize the data into json/xml
class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient;
        #fields = '__all__'
        fields = ['id', 'first_name', 'last_name', 'history', 'dentist', 'gender', 'group'];
        #extra_kwargs = {
        #    "price":{"min_value":2},
        #    "inventory":{"min_value":0}
        #    }
        def validate_gender(self, value):
            if value != 'male' or value != "female":
                raise serializers.ValidationError("Gender should be either male or female");
            else:
                return bleach.clean(value)