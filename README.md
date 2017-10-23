### Django BucketList API

According to the Oxford Dictionary, a BucketList is a number of experiences or achievements that a person hopes to have or accomplish during their lifetime.

This is a Django API for an online BucketList service.

### Installation and Setup

Clone the repository from GitHub:
```
$ git clone https://github.com/WNjihia/django-bucketlist-api.git
```

Fetch from the develop branch:
```
$ git fetch origin develop
```

Navigate to the `bucketlist_api` directory:
```
$ cd bucketlist_api
```

Create a virtual environment:
```
$ virtualenv -p /usr/local/bin/python3 env
```

Activate your virtual environment:
```
source env/bin/activate
```

Install the required packages:
```
$ pip install -r requirements.txt

```

Navigate to the `djangoapi` directory and create the database:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Then create an administrative user:
```
python manage.py createsuperuser
```

To start the server, run:
```
python manage.py runserver
```

You can now access the bucktlist service on your browser using:
```
http://localhost:8000/
```

### API Endpoints

| Methods | Resource URL | Description | Public Access |
| ---- | ------- | --------------- | ------ |
|POST| `/api/v1/auth/login` | Logs a user in| TRUE |
|POST| `/api/v1/auth/register` |  Register a user | TRUE |
|POST| `/api/v1/bucketlists/` | Create a new bucket list | FALSE |
|GET| `/api/v1/bucketlists/` | List all the created bucket lists | FALSE |
|GET| `/api/v1/bucketlists/<bucketlist_id>/` | Get single bucket list | FALSE |
|PUT| `/api/v1/bucketlists/<bucketlist_id>/` | Update this bucket list | FALSE |
|DELETE| `/api/v1/bucketlists/<bucketlist_id>/` | Delete this single bucket list | FALSE |
|POST| `/api/v1/bucketlists/<bucketlist_id>/items/` | Create a new item in bucket list | FALSE |
|GET| `/api/v1/bucketlists/<bucketlist_id>/items/` | List items in this bucket list | FALSE |
|GET| `/api/v1/bucketlists/<bucketlist_id>/items/<item_id>/` | Get single bucket list item | FALSE |
|PUT|`/api/v1/bucketlists/<bucketlist_id>/items/<item_id>/` | Update a bucket list item | FALSE |
|DELETE|`/api/v1/bucketlists/<bucket_id>/items/<item_id>/` | Delete an item in a bucket list | FALSE |
|GET| `/api/v1/bucketlists?limit=2` | Pagination to get 2 bucket list records per page | FALSE |
|GET| `/api/v1/bucketlists?search=bucket` | Search for bucket lists with name like ```bucket``` | FALSE |
|GET| `/api/v1/bucketlists/<bucketlist_id>/items?limit=2` | Pagination to get 2 bucketlist items per page | FALSE |
|GET| `/api/v1/bucketlists/<bucketlist_id>/items?search=climb` | Search for bucketlist items with name like ```climb``` | FALSE |

### Testing

To test, run the following command:
```
nosetests
```
