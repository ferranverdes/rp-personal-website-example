from django import forms

class CommentForm(forms.Form):
	author = forms.CharField(
		max_length=70,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Your name'
			}
		)
	)

	body = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class': 'form-control',
				'placeholder': 'Leave a comment'
			}
		)
	)

# The author field has the forms.TextInput widget. This tells Django to load this
# field as an HTML text input element in the templates. The body field uses a forms.TextArea
# widget instead, so that the field is rendered as an HTML text area element.
#
# These widgets also take an argument attrs, which is a dictionary and allows us to
# specify some CSS classes, which will help with formatting the template for this view
# later. It also allows us to add some placeholder text.
