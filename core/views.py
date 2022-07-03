from django.contrib.auth import login, authenticate,logout
from django.shortcuts import redirect, render, HttpResponse
from .models import Blog, BlogComment, Contact
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(request):
    blogs = Blog.objects.all().order_by('-release_date')[0:20]
    blogDic = {"allblogs": blogs}
    return render(request, "index.html", blogDic)


def blogPost(request, slug):
    filteringTheBlog = Blog.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(
        post=filteringTheBlog).order_by('-Date')
    filterBlogDic = {"singleBlog": filteringTheBlog, "comments": comments}
    return render(request, "blogPost.html", filterBlogDic)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postid = request.POST.get('postSno')
        post = Blog.objects.get(id=postid)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/blogPost/{post.slug}")


def contact(request):
    if request.method == 'POST':
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        contact = Contact(fullname=fullname, email=email,
                          phone=phone, message=message)
        contact.save()
        messages.success(request, "Thanks for contacting us " + fullname)

    return render(request, "contact.html")


def privacyPolicy(request):
    return render(request, "privacy-policy.html")


def loginUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        userLogin = authenticate(username=username, password=password)
        if userLogin is not None:
            login(request, userLogin)
            messages.success(request, "Welcome " + username)
            return redirect('/')
        else:
            messages.warning(request, "Please check your username or password")
            return redirect('login')
    return render(request, "login.html")


def signupUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).first():
            messages.warning(
                request, "This username already exists")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            messages.success(
                request, " Your account has been created successfully ")
            return redirect('login')

    return render(request, "signup.html")


def logoutUser(request):
    logout(request)
    messages.success(request,"You have been loggedOut")
    return redirect("login")
    return HttpResponse("You have been loggedOut")


def allblogs(request):

    allblogs = Blog.objects.all().order_by('-release_date')
    prop = {"blogs":allblogs}
    return render(request,"allblogs.html",prop)



def category(request,cat):
    blogcat = Blog.objects.filter(category=cat)
    catDic = {"catblog":blogcat}
    return render(request,"category.html",catDic)




def search(request):
    query = request.GET['search']
    search_filter = Blog.objects.filter(title__icontains=query)
    search_dic = {"search": search_filter, "query": query }
    return render(request, "search.html", search_dic)