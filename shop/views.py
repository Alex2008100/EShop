#Libraries
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.core.serializers.json import DjangoJSONEncoder
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.contrib import messages
from .models import Product
from .forms import UserRegisterForm, UserLoginForm
import csv, json

#Main views
def index(request):
    return render(request, 'index.html', {})

@csrf_exempt
def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products':products})

def shop_sorter(request):
    if request.post = "POST"
        products = Product.objects.all()
        data = []
        for product in products:
            line = product.title + ';' + product.brand + ';' + product.description + ';' + product.tag + ';' + str(product.price_buy) + ';' + str(product.price_sell) + ';' + str(product.price_sell_no_discount) + ';' + product.sku
            data.append(line)
            print(data)
            return JsonResponse(data)
        else:
            return JsonResponse(None)

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product':product})

def register(request):

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                password = form.cleaned_data.get('password'))
            user.save()
            login(request, user)
        return redirect(index)
    else:
        return render(request, 'register.html', {'form':form})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = authenticate(request,
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password'))
            if user and user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'form':form})
        else:
            return render(request, 'login.html', {'form':form})

    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form':form})

#Test views
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'test.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'test.html')

def import_csv(request):
    lines = []

    try:
        with open('media/icsv.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            for row in spamreader:
                lines.append(row)
                parameters = []
                parameters = str(row)[2:-3].split(',')
                #print(str(row)[2:-3])
                print(parameters[0])
                products = Product.objects.create(
                    title = parameters[0],
                    brand = parameters[1],
                    description = parameters[2],
                    tag = parameters[3],
                    price_buy = parameters[4],
                    price_sell = parameters[5],
                    price_sell_no_discount = parameters[6],
                    sku = parameters[7])
        csvfile.close()

    except Exception as e:
        print(e)

    return HttpResponse(lines)

def export_csv(request):
    products = Product.objects.all()
    file = []
    with open('media/ecsv.csv', 'w') as csvfile:
        for product in products:
            line = product.title + ';' + product.brand + ';' + product.description + ';' + product.tag + ';' + str(product.price_buy) + ';' + str(product.price_sell) + ';' + str(product.price_sell_no_discount) + ';' + product.sku + '\n'
            file.append(line)
        csvfile.write(''.join(file))
    csvfile.close()
    return HttpResponse(file)

def import_json(request):
    try:
        jsfile = open('media/ijson.json', 'r')
        raw_data = json.load(jsfile)
        for product in raw_data:
            fields = product.get('fields')
            print(fields)
            products = Product.objects.create(
                title = fields['title'],
                brand = fields['brand'],
                description = fields['description'],
                tag = fields['tag'],
                price_buy = fields['price_buy'],
                price_sell = fields['price_sell'],
                price_sell_no_discount = fields['price_sell_no_discount'],
                sku = fields['sku'])

        jsfile.close()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse('Finished successfully!')

def export_json(request):
    class encoder(DjangoJSONEncoder):
        def default(self, obj):
            dic = {}
            for field in obj._meta.local_fields:
                if field.serialize:
                    if field.rel is None:
                        dic[field.name] = self.handle_field(obj, field)
                    else:
                        dic[field.name] = self.handle_fk_field(obj, field)
            for field in obj._meta.many_to_many:
                if field.serialize:
                    dic[field.name] = self.handle_m2m_field(obj, field)
                    return dic

    data = serialize('json', Product.objects.all(), cls = encoder)
    #data = json.dumps(vars(products), sort_keys=False, indent=4)
    with open('media/ejson.json', 'w') as outfile:
        json.dump(data, outfile)
    outfile.close()
    print(data)
    return HttpResponse(data)

#Background views
def api_register_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username = request.POST.get('username'),
            email = request.POST.get('email'),
            password = request.POST.get('password'))
        user.save()
        login(request, user)
        return JsonResponse({'status':'Registered successfully!'})

def logout_view(request):
    logout(request)
    return redirect('/')

'''
def add_dinner(request):
    if request.method == 'POST':
        form = DinnerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            diner = Dinner.objects.create(
                            name = name,
                            text = text,)
['John', 30, False, None]
{
  "name": "John",
  "age": 30,
  "isAdmin": false,
  "wife": null
}
'''
