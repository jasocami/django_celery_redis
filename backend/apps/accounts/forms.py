from django.contrib.auth.forms import SetUnusablePasswordMixin, BaseUserCreationForm, \
    UserChangeForm as BaseUserChangeForm
from django.core.exceptions import ValidationError
from django.forms import EmailField

from apps.accounts.models import User


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = User
        fields = "__all__"
        field_classes = {"email": EmailField}


class UserCreationForm(BaseUserCreationForm):
    def clean_username(self):
        """Reject usernames that differ only in case."""
        email = self.cleaned_data.get("email")
        if (
            email
            and self._meta.model.objects.filter(email__exact=email).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "email": self.instance.unique_error_message(
                            self._meta.model, ["email"]
                        )
                    }
                )
            )
        else:
            return email



class AdminUserCreationForm(SetUnusablePasswordMixin, UserCreationForm):
    pass