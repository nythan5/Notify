from rest_framework import views, response, status
from webhooks.models import Webhook
import json
from webhooks.messages import outflow_message
from services.callmebot import CallMeBot
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


class WebhookOrderView(views.APIView):

    def post(self, request):
        data = request.data

        Webhook.objects.create(
            event_type=data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False)
        )

        # Capturando os valores da request
        product_name = data.get('product')
        quantity = data.get('quantity')
        product_cost_price = data.get('product_cost_price')
        product_selling_price = data.get('product_selling_price')

        # Calculando os totais
        total_value = product_selling_price * quantity
        profit_value = total_value - (product_cost_price * quantity)

        # Montando a message com o format utilizando posicionamento para exibir as variaveis
        message = outflow_message.format(
            product_name,
            product_cost_price,
            product_selling_price,
            quantity,
            total_value,
            profit_value
        )

        # Instanciando e enviando a message via WhatsApp
        callmebot = CallMeBot()
        callmebot.send_message(message=message)

        # Fazendo o SEND_EMAIL

        data['total_value'] = total_value
        data['profit_value'] = profit_value

        send_mail(
            subject='Novo Registro de Saida - SGE',
            message='',
            from_email=f'SGE <{settings.EMAIL_HOST_USER}>',
            recipient_list=[settings.EMAIL_ADMIN_RECEIVER],

            # usando a função render to string para renderizar as varaveis dentro do template
            html_message=render_to_string('outflow.html', data),
            fail_silently=False,
        )

        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )
