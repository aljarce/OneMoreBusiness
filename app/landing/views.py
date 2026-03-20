import os

from django.shortcuts import render, redirect
from django.conf import settings
import requests
import logging
from .forms import QuestionnaireForm
 # ...existing code...

WHATSAPP_LINK = 'https://wa.me/34625144654?text=Quiero%20agendar%20llamada%20para%20entrar%20en%20OneMoreBusiness'  # Cambia por tu enlace
logger = logging.getLogger(__name__)

def send_telegram_message(data):
	telegram_bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', '')
	telegram_chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', '')

	if not telegram_bot_token or not telegram_chat_id:
		logger.error('Faltan TELEGRAM_BOT_TOKEN o TELEGRAM_CHAT_ID en variables de entorno.')
		return False

	text = (
		"Nuevo cuestionario recibido:\n"
		f"Nombre: {data.get('nombre', '')}\n"
		f"Email: {data.get('email', '')}\n"
		f"Situación actual: {data.get('situacion', '')}\n"
		f"Objetivo: {data.get('objetivo', '')}\n"
		f"Inversión: {data.get('inversion', '')}\n"
		f"Meta con acompañamiento: {data.get('conseguir', '')}\n"
		f"Disponibilidad: {data.get('disponibilidad', '')}\n"
		f"Teléfono: {data.get('tlf', '')}"
	)
	url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
	payload = {"chat_id": telegram_chat_id, "text": text}
	try:
		response = requests.post(url, data=payload, timeout=10)
		telegram_result = response.json()
		if response.status_code >= 400:
			logger.error(
				'Telegram HTTP error. status=%s body=%s',
				response.status_code,
				telegram_result,
			)
			return False
		if not telegram_result.get('ok'):
			logger.error('Telegram devolvio error: %s', telegram_result)
			return False
		logger.info('Telegram enviado correctamente para email=%s', data.get('email', ''))
		return True
	except Exception as e:
		logger.exception("Error enviando mensaje a Telegram: %s", e)
		return False

def questionnaire_view(request):
	if request.method == 'POST':
		form = QuestionnaireForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			logger.info('Formulario valido recibido para email=%s', data.get('email', ''))
			send_telegram_message(data)
			return redirect(WHATSAPP_LINK)
		logger.error('Formulario invalido. errores=%s', form.errors.as_json())
	else:
		form = QuestionnaireForm()
	return render(request, 'landing/questionnaire.html', {'form': form})
