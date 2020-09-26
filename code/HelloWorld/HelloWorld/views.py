from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Book,Publish,Author
from django.db.models import Avg,Max,Min,Count,Sum
from . import My_forms
 
def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    views_list = ["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
    return render(request, "runoob.html", {"views_list": views_list})


def add_book(request):
    #添加方式一
    #  获取出版社对象
    #pub_obj = Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    #book = Book.objects.create(title="cainiaojiaocheng", price=200, pub_date="2010-10-10", publish=pub_obj)


    #添加方式二
    #  获取出版社对象
    #pub_obj = Publish.objects.filter(pk=1).first()
    #  获取出版社对象的id
    #pk = pub_obj.pk
    #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    #book = Book.objects.create(title="chonglingjianfa", price=100, pub_date="2004-04-04", publish_id=pk)


    #关联方式一
    #  获取作者对象
    #chong = Author.objects.filter(name="lhc").first()
    #ying =  Author.objects.filter(name="ryy").first()
    #  获取书籍对象
    #book = Book.objects.filter(title="cainiaojiaocheng").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    #book.authors.add(chong, ying)

    #关联方式二
    #  获取作者对象
    #chong = Author.objects.filter(name="lhc").first()
    #  获取作者对象的id
    #pk = chong.pk
    #  获取书籍对象
    #book = Book.objects.filter(title="chonglingjianfa").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象的id
    #book.authors.add(pk)

    #pub = Publish.objects.filter(name="mjcbs").first()
    #wo =  Author.objects.filter(name="rwx").first()
    #book = wo.book_set.create(title="xxdf", price=300, pub_date="1999-9-19", publish=pub)
    #print(book, type(book))


    res = Book.objects.aggregate(Avg("price"))
    print(res, type(res))

    return HttpResponse("Hello world ! ")


def add_emp(request):
    if request.method == "GET":
        form = My_forms.EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = My_forms.EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            data.pop('r_salary')
            print(data)
            return HttpResponse(
                'ok'
            )
            # return render(request, "add_emp.html", {"form": form})
        else:
            print(form.errors)    # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})