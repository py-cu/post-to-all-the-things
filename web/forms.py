from wtforms import Form, TextAreaField, DateTimeField, BooleanField, validators, FieldList


class NewMessageForm(Form):
    date = DateTimeField('Date', format='%m-%d-%Y %H:%M:%S')
    message = TextAreaField('Message', [validators.Length(min=1, max=144)])
    send_twitter = BooleanField('Twitter')
    send_facebook = BooleanField('Facebook')
    send_meetup = BooleanField('Meetup')
