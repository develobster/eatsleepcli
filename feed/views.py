#import smtplib
from email.header import Header
from email.mime.text import MIMEText
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView
from feed.forms import FeedbackForm
from django.conf import settings
from django.core.mail import send_mail

class FeedbackFormView(FormView):
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = '/form-success'


    def form_invalid(self, form):
        response = super(FeedbackFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(FeedbackFormView, self).form_valid(form)
        if self.request.is_ajax():
            mail_sender = form.cleaned_data.get('email')
            #mail_receiver = ''
            #username = ''
            #password = ''
            #server = smtplib.SMTP('smtp.mail.ru:465')
            subject = 'Test email by ' + mail_sender
            body = 'Входящее сообщение от пользователя ' +\
                   form.cleaned_data.get('name') + ', тел: ' + form.cleaned_data.get('tel') + \
                   ': ' + form.cleaned_data.get('text')
            #msg = MIMEText(body, 'plain', 'utf-8')
            
            #msg['Subject'] = Header(subject, 'utf-8')
            send_mail(subject, body, settings.EMAIL_HOST_USER, ['temavandal@gmail.com'])
            #server.starttls()
            #server.ehlo()
            #server.login(username, password)
            #server.sendmail(mail_sender, mail_receiver, msg.as_string())
            #server.quit()

            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response
