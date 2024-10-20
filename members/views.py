from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from datetime import datetime

def members(request):
    if len(request.GET) != 0: #Checking whether the dictionary response is empty or not, basically checks whether something is written in the username or not.
        #Lets get the username first, makes it easier to work with
        username = request.GET.get("username") #Here since the dictionary has a key value pair with username as one and only key, we simply use get(key), we can choose to not use it but it gives None instead of error if the key doesnt exist for some reason

        if len(username)>0:
            url_to_api = f"https://api.github.com/users/{username}"
            username_response = requests.get(url_to_api)

            if username_response.status_code == 200: #checking whether the API returned a valid response, i.e. the username exists and Github servers are sending the data normally
                user_data = username_response.json()#get that data in json format 
                user_data["created_at"] = datetime.strptime(user_data["created_at"][:10], '%Y-%m-%d').date()
                repos_url = user_data["repos_url"]
                repos_data = requests.get(repos_url).json()[:5] #get the first five repos

                for i in repos_data:
                    i["updated_at"] = datetime.strptime(i["updated_at"][:10], '%Y-%m-%d').date()
                return render(request, 'result.html', 
                              {
                                  'user_data': user_data,
                                  'repos_data': repos_data
                              })
            else:
                return render(request, 'notfound.html')
            
    return render(request, 'mysecond.html')
            