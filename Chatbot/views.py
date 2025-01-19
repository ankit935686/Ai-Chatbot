from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Create your views here.

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        # Call Gemini API with correct endpoint
        api_key = "AIzaSyBuXUVX8PvzlBXMDRctrMPudQSd6nNrDbU"  # Replace with your actual API key
        gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        
        headers = {
            "Content-Type": "application/json",
        }
        
        payload = {
            "contents": [{
                "parts": [{
                    "text": user_message
                }]
            }]
        }

        try:
            response = requests.post(
                f"{gemini_api_url}?key={api_key}",
                headers=headers,
                json=payload
            )
            response_data = response.json()
            bot_response = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'Sorry, I couldn\'t understand that.')
        except Exception as e:
            bot_response = f"Error: {str(e)}"

        return JsonResponse({"response": bot_response})
    return JsonResponse({"error": "Invalid request method"}, status=400)

def home(request):
    return render(request, 'botpage.html')
