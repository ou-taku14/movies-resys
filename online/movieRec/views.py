from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pandas as pd
import pickle
with open("rank10.pkl","rb") as fr:
    r10 = pickle.load(fr)
movie_detail = pd.read_csv("movie_detail.csv",index_col=0)

def index(request):
	return render(request,'index.html')

def rec(request):
	if request.POST:
		userid = int(request.POST['userid'])
		r10_detail = movie_detail[movie_detail.movieId.isin(r10[userid])]
		r10_img = r10_detail.img.values
		return render(request,'rec.html',context={'data':r10_img})
	else:
		return HttpResponse('please visit us with POST')