# from django.shortcuts import render, redirect
# from django.views import View
# from django.views.generic import ListView
# from Lpage.forms import SubscriberEntryForm
# from Lpage.models import Subscriber
#
# # Create your views here.
# class homeview(View):
#
#     def get(self,request):
#         msg = request.session.get('msg', False)
#         if(msg):
#             del(request.session['msg'])
#         return render(request,'Lpage/index.html',{'message' : msg})
#
#     def post(self, request):
#         form = SubscriberEntryForm(request.POST or None)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.save()
#             request.session['msg'] = "Your subsciption was successfull"
#             return redirect('thanks')
#         else:
#             name=form.cleaned_data['name']
#             return redirect('message')
#
#
#
# def messageview(request):
#
#     return render(request,'Lpage/messages.html')
#
# def thanksview(request):
#     return render(request,'Lpage/thankyou.html',{})
#
# class UserListView(ListView):
#     model = Subscriber
#     template_name = 'Lpage/user_list.html'
#     ordering = ['-updated']
