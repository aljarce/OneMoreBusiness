import os

from django.shortcuts import render, redirect
from django.conf import settings
import requests
import logging
from .forms import QuestionnaireForm
 # ...existing code...

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'AQUI_TU_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'AQUI_TU_CHAT_ID')
WHATSAPP_LINK = 'https://wa.me/34625144654?text=Quiero%20agendar%20llamada%20para%20entrar%20en%20OneMoreBusiness'  # Cambia por tu enlace

def send_telegram_message(data):
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
	url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
	payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
	print(f"token: {TELEGRAM_BOT_TOKEN}, chat_id: {TELEGRAM_CHAT_ID}")
	try:
		response = requests.post(url, data=payload, timeout=5)
	except Exception as e:
		print(f"Error enviando mensaje a Telegram: {e}")

def questionnaire_view(request):
	if request.method == 'POST':
		form = QuestionnaireForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			send_telegram_message(data)
			return redirect(WHATSAPP_LINK)
	else:
		form = QuestionnaireForm()
	return render(request, 'landing/questionnaire.html', {'form': form})
