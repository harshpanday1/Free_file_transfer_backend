from django import forms
from .models import UserOTP
from .models import UserDetail
class UserOTPForm(forms.ModelForm): 
    class Meta:
        model = UserOTP
        # fields = '__all__'
        fields = ('otp'),

class UserDetailForm(forms.ModelForm): 
    class Meta:
        model = UserDetail
        # fields = '__all__'
        fields = '__all__'