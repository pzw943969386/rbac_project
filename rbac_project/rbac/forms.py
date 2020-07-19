from django import forms
from rbac import models
from django.utils.safestring import mark_safe


# 角色的Form
class RoleForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = ['name']
        
        widgets = {
            'name': forms.widgets.Input(attrs={"class": 'form-control'})
        }


ICON_LIST = [[i[0], mark_safe(i[1])] for i in [
    ['fa-address-book', '<i aria-hidden="true" class="fa fa-address-book"></i>'],
    ['fa-address-book-o', '<i aria-hidden="true" class="fa fa-address-book-o"></i>'],
    ['fa-address-card', '<i aria-hidden="true" class="fa fa-address-card"></i>'],
    ['fa-address-card-o', '<i aria-hidden="true" class="fa fa-address-card-o"></i>'],
    ['fa-adjust', '<i aria-hidden="true" class="fa fa-adjust"></i>'],
    ['fa-american-sign-language-interpreting',
     '<i aria-hidden="true" class="fa fa-american-sign-language-interpreting"></i>'],
    ['fa-anchor', '<i aria-hidden="true" class="fa fa-anchor"></i>'],
    ['fa-archive', '<i aria-hidden="true" class="fa fa-archive"></i>'],
    ['fa-area-chart', '<i aria-hidden="true" class="fa fa-area-chart"></i>'],
    ['fa-arrows', '<i aria-hidden="true" class="fa fa-arrows"></i>']
]]


# 菜单的Form
class MenuForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ['title', 'weight', 'icon', ]
        
        widgets = {
            'title': forms.widgets.Input(attrs={"class": 'form-control'}),
            'weight': forms.widgets.Input(attrs={"class": 'form-control'}),
            'icon': forms.widgets.RadioSelect(choices=ICON_LIST),
        }

class PermissionForm(forms.ModelForm):
    class Meta:
        model = models.Permission
        # fields = '__all__'
        fields = ['title', 'url', 'name', 'parent', 'menu']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})