from django.shortcuts import render

# Create your views here.



# def register(response):
#     if response.method == 'POST':
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.person.birthdate = form.cleaned_data.get('birthdate')
#             user.person.discord_id = form.cleaned_data.get('discord_id')
#             user.person.zoom_id = form.cleaned_data.get('zoom_id')
#             user.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(response, user)

#             return redirect('/')

#         else:
#          form = RegisterForm()

#     return render(response, 'manager/register.html', {'form': form})