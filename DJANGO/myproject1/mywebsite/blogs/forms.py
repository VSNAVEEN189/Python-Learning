from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment    #Actually connects the form to the model, it is a way to tell django that this form is associated with the comment model, so that we can use the fields of the comment model in our form.
        # fields = ["user_name", "user_email", "comment_text"]  #To specify which fields we want to use in our form, we can use all to get all the fields of the model or we can specify the fields we want to use in our form. In this case, we are using user_name, user_email and comment_text fields of the comment model in our form.
        exclude = ["post"]  #To specify which fields we want to exclude from our form, we can use all to get all the fields of the model or we can specify the fields we want to exclude from our form. In this case, we are excluding post field of the comment model from our form because we will set it in the view when we save the form.
        labels = {"user_name": "Your Name", "user_email": "Your Email", "comment_text": "Your Comment"}  #To specify the labels for the fields in our form, we can use a dictionary to specify the labels for each field. In this case, we are specifying the labels for user_name, user_email and comment_text fields of the comment model in our form.
        