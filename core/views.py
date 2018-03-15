#from django.http import HttpResponse


#def hi(request, n1, n2):
    #w=request.GET.get('w')
    # s='<hi>Hello World</h1>'
    # return HttpResponse('<h1>{}</h1>'.format(n1+n2))

from django.shortcuts import render

def hi(request, n1, n2):
    s = n1 + n2
    return render(request, 'hi.html', {
        's' : s,
    })

def r(request, start, stop):
    if start > stop:
        start, stop = stop, start

    rr = range(start, stop+1)
    rr = reversed(rr)
    return render(request, 'r.html',{
        'rr' : rr,
    })