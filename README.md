<h2>MultipleDB</h2>
1. Deault 

2. another

3. MongoDB
   Steps: 

   - For mongodb we have to create an app **mongoDBWork**
   - install djongo for MongoDB engine 
           ```
              pip install djongo

           ```
   - Add Db engine on setting.py
         ```python
            .
            .   
            }
            'mongo':{
                "ENGINE": "djongo",
                "NAME": "local",
                'HOST': '127.0.0.1',
                'PORT': 27017,
            }

         ```
    - Since it is not default Database we Have to add DATABASE_ROUTERS for this DB
        ```python 
           DATABASE_ROUTERS = ['otherdbapp.router.OtherAppDB',"mongoDBwork.router.MongoDBRouter"]
        ```
        Description of DATABASE_ROUTERS:<br>
        mongoDBwork : App Name
        router : router.py file inser
        MongoDBRouter: class name on the router.py file 
        Please have a look on router.py file 







<br>


<br>


<h2>Testcase: </h2>

<p>Unittest is very importent for CI/CD. Whenever you wirte a code you need to initaiate test case for this code</p>
<br>

<p>Below I have added some code for testing the views functions( get apis)</p>


1. urls.py for otherdbapp

```python

	urlpatterns = [
          #url(r'^admin/', admin.site.urls),
   	  url(r'create_user', create_user),
  	  url(r'get_user/', get_user),
	]
```
<br>
from the urls.py we can see there is two basic(not REST) apis path(create_user, get_user). Now we can move the views function these path

<br>
2.  The view function for these two url path are given here <strong>views.py</strong>


```python
def create_user(requests):
    try:
        first_name = requests.GET.get("first_name")
        last_name = requests.GET.get("last_name")
        phone =  requests.GET.get('phone')
        email = requests.GET.get('email')
        data = Users.objects.create(first_name= first_name, last_name= last_name, phone = phone, email = email)
        uuid = data.id
        return Response_data.success_response([{'id': uuid}])
    except Exception as E:
        return Response_data.failure_response("Something Went Wrong", str(E))



def get_user(requests):
    return Response_data.failure_response("Something Went Wrong", "")	

```

3. Now we can write testcase for these two functions   <strong>test.py</strong><br>


```python


class TestView(unittest.TestCase):
    def test_create_users(self):
        client = Client()
        response= client.get(reverse(create_user), {'first_name': 'john', 'last_name': 'smith', 'phone': "......", 'email': "/........."})
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        client = Client()
        response= client.get(reverse(get_user))
        self.assertEqual(response.status_code, 450)

```








