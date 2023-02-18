from django.shortcuts import render
import cyrtranslit
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Word
from django.http import HttpResponse
import pandas as pd
# Create your views here.


def test(request):
    text = "собака"
    over = cyrtranslit.to_latin(text, "ru")
    print(over)
    return render(request, 'test.html')

@csrf_exempt
def get_date(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        text = (body['message'])
        over = cyrtranslit.to_latin(text, "ru")
        word = Word.objects.create(word=text, over_word=over)
    return JsonResponse({'message':over}, safe=False)


def show_table(request):
    data = Word.objects.all().order_by('-id')[:10]
    block = []
    for i in data:
        obj = {}
        print(i.pk)
        obj['id'] = i.pk
        obj['rus'] = i.word
        obj['latin'] = i.over_word
        block.append(obj)
    return JsonResponse(block, safe=False)


def export_data(request):
    data = Word.objects.all()
    df = pd.DataFrame(list(data.values()))
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="export.xlsx"'
    writer = pd.ExcelWriter(response, engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1', index=False)
    
    writer.save()
    return response



