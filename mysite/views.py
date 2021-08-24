from django.http import HttpResponse
from django.shortcuts import render
from app.models import *
from app.forms import *
from django.core.mail import send_mail
from twilio.rest import Client
from mysite.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


def index(request):
    Slider=slider.objects.all()
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Slider": Slider}
    return render(request, "index.html", context)


def my_projects(request):
    Python_Projects=python_project.objects.all()
    Scratch_Projects=scratch_project.objects.all()
    Basic_Projects=basic_project.objects.all()
    Arduino_Projects=arduino_project.objects.all()
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Python_Projects": Python_Projects, "Scratch_Projects": Scratch_Projects, "Basic_Projects": Basic_Projects, "Arduino_Projects": Arduino_Projects}
    return render(request, "my_projects.html", context)


def python_projects_codes(request):
    Codes=python_code.objects.all()
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Codes": Codes}
    return render(request, "python_projects_codes.html", context)


def scratch_projects_codes(request):
    Codes=scratch_code.objects.all()
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Codes": Codes}
    return render(request, "scratch_projects_codes.html", context)


def certifications(request):
    Social=social_media_link.objects.all()
    Certifications=certification.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Certifications": Certifications}
    return render(request, "certifications.html", context)


def feedback(request):
    #new feedback form
    form=feedback_form
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    if request.method=='POST':
        form=feedback_form(request.POST)

        user_name = request.POST.get('name')
        e_mail_address = request.POST.get('e_mail')
        feedback_message = request.POST.get('feedback')

        t1 = '''
        
        '''

        user_name_1 = '''Name: ''' + user_name + '''
        
        '''
        e_mail_address_1 = '''E-mail: ''' + e_mail_address + '''
        
        '''
        feedback_message_1 = '''Message: ''' + feedback_message + '''
        
        '''
        
        final_message = t1 + user_name_1 + e_mail_address_1 + feedback_message_1

        #final_message = "Name: " + user_name + " (" + e_mail_address + ") " + "     " + "Message: " + feedback_message

        send_mail("New feedback on your website", final_message, 'website.submissions1@gmail.com', ['10026.dpsgv@dpsgs.org'], fail_silently=False)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="New feedback on your website" + ''' 
            
            '''+final_message,
            to='whatsapp:+919899002189'
        )
        

        if form.is_valid:
            form.save()
    #new feedback form end
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "form": form}
    return render(request, "feedback.html", context)


def blog(request):
    #new blog form
    form=add_blog_data
    if request.method=='POST':
        form=add_blog_data(request.POST)
        if form.is_valid:
            form.save()
    #new blog form end
    blogs=blog_data.objects.all()
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "blogs": blogs, "form": form}
    return render(request, "blog.html", context)


def python_projects(request, pk_prod):
    Codes=python_code.objects.get(id=pk_prod)
    Python_Projects=python_project.objects.get(id=pk_prod)
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Python_Projects": Python_Projects, "Codes": Codes}
    return render(request, "python_projects.html", context)


def arduino_projects(request, pk_prod):
    Arduino_Projects=arduino_project.objects.get(id=pk_prod)
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Arduino_Projects": Arduino_Projects}
    return render(request, "arduino_projects.html", context)


def scratch_projects(request, pk_prod):
    Codes=scratch_code.objects.get(id=pk_prod)
    Scratch_Projects=scratch_project.objects.get(id=pk_prod)
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social,"Codes": Codes, "Scratch_Projects": Scratch_Projects}
    return render(request, "scratch_projects.html", context)


def basic_electronics_projects(request, pk_prod):
    Basic_Projects=basic_project.objects.get(id=pk_prod)
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Basic_Projects": Basic_Projects}
    return render(request, "basic_electronics_projects.html", context)


def view_python_codes(request, pk_prod):
    Codes=python_code.objects.get(id=pk_prod)
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Codes": Codes}
    return render(request, "view_python_codes.html", context)


def view_scratch_codes(request, pk_prod):
    Codes=scratch_code.objects.get(id=pk_prod)
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Codes": Codes}
    return render(request, "view_scratch_codes.html", context)


def play_scratch_game(request, pk_prod):
    Codes=scratch_code.objects.get(id=pk_prod)
    Social=social_media_link.objects.all()
    Details=site.objects.all()
    context={"Details": Details, "Social": Social, "Codes": Codes}
    return render(request, "play_scratch_game.html", context)