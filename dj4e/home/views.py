from dajngo.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
	logging.error("Hello world DJ4E in the log...")
	print("Hello world DJ4E in a print statment...")
	response="""<html>
	<head><meta name=wa4e" content="c9e1074f5b3f9fc8ea15d152add07294"></head>
	<body><p>Hello world DJ4E in HTML</p>
	</body></html>"""
	return HttpResponse(response)
