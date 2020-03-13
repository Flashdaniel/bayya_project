from django import forms
from .models import MyUser, UserProfile
from django.contrib import admin
from django.core import validators
from django.contrib.auth.models import Group
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
                            'class':'form-control',
                            'placeholder':'EMAIL'
                            }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                            'class':'form-control',
                            'placeholder': 'PASSWORD'
                            }))


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    email = forms.CharField(widget=forms.EmailInput(attrs={
                            'class':'form-control',
                            'placeholder':'EMAIL'
                            }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'FIRST NAME'
                                }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'LAST NAME'
                                }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                                'class':'form-control',
                                'placeholder':'PASSWORD'
                                }))

    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={
                                'class':'form-control',
                                'placeholder':'CONFIRM PASSWORD'
                                }))

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'country')
        widgets = {'country':CountrySelectWidget(attrs={
                    'class':'form-control',
                })}

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name',  'country', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('bank_name', 'bank_acct_no', 'bitcoin_address')
        widgets = {'bank_name':forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'BANK NAME'
                    }),
                    'bank_acct_no':forms.NumberInput(attrs={
                        'class':'form-control',
                        'placeholder':'BANK ACCOUNT NO'
                    }),
                    'bitcoin_address':forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'BITCOIN ADDRESS'
                    })
                }

class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('my_user', 'bank_name', 'bank_acct_no', 'bitcoin_address')
    list_filter = ('my_user', 'bank_name', 'bank_acct_no')

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name',  'country')
    list_filter = ('is_admin', 'first_name', 'last_name', 'country')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ( 'first_name', 'last_name', 'country')}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'country', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'country')
    ordering = ('email', 'first_name', 'last_name', 'country')
    filter_horizontal = ()
#Changes the django administrations header
admin.site.site_header = 'BAYYA ADMIN PANEL'
#Now register the new UserProfile
admin.site.register(UserProfile, UserProfileAdmin)
# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
