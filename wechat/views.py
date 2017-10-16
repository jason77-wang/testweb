# coding: UTF-8

from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt
import json
from lxml import etree
from django.utils.encoding import smart_str
from django.http import HttpResponse
import processfile

WEIXIN_TOKEN = 'xiaochuchinese'
@csrf_exempt
# Create your views here.
def main(request):

    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)

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
        tpl = u'''<xml><ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1507874304</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
<MsgId>6476270822591158287</MsgId>
</xml>'''

        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        c1 = request_xml[0]
        c2 = request_xml[1]
        txt = request_xml[4]
        if txt == "听写":
            txt = processfile.testfile()
            smsg = tpl % (c2.text, c1.text, txt.text)
        else:
	    smsg = tpl % (c2.text, c1.text, u"您发的内容为: "+txt.text)
#	smsg = tpl % (c2.text, c1.text, u"字符编码声明")
#        print smsg
        return HttpResponse(smsg)


