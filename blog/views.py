from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render_to_response
import smtplib
from email.mime.text import MIMEText
# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import Tag, Article, Author

smtp_server = 'smtp.ym.163.com'
from_addr = 'uestc_ccse@fuestck.ml'
password = '******'
to_addr = 'uestc_ccse@qq.com'

def index(request, page_num = 1):
	posts = list(Article.objects.all())
	paginator = Paginator(posts, 2)
	t = loader.get_template("index.html")
	c = Context({'posts':paginator.page(int(page_num))})
	return HttpResponse(t.render(c))

def contact(request):
    name = request.POST.get('name','guest')
    subject = request.POST['subject']
    message = request.POST['message']
    email = request.POST.get('email', 'noreply@example.com')
    msg = MIMEText(message,_subtype='plain',_charset='gb2312')
	
    msg['To'] = to_addr
	
    msg['Subject'] = u'%s'%subject
    
    msg['From'] = u'%s<%s>'%(name,email)
    
    server = smtplib.SMTP(smtp_server,25)
		
    server.login(from_addr,password)
		
    server.sendmail(from_addr,to_addr,msg.as_string())
		
    server.quit()
    return render_to_response('post.html')
    