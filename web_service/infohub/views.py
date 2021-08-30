import json

from django.http import JsonResponse
from django.shortcuts import render
from infohub.stock import get_zh_volume_300

def homepage(request):
    data_zh_stock = get_zh_volume_300()
    data_list_header = list(data_zh_stock.columns)
    header_column = []
    for header in data_list_header:
        header_column.append({"data":header})
    data_list_stock = data_zh_stock.values.tolist()
    return render(request, 'AdminLTE/pages/tables/data.html', locals())


def zh_volume_300_api(request):
    json_txt = get_zh_volume_300().to_json(orient="records", force_ascii=False)
    json_list = json.loads(json_txt)
    json_list = {"data": json_list}
    return JsonResponse(json_list, safe=False,json_dumps_params={'ensure_ascii':False})

# Create your views here.
