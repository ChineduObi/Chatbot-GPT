from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = "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"
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    print(response)
""" answer = response.choice[0].text.strip()
    return answer """


# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')