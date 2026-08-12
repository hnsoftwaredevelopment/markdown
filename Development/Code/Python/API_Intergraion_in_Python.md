API_Intergraion_in_Python

# API Integration in Python – Part 1

by [Real Python](https://realpython.com/api-integration-in-python/#team) [51 Comments](https://realpython.com/api-integration-in-python/#reader-comments)  [api](https://realpython.com/tutorials/api/) [basics](https://realpython.com/tutorials/basics/) [web-dev](https://realpython.com/tutorials/web-dev/)

Table of Contents

- [How to Make Friends and Influence APIs](https://realpython.com/api-integration-in-python/#how-to-make-friends-and-influence-apis)
- [Talking REST](https://realpython.com/api-integration-in-python/#talking-rest)
- [Constructing an API Library](https://realpython.com/api-integration-in-python/#constructing-an-api-library)
- [Coming in Part 2](https://realpython.com/api-integration-in-python/#coming-in-part-2)
- [Appendix: REST in a nutshell](https://realpython.com/api-integration-in-python/#appendix-rest-in-a-nutshell)



[![img](assets/debff3e0f366daf7d4afd4217dfd9fee.png)](https://srv.realpython.net/click/26004507324/?c=55980524899&p=58946116052&r=95734)

The following is a guest post by Aaron Maxwell, author of [Livecoding a RESTful API Server](https://powerfulpython.com/store/restful-api-server/).

## How to Make Friends and Influence APIs

More and more, we’re all writing code that works with remote APIs. Your magnificent new app gets a list of your customer’s friends, or fetches the coordinates of nearby late-night burrito joints, or starts up a cloud server, or charges a credit card… You get the idea. All this happens just by making an HTTPS request.

(At least, I hope it’s HTTPS. Please don’t use plain HTTP. But that’s a different topic.)

So how do you use this in your code? Ideally, the people behind the web service will provide an SDK or library that does all the above so you can just “pip install openburrito-sdk”, or something, and just start using its functions and methods to find late-night burrito joints immediately. Then you won’t have to deal with making HTTP requests at all.

That’s not always available, though, especially if you are using an internally developed API, which is very common when your architecture is based on microservices or trying to be based on microservices.

**That’s what this article is about: writing Python code to integrate with RESTful APIs, in a way that is as fun, easy, and quick as possible—and makes you look good doing it!**(Hopefully.)

**Free Bonus:** [Click here to download a copy of the "REST in a Nutshell" Guide](https://realpython.com/api-integration-in-python/) with a hands-on introduction to REST API principles and examples.

Sound exciting? Great, let’s get started!

## Talking REST

First, if you are not sure what the phrase “REST API” means, [jump to the appendix](https://realpython.com/api-integration-in-python/#appendix-rest-in-a-nutshell) for a crash course.

Got it? Good, let’s keep going. There are many ways in which such web services can be organized and many formats in which you can pass it data and then get other data back. Right now, it’s popular to make your API RESTful, or at least claim it’s RESTful. As for sending data back and forth, the [JSON format](https://realpython.com/python-json/) is very popular.

Tragically, I have so far failed in my campaign to persuade everyone to use YAML instead of JSON. Despite this heartbreaking setback, there is a silver lining: the same key principles apply to any HTTP API, using any data format.

The examples below will be for a REST API, using JSON. But what you are about to learn will apply when I prevail, and we are all joyously using YAML. It also applies to XML or custom data formats as well as un-RESTful architectures. It’ll even work next year, when we’re all checking email via telepathic neural implants!

Let’s use a concrete example. Imagine a to-do list API, tracking your action items on your road to success. Here are its methods and endpoints:

- **GET /tasks/**

  Return a list of items on the to-do list, in the following format:

  ```json
  {
      "id": "<item_id>", 
      "summary": "<one-line summary>"
  }
  ```

- **GET /tasks/<item_id>/**

  Fetch all available information for a specific to-do item, in the following format:

  ```json
  {
      "id": "<item_id>", 
      "summary": "<one-line summary>", 
      "description" : "<free-form text field>"
  }
  ```

- **POST /tasks/**

  Create a new to-do item. The POST body is a JSON object with two fields: “summary” (must be under 120 characters, no newline), and “description” (free-form text field). On success, the status code is 201, and the response body is an object with one field: the id created by the server (for example, `{ "id": 3792 }`).

- **DELETE /tasks/<item_id>/**

  Mark the item as done: strike it off the list so that GET `/tasks/` will not show it. The response body is empty.

- **PUT /tasks/<item_id>/**

  Modify an existing task. The PUT body is a JSON object with two fields: `summary` (must be under 120 characters, no newline), and `description` (free-form text field).

**Note:** Unless otherwise noted, all actions return 200 on success; those referencing a task ID return 404 if the ID is not found. The response body is empty unless specified otherwise. All non-empty response bodies are JSON. All actions that take a request body are JSON (not form-encoded).

Great. Now, how do we interact with this thing? In Python, we are lucky to have an excellent HTTP library: Kenneth Reitz’ `requests`. It’s one of the few projects worth treating as if it is part of the standard library:

```python
# Step one for every Python app that talks over the web
$ pip install requests
```

This is your primary tool for writing Python code to use REST APIs—or any service exposed over HTTP, for that matter. It gets all the details right, and has a brilliantly elegant and easy to use interface. You get the point. I’m going to stop with the gushing praise now, and show you how to use it.

Let’s say you want to get a list of action items, via the `GET /tasks/` endpoint:

```python
import requests

resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))
```

Notice the following:

- The `requests` module has a function called `get` that does an HTTP GET.
- The response object has a method called `json`. This takes the response body from the server—a sequence of bytes—and transforms it into a Python list of dictionaries, *à la*`json.loads()`.

After some error checks and minimal processing, what you get out of the API call is a list of Python dictionaries, each representing a single task. You can then process this however you wish (printing them out, for example).

Now suppose I want to create a new task: add something to my to-do list. In our API, this requires an HTTP POST. I start by creating a Python dictionary with the required fields, “summary” and “description”, which define the task. Remember how response objects have a convenient `.json()` method? We can do something similar in the other direction:

```python
task = {"summary": "Take out trash", "description": "" }
resp = requests.post('https://todolist.example.com/tasks/', json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))
```

Notice the following:

- `requests` sensibly provides a function called `post`, which does an HTTP POST. Dear Lord, why can’t all HTTP libraries be this sane?
- The `post` function takes a `json` argument, whose value here is a Python dictionary (`task`).
- Per the API spec and REST best practices, we know the task is created because of the 201 response code.

Now, since we are using JSON as our data format, we were able to take a nice shortcut here: the `json` argument to `post`. If we use that, `requests` will do the following for us:

- Convert that into a JSON representation string, *à la* `json.dumps()`
- Set the requests’ content type to `"application/json"` (by adding an HTTP header).

If you are using something other than JSON (some custom format, XML, or everybody’s favorite, YAML) then you need to do this manually, which is a bit more work. Here’s how it looks:

```python
# The shortcut
resp = requests.post('https://todolist.example.com/tasks/', json=task)
# The equivalent longer version
resp = requests.post('https://todolist.example.com/tasks/',
                     data=json.dumps(task),
                     headers={'Content-Type':'application/json'},
```

We use the `data` argument now: that’s how you specify the contents of the POST body. As you can see, `requests.post` takes an optional `headers` argument: a dictionary. This adds each key as a new header field to the request. `get()` and the others all accept this argument too, by the way.

## Constructing an API Library

If you are doing anything more than a few API calls, you’ll want to make your own library to keep yourself sane. Of course, this also applies if you are the one providing the API and want to develop that library so that people can easily use your service.

The structure of the library depends on how the API authenticates, if it does at all. For the moment, let’s ignore authentication, to get the basic structure. Then we’ll look at how to install the auth layer.

Glance again at the API description above. What are the specific actions and services it provides? In other words, what are some of the things it allows us to do?

- We can get a summary list of tasks that need to be done.
- We can get much more detailed information about a specific task.
- We can add a new task to our to-do list.
- We can mark a task as done.
- We can modify an existing task (changing its description, and so on).

Instead of thinking about HTTP endpoints, we can create our own internal API based on these concepts. This lets us more easily integrate the logic of using the API in our code, without being distracted by the details.

Let’s start with the simplest thing that could possibly work. I’m going to create a file named `todo.py`, defining the following functions:

```python
# todo.py
def get_tasks():
    pass
def describe_task(task_id):
    pass
def add_task(summary, description=""):
    pass
def task_done(task_id):
    pass
def update_task(task_id, summary, description):
    pass
```

Notice a few design decisions I made here:

- All parameters are explicit. For `update_task()`, for example, I have three arguments, instead of a single dictionary with three keys.
- In `add_task()`, I anticipate that sometimes I will want to create a task with just a summary field—“get milk” doesn’t really need elaboration, for example—so give `description` a sensible default.
- These are functions in a module. That is a useful organization in Python. (In Java, I’d have to create a class with methods, for example.)

To fill these out, I am going to define a helper:

```python
def _url(path):
    return 'https://todo.example.com' + path
```

This just constructs the full URL to make the API call, relative to the path. With this, implementing the helper is straightforward:

```python
import requests

def get_tasks():
    return requests.get(_url('/tasks/'))

def describe_task(task_id):
    return requests.get(_url('/tasks/{:d}/'.format(task_id)))

def add_task(summary, description=""):
    return requests.post(_url('/tasks/'), json={
        'summary': summary,
        'description': description,
        })

def task_done(task_id):
    return requests.delete(_url('/tasks/{:d}/'.format(task_id)))

def update_task(task_id, summary, description):
    url = _url('/tasks/{:d}/'.format(task_id))
    return requests.put(url, json={
        'summary': summary,
        'description': description,
        })
```

I can use this like so:

```python
import todo

resp = todo.add_task("Take out trash")
if resp.status_code != 201:
    raise ApiError('Cannot create task: {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))

resp = todo.get_tasks()
if resp.status_code != 200:
    raise ApiError('Cannot fetch all tasks: {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))
```

Notice that each of my library functions returns a response object, just like `requests.get` and friends. This is often a useful choice. Generally, when working with APIs, you will want to inspect the status code and the payload (from `resp.json()` in this case). The response object provides easy access to this, and other information we might need, but did not anticipate when we first made the library.

You might be thinking this is exposing implementation details. Wouldn’t it be better to construct some kind of `ApiResponse` class that provides the needed info through a more explicit interface? While that can sometimes be the best approach, I have more often found it to be over-engineering.

I recommend that you start by just returning simple response objects. If you later need to install a response abstraction layer, you’ll know when the time comes.

## Appendix: REST in a nutshell

REST is essentially a set of useful conventions for structuring a web API. By “web API,” I mean an API that you interact with over HTTP, making requests to specific URLs, and often getting relevant data back in the response.

There are whole books written about this topic, but I can give you a quick start here. In HTTP, we have different “methods,” as they are called. GET and POST are the most common; these are used by web browsers to load a page and submit a form, respectively. In REST, you use these to indicate different actions.

GET is generally used to get information about some object or record that already exists. Crucially, the GET does not modify anything, or at least it isn’t supposed to. For example, imagine a kind of to-do list web service. You might do an HTTP GET to the URL `/tasks/` to get a list of current tasks to be done. So it may return something like this:

```json
[
  { "id": 3643, "summary": "Wash car" },
  { "id": 3697, "summary": "Visit gym" }
]
```

This is a list of JSON objects. (A “JSON object” is a data type very similar to a Python dictionary.)

In contrast, POST is typically used when you want to create something. So to add a new item to the todo list, you might trigger an HTTP POST to `/tasks/`. That’s right: it is the same URL, which is allowed in REST. The different methods GET and POST are like different verbs, and the URL is like a noun.

When you do a POST, normally you will include a body in the request. That means you send along some sequence of bytes—some data defining the object or record you are creating. What kind of data? These days, it’s very common to pass JSON objects. The API may state that a POST to `/tasks/` must include a single object with two fields, “summary” and “description”, like this:

```json
{
  "summary": "Get milk",
  "description": "Need to get a half gallon of organic 2% milk."
}
```

This is a string, encoding a JSON object. The API server then parses it and creates the equivalent Python dictionary.

What happens next? Well, that depends on the API, but generally speaking, you will get a response back with some useful information, along two dimensions.

First is the status code. This is a positive number, something like 200 or 404 or 302. The meaning of each status code is well defined by the HTTP protocol standard. Search for “http status codes”, and the first hit will probably be the official reference. Anything in the 200s indicates success.

The other thing you get back is the response body. When your web browser GETs a web page, the HTML sent back is the response body. For an API, the response body can be empty or not. It depends on the API and the end point. For example, when we POST to `/tasks/` to add something to our to-do list, we may get back an automatically assigned task ID. This can again be in the form of a JSON object:

```json
{ "id": 3792 }
```

Then if we GET `/tasks/` again, our list of tasks will include this new one:

```json
[
  { "id": 3643, "summary": "Wash car" },
  { "id": 3697, "summary": "Visit gym" },
  { "id": 3792, "summary": "Get milk" }
]
```

There are other methods besides GET and POST. In the HTTP standard, PUT is used to modify an existing resource (like change a task’s summary). Another method called DELETE will… well, delete it. You could use this when a task is done, to remove it from your list.

There is a lot more to REST than this. However, this is enough information for you to get started. [Jump back to “Talking REST”](https://realpython.com/api-integration-in-python/#talking-rest).