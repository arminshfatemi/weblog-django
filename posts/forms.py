from django import forms


class PostForm(forms.Form):

    title = forms.CharField(max_length=100)
    decription = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea, max_length=400)
    hidden = forms.BooleanField(required=False,initial=False, widget=forms.CheckboxInput())

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=400)

