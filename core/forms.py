from django import forms


class CommentForm(forms.Form):
    user = forms.CharField(required=False)
    content = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = 'Имя'
        self.fields['content'].label = 'Коментарий'
        self.fields['content'].help_text = 'Напишите свой коментарий'


class ContactForm(forms.Form):
    user = forms.CharField()
    content = forms.CharField(widget=forms.Textarea )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = 'Имя'
        self.fields['content'].label = 'Сообщение'
        self.fields['content'].help_text = 'Напишите своё сообщение'















        # self.fields['date'].label = 'Дата доставки'
        # self.fields['date'].help_text = 'Доставка производиться на следующий день после оформления заказа. Менеджер с Вами свяжится'
        # self.fields['date'].widget.attrs['class'] = 'help-text-class help-text-other'

    # content.widget.attrs.update({'style': 'width: 70vh; display: inline; margin-right: 1px;', 'class': 'date-widget'})

