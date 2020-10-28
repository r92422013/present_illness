from django.shortcuts import render
from django.http import HttpResponse
from patientapp.models import patient

# Create your views here.
def question(request):
    if request.method == 'POST':
        cNAME = request.POST['NAME']
        cID = request.POST['ID']
        cGENDER = request.POST['GENDER']
        cAGE = request.POST['AGE']
        cWHERE = request.POST['WHERE']
        cPAINSITE = request.POST['PAINSITE']
        cWHEN = request.POST['WHEN']
        cHOW = request.POST['HOW']
        cPROVOCATION = request.POST['PROVOCATION']
        cPAINLEVEL = request.POST['PAINLEVEL']
        SYNONYM = ''
        if request.POST['GENDER'] == 'male':
            SYNONYM = 'he' 
        else:
            SYNONYM = 'she'
        POSSESIVE = ''
        if request.POST['GENDER'] == 'male':
            POSSESIVE = 'his'
        else:
            POSSESIVE = 'her'
        cPI = 'This is a ' + cAGE + '-year-old ' + cGENDER + ' patient who states that starting ' + cWHEN + ' ' + SYNONYM + ' has had very significant discomfort in ' + POSSESIVE + ' ' + cWHERE + ' '+ cPAINSITE + '.' + 'This discomfort began ' + cHOW + ' and was first noted as a ' + cPAINLEVEL + ' pain. The patient complains ' + cPROVOCATION + '.'
        unit = patient.objects.create(cNAME=cNAME, cID=cID, cGENDER=cGENDER,cAGE=cAGE,cWHERE=cWHERE,cPAINSITE=cPAINSITE,cWHEN=cWHEN,cHOW=cHOW,cPAINLEVEL=cPAINLEVEL,cPI=cPI)
        unit.save()
        patients = patient.objects.all().order_by('-id')
        return HttpResponse('資料輸入完成')
    else:
        return render(request,"question.html",locals())
