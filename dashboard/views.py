from django.http.response import HttpResponse
from django.shortcuts import render
from . forms import *
import requests
from googletrans import LANGUAGES
from django.views import View
from translate import Translator
from . models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import generic
import wikipedia

# Create your views here.
@login_required
def home(request):
    return render(request,"dashboard/home.html")

@login_required
def dictionary(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url ="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json()
        try:
            phonetics = answer[0]['phonetics'][0]['text'],
            audio = answer[0]['phonetics'][0]['audio'],
            definition = answer[0]['meanings'][0]['definitions'][0]['definition'],
            example = answer[0]['meanings'][0]['definitions'][0]['example'],
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms'],
            context = {
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio': audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms
            }
        except:
            context = {
                'form':form,
                'input':''
            }
        return render(request,"dashboard/dictionary.html",context)
    else:
        form =DashboardForm()
        context = {'form':form}
    return render(request,"dashboard/dictionary.html",context)

@login_required
def conversions(request):
    if request.method == "POST":
        form = ConversionForm(request.POST)
        if request.POST['measurement'] == 'length':
            measurement_form = ConversionLengthForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input  =request.POST['input']
                answer = ''
                if input and int(input) >=0:
                    if first =='yard' and second == 'foot':
                        answer = f'{input} yard = {int(input)*3} foot'
                    if first =='foot' and second == 'yard':
                        answer = f'{input} foot = {int(input)/3} yard'
                    if first =='foot' and second == 'centimeter':
                        answer = f'{input} foot = {int(input)*30.48} centimeter'
                    if first =='centimeter' and second == 'foot':
                        answer = f'{input} centimeter = {int(input)/30.48} foot'
                    if first =='foot' and second == 'meter':
                        answer = f'{input} foot = {int(input)*0.305} meter'
                    if first =='meter' and second == 'foot':
                        answer = f'{input} meter = {int(input)/0.305} foot'
                    if first =='yard' and second == 'centimeter':
                        answer = f'{input} yard = {int(input)*91.44} centimeter'
                    if first =='centimeter' and second == 'yard':
                        answer = f'{input} centimeter = {int(input)/91.44} yard'
                    if first =='yard' and second == 'meter':
                        answer = f'{input} yard = {int(input)*0.914} meter'
                    if first =='meter' and second == 'yard':
                        answer = f'{input} meter = {int(input)/0.914} yard'
                    if first =='meter' and second == 'centimeter':
                        answer = f'{input} meter = {int(input)*100} centimeter'
                    if first =='centimeter' and second == 'meter':
                        answer = f'{input} centimeter = {int(input)/100} meter'
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }
        if request.POST['measurement'] == 'mass':
            measurement_form = ConversionMassForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input  =request.POST['input']
                answer = ''
                if input and int(input) >=0:
                    if first =='pound' and second == 'kilogram':
                        answer = f'{input} pound = {int(input)*0.454} kilogram'
                    if first =='kilogram' and second == 'pound':
                        answer = f'{input} kilogram = {int(input)/0.454} pound'
                    if first =='pound' and second == 'gram':
                        answer = f'{input} pound = {int(input)*453.592} gram'
                    if first =='gram' and second == 'pound':
                        answer = f'{input} gram = {int(input)/453.592} pound'
                    if first =='kilogram' and second == 'gram':
                        answer = f'{input} kilogram = {int(input)*1000} gram'
                    if first =='gram' and second == 'kilogram':
                        answer = f'{input} gram = {int(input)/1000} kilogram'
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }
        if request.POST['measurement'] == 'time':
            measurement_form = ConversionTimeForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input  =request.POST['input']
                answer = ''
                if input and int(input) >=0:
                    if first =='minutes' and second == 'seconds':
                        answer = f'{input} minutes = {int(input)*60} seconds'
                    if first =='seconds' and second == 'minutes':
                        answer = f'{input} seconds = {int(input)/60} minutes'
                    if first =='seconds' and second == 'hours':
                        answer = f'{input} seconds = {int(input)/3600} hours'
                    if first =='hours' and second == 'seconds':
                        answer = f'{input} hours = {int(input)*3600} seconds'
                    if first =='minutes' and second == 'hours':
                        answer = f'{input} minutes = {int(input)/60} hours'
                    if first =='hours' and second == 'minutes':
                        answer = f'{input} hours = {int(input)*60} minutes'
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }

    else:
        form = ConversionForm()
        context ={
            'form':form,
            'input':False
        }
    return render(request,"dashboard/conversion.html",context)

@login_required
def translate_app(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        return HttpResponse(translation)
    return render(request, 'dashboard/translate.html')

@login_required
def wiki(request):
    if request.method == "POST":
        text = request.POST['text']
        form = DashboardForm(request.POST)
        search = wikipedia.page(text)
        context = {
            'form':form,
            'title':search.title,
            'link' : search.url,
            'details' : search.summary
        }
        return render(request,"dashboard/wiki.html",context)
    else:
        form = DashboardForm()
        context = {
        'form':form
        }
    return render(request,"dashboard/wiki.html",context)

def register(request):
    if request.method == "POST":
        form =UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username} Succesfully!!")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {
        'form':form
    }
    return render(request,"dashboard/register.html",context)

