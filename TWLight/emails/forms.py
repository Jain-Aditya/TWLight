from django import forms
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

class ContactUsForm(forms.Form):
    email = forms.EmailField(disabled = True,)
    message = forms.CharField(widget = forms.Textarea, max_length = 1000,)
    next = forms.CharField(widget = forms.HiddenInput, max_length = 40,)
    
    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        # Translators: This labels a textfield where users can enter their email ID.
        self.fields['email'].label = _('Your email')
        self.fields['email'].help_text =  _('This field is automatically updated with the email from your <a href="{}">user profile</a>.'.format(reverse_lazy('users:home')))
        # Translators: This labels a textfield where users can enter their email message.
        self.fields['message'].label = _('Message')

        # @TODO: This sort of gets repeated in ContactUsView.
        # We could probably be factored out to a common place for DRYness.
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'
        self.helper.layout = Layout(
            'email',
            'message',
            'next',
            # Translators: This labels a button which users click to submit their email message.
            Submit('submit', _('Submit'), css_class='center-block'),
        )