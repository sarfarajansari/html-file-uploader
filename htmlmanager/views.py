from django.shortcuts import render,redirect
from urllib.request import urlopen
from .models import Project,ProjectFile
from django.http import JsonResponse,HttpResponse

# Create your views here.

def index(request):
    projects = Project.objects.all()
    context={
        "projects":projects
    }
    return render(request,"index.html",context)

def project(request,project,filename):
    try:
        project = Project.objects.get(name=project)
        page = project.files.get(filename=filename)
        html = page.data
    except:
        fileobj = open("static/media/not_found.html",mode="r")
        html = fileobj.read()

    if ".css" in filename:
        response = HttpResponse(html,content_type='text/css')
        return response

    elif ".js" in filename:
        response= HttpResponse(html,content_type="application/javascript")
        return response

    context={
        "html":html,
        "project":project
    }
    return render(request,"project.html",context)

def submit(request):
    if request.method =="GET":
        if "n" in request.GET and int(request.GET["n"])<21 and int(request.GET["n"])>0 and "project" in request.GET :
            n=request.GET["n"]
            request.session["project"] = request.GET["project"]

            try:
                project = Project.objects.get(name=request.GET["project"])
                return render(request,"submit.html",{
                    "error":"Project Name Unavailable"
                })
            except:
                pass

            

            if "name" in request.GET:
                request.session["name"]=request.GET["name"]

            if not request.session["name"]:
                return redirect("/submit/")


            return render(request,"submit.html",{
                "n":n,
                "range":range(int(n))
                })
        else:
            return render(request,"submit.html")

    else:
        print("block1")
        P= request.POST

        if "n" in P and "project" in request.session and "name" in request.session:
            project = Project.objects.create(name=request.session["project"],username=request.session["name"])
            for i in range(int(P["n"])):
                html = "html" + str(i)
                name = "filename" + str(i)
                if html in P and name in P:
                    htmlfile= P[html]
                    filename = P[name]
                    projectfile = ProjectFile.objects.create(data=htmlfile,project=project,filename=filename)


            return redirect(project.site)

        return redirect("/admin/")


