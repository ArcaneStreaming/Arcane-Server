# -*- coding: utf-8 -*-

from django import forms


class UploadForm(forms.Form):
    uploadfiles = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Add Tracks')
