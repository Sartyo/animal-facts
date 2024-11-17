from django.shortcuts import render
import requests

# Create your views here.

def dog_facts(request):
    url = 'https://dogapi.dog/api/v2/facts?limit=1'
    response = requests.get(url)
    data = response.json()
    fact = data['data'][0]["attributes"]["body"]
    return render(request, 'facts/dog-facts.html', {'fact': fact,})

def cat_facts(request):
    url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1'
    response = requests.get(url)
    data = response.json()
    fact = data['text']
    return render(request, 'facts/cat-facts.html', {'fact': fact,})