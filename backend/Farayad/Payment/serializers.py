from rest_framework import serializers
from .models import Payment

def change_date_format(object):
    if object is None:
        return None  
        
    date = object.date_purchased
    if date.minute/10 > 1:
        date = f"{date.date().isoformat()} {date.hour}:{date.minute}"
    else:
        date = f"{date.date().isoformat()} {date.hour}:0{date.minute}"

    return date


class PaymentSerializer(serializers.ModelSerializer):
    _date_purchased = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = ('purchaser',
                  'course',
                  '_date_purchased')

    def get__date_purchased(self,object):
        return change_date_format(object)
