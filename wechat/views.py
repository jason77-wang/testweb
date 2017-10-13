from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt
import json
from lxml import etree
from django.utils.encoding import smart_str
from django.http import HttpResponse

WEIXIN_TOKEN = 'xiaochuchinese'
@csrf_exempt
# Create your views here.
def main(request):
    print request
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        print signature
        timestamp = request.GET.get("timestamp", None)
        print timestamp
        nonce = request.GET.get("nonce", None)
        print nonce
        echostr = request.GET.get("echostr", None)
        print echostr
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")
        
    elif request.method == "POST":
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        response_xml = request_xml
        c1 = request_xml[0]
        c2 = request_xml[1]
        tmp = c1.text

        response_xml[0].text = c2.text
        response_xml[1].text = tmp
        response_xml[4].text = "welcome!"
        print etree.tostring(response_xml)
        return HttpResponse(etree.tostring(response_xml))


