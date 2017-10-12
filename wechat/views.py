from django.shortcuts import render
from django.http import HttpResponse
import hashlib

WEIXIN_TOKEN = 'write-a-value'

# Create your views here.
def main(request):
#    print request
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
    else:
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        response_xml = auto_reply_main(request_xml)
        return HttpResponse(response_xml)

