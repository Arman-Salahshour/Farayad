from rest_framework import serializers
from .models import Payment
from User.serializers import UserSerializer

def change_date_format(date):

    if date.minute/10 > 1:
        date = f"{date.date().isoformat()} {date.hour}:{date.minute}"
    else:
        date = f"{date.date().isoformat()} {date.hour}:0{date.minute}"

    return date


class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(source = 'purchaser')
    _date_purchased = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = ('user',
                  'course',
                  '_date_purchased')

    def get__date_purchased(self,object):
        if object is None:
            return None  
        return change_date_format(object.date_purchased)
