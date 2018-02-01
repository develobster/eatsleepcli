from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    tel = forms.CharField(max_length=60)
    text = forms.CharField(max_length=500)
    # login = forms.CharField(max_length=120)
    # pwd = forms.CharField(max_length=120)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email == "abc@gmail.com":
            raise forms.ValidationError("Неправильный email")
        return email