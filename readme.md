## Project: Global Historical Climatology Network

This project explains the climatic conditions of different latitude and longitude shown in the data. The Global Historical Climatology Network (GHCN) is an integrated database of climate summaries from land surface stations across the globe. This data set contains gridded mean temperature anomalies, or departures from a reference value or long-term average, from the Global Historical Climatology Network-Monthly (GHCN-M) version 3.2.1 temperature data set. The gridded anomalies were produced from GHCN-M bias corrected data. Each month of data consists of 2,592 gridded data points produced on a 5° by 5° basis for the entire globe (72 longitude by 36 latitude grid boxes).

-   **Frequency**: Monthly
-   **Period**: 1880 to 2016

Another reason for developing it is to find the average of the temperatures in different regions  

## How to start it

-   Create a new project folder called 'Climate_stories' and then cd into the folder via the terminal and execute these commands:
    
   ```
pyenv local 3.10.7 # this sets the local version of python to 3.10.7
python3 -m venv .venv # this creates the virtual environment for you
source .venv/bin/activate # this activates the virtual environment
pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```
    
   
    
-   then We used Django ([https://www.djangoproject.com](https://www.djangoproject.com/)) as our web framework for the application. We installed that with
    
    ```
     pip install Django==4.1.2
    
    ```
    
-   Now we can start to create the site using the django admin tools. Issue this command, and don't forget the '.' at the end of the line, which says 'create the project in this directory'. This will create the admin part of our application, which will sit alongside the actual site.
    
    ```
    django-admin startproject mysite .
    

- We need to specify some settings for the site, which we do in the mysite/settings.py file. Open this and add this line above the line for pathlib import Path:
    
    
    ```
      import os

- Now go to the end of the file to add a line specifying the root directory for the static files.
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
- Now go further up the file to 'ALLOWED_HOSTS' so that we can run this beyond 'localhost' and 127.0.0.1, which are the only allowed ones if this is empty. Modify this accordingly to suit your needs:

```
ALLOWED_HOSTS = [ 'https://groupindia.onrender.com','groupindia.onrender.com', '127.0.0.1', 'beyondlaura-exceptvisa-8000.codio-box.uk', 'localhost', 'spendminimum-stadiumjaguar-8000.codio-box.uk', 'politicpermit-freedompastel-8000.codio-box.uk', 'opinionwave-octaviagordon-8000.codio-box.uk', 'ingridinfo-designlogo-8000.codio-box.uk', 'salsanurse-arthurcosmos-8000.codio-box.uk', 'infohavana-maydaypenguin-8000.codio-box.uk', 'rajapicture-comedystatic-8000.codio-box.uk', 'miketopic-rentgraph-8000.codio-box.uk','rajapicture-comedystatic-8000.codio-box.uk']
```
- Although we are not using a database for this application, django uses one in the background. We now need to configure this database, which you saw was already detailed in the settings.py file. As django has a built-in admin tool, it already knows some of the tables that it needs to use. We can set this up with the command:

```
           python3 manage.py migrate
```
## Start the server 

    
- We can now use the manage.py command tool to start the development server by entering this command in the terminal:    
    ```
      python3 manage.py runserver
    ```
- If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):
```
      python3 manage.py runserver 0.0.0.0:8000
```
 - If it went well, then you should see the python rocket launching your site when you open the browser at the site.  

## Creating the Story content

Leave the server running. Open a new terminal and navigate as required to the same directory. We can now set about creating the space for our Climate_stories，
```
    python3 manage.py startapp group_india
```
- This will create a new folder for us including space for database migrations, and other details specific to our content. By the way, we need to use an underscore to join the words in temp_stories as a hyphen is not allowed as part of an identifier in django applications.

- Django needs to know the urls of the site so that it can serve up pages to visitors, and tell others that the page requested isn't part of the site. We do that by opening mysite/urls.py and adding a line for the pages that will be under Climate_stories.

-   First, add 'include' to the line with 'import path' so that it reads

  ```
           from django.urls import path, include
```
  
-   Second, add this line (plus the , at the end of the line above it), to have django find your Climate_stories pages:
```
       path('', include('climatology_stories.urls')),
```
- Third, we need to modify the settings.py file in the mysite app, so that it knows to include the 'Climate_stories' contents. We do this by adding a line in the section on 'INSTALLED_APPS'. Add this line to the end of the block ( plus the , at the end of the line above it).

 ```
        'climatology_stories.apps.ClimatologyStoriesConfig',
```
- Fourth, we need to tell Climate_stories about the URLs it is using, so that they can be added to the list of URLs (pages) used by 'mysite'. We do that by creating the file urls.py in the 'Climate_stories' folder. It should hold these details:
```
         from django.urls import path

from climatology_stories import views

  

urlpatterns = [

path('', views.index, name='index'),
```


- As you can see this is similar to the code we used in the flask version of the site. The only differences are that we're now passing in the 'request' object to the index method, and use that in the template rendering, and we also create a dictionary object to pass to the template. The ideas are the same, but the syntax is slightly different.

- For the templates we need to put the index.html file into a 'templates' directory. Create that, and then create a 'climate_stories' directory under 'templates'. This is a Django convention, and helps us separate out the content for our site if we added other components to the site.

- Now create a blank index.html file and put this code into it. This is almost the same as what we used in the flask version. We've only changed the text in the file
```
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Climate Data Site</title>

<link rel="stylesheet"

href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<link rel="stylesheet"

href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.2/css/bootstrap.min.css">
```
- We are now ready to run the changes to see the page load. Stories should now appear when you load the page on the site. You can change the nouns, adjectives and other parts of mystory with values from Faker. Go to  [https://faker.readthedocs.io/en/stable/providers.html](https://faker.readthedocs.io/en/stable/providers.html)  and look through the options for Standard Providers and make some changes to mystory

 ## Adding in the temperature conversion form
- We can add a form to the page so that we can add a temperature conversion that's added to the story. Weird, but it makes the exercise more interesting.
- Open up views.py and add modify the index method so that it looks like this:
 ```
def years(request):

try:

year =  int(request.GET.get('year', None))

except:

year =  1880

years = Year.objects.all()

paginator = Paginator(years, 20)

page_number = request.GET.get('page')

page_obj = paginator.get_page(page_number)

return render(request, 'climatology_stories/years.html', {'page_obj': page_obj, 'year': year})
```
- We need to add a line to the settings.py file that will tell Django that the csrf token used in our form is valid. Add this line below the Allowed hosts line:
```
CSRF_TRUSTED_ORIGINS =  ['https://scharlau.pythonanywhere.com', 'localhost']
```
- Amend the server name to suit your system. Save the changes, and reload the pages to see it in action.
## Do Some  changes
- We're now ready for you to modify the site to learn a bit more about how you use Django and understand the relationship between the components. This is mostly a quick intro without models and tables to let you focus on the structure of a Django application.

- You can take this further in three stages:

    1.  Clean up the code in views.py by moving the temperature convertion to a separate method so that you can add the two temperatures to the story, and still display the 'conversion sentence' too.
  2.  Separate out the temperature conversion as a new app in 'mysite' that is called 'convert' and has a form for converting temperatures from farhrenheit to celsius.
  3.  Push the boundaries further to see what else you might do with Django.

    

## Installation

- Clone or download the project code:

```
git clone https://github.com/your_username/app.git

```

- Enter the project directory:

```
cd app

```

- To create and activate a Python virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate

```

- Python dependencies required to install the project:

```
 pip install Django==4.1.2
 pyenv install 3.11.0
 pip install --upgrade pip
 pip3 install whitenoise
```

- Run the application (take the codio run as an example)

```
python3 manage.py runserver 0.0.0.0:8000
```

- Visit the following URL in your Web browser to view the application:

```
https://rajapicture-comedystatic-8000.codio-box.uk/

```

## USE

1.  The page displays a list of applications. You can click the Details button to see the details of your application.
2.  On the application list page, you can use the paging control to browse applications on different pages.




