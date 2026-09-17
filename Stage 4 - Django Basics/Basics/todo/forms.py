from django import forms
from .models import Todo

status_choices = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]
priority_choices = [
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH', 'High'),
]

# create a form for the todo model 
class TodoForm(forms.ModelForm):

    # create a choice field for status and priority
    status = forms.ChoiceField(choices=status_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(choices=priority_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    # meta class to define the model and fields to be included in the form
    class Meta:
        model = Todo
        fields = ['title','description','priority','status']
        labels = {
            'title': 'Title',
            'description': 'Description',
        }
        error_messages = {
            'title': {
                'max_length': 'This title is too long.',
            },
            'description': {
                'max_length': 'This description is too long.',
            },
        }

        # widget to define the type of input field to be used
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter title' }),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter description' }),
        }
        # fields that are required
        required_fields = ['title', 'description', 'priority', 'status'] 
        help_texts = {
            'title': 'Enter the title for the todo.',
            'description': 'Enter the description for the todo.',
            'priority': 'Select the priority of the todo.',
            'status': 'Select the status of the todo.',
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long")
        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long")
        return description

