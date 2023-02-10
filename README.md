# TSL NIGERIA Streamit API

## Welcome to TSL Nigeria API.

The API has a couple of endpoints that gives you access to the database. The base URL allows you to make requests along side sub-endpoints or paths.

### Base URL

```
https://web-production-93c3.up.railway.app/
```

Note that every endpoint must have an ending slash. This shows that it is an absolute URL. With the base URL above, requests can be made to various endpoints.

## Requests and Responses

This API gives you access to create and authenticate users, add and remove videos, categories, like videos, add videos to favourites, list and display videos and categories, user profiles and details, et cetera.

# POST, GET - /user/

Here, you can retrieve, create, and delete users from the database. Although you should note that each user is conected to a profile object i.e when a user is deleted, the profile will be deleted automatically. When a user is created on the otherhand, a profile is created too.

The required fields necessary to create a user are `email`, `password` and `password2`.
The `password2` field is used to compare the users' passwords to see if they match.

```
{Base_Url}/user/
```

For detail view:

```
{Base_Url}/user/{id}/
```

```json
{
  "email": "validemail@gmail.com",
  "password": "string",
  "password2": "string"
}
```

If `password` and `password2` does not match, an exception is raised:

```json
{
  "password": "Password must match"
}
```

Creating a user that already exist, will give you the following error:

```json
{ "email": ["user with this email already exists."] }
```

You will get this success message when a user is created:

```json
{
  "email": "sarah@gmail.com",
  "is_superuser": false,
  "is_active": false,
  "date_joined": "2023-01-20T13:12:00.268410Z",
  "last_login": null
}
```


# GET, DELETE - /user/:id/

This endpoint retrieves or deletes a single user with a declared id.
Here, you must ensure you send a request with the user id from the client side.

Although deleting a user might come in handy to a site admin or to a client user who wishes to delete his user account, but this should be used with caution.
This is because, when a user instance is deleted, the profile associated with it is also deleted automatically. This means that the user cannot log into his or her account until he creates another user instance.

```
{Base_Url}/user/
```

For detail view:

```
{Base_Url}/user/{id}/
```

The response returned when a user is successfully deleted is as folllows:

```json
{
  "details": "user {id} was successfully deleted"
}
```

A GET request on the other hand fetches you that single user as follows:

```json
{
  "email": "user@gmail.com",
  "is_superuser": false,
  "is_active": true,
  "date_joined": "2023-01-21T05:45:39.075086Z"
}
```



# POST /user/auth-token/

The above is used to authenticate existing users. Please note that this endpoint does not allow a GET request. After a user has been created, this endpoint is used to retrieve the user's `Auth Token` that is used to authenticate the user. The client do not need to authenticate before accessing this endpoint.

```
{Base_Url}/user/auth-token/
```

Inorder to make a request, the user must send in a json object. He should ensure that these json objects are properly stringified in the following format, having the following keys and values:

```json
{
  "username": "validemail@gmail.com",
  "password": "validpassword"
}
```

Keys: `username` and `password`.
The `username` key requires the email of an existing user.
The `password` key requires a valid password.

Both `username` and `password` feilds are required.
If a request is sent without the above two fields, a response is returned telling the user that both fields are required.

## Expected Response

A JWT Token will be generated as a result of your request in this format:

```json
{
  "token": "afbf91b454b50cc56637d34b77133fef3c6604da",
  "user_id": 1,
  "email": "peter@gmail.com"
}
```

Keys: token, user_id, email.

The above token example should be included in the `Authorization` header in order to make subsequent requests. Without the token given, an exception of `UnAuthorized user` will be raised.

If either the password or username (email) entered is inaccurate, a `non_field_error` is raised.

`{'non_field_errors': ['Unable to log in with provided credentials.']}`

You can customize the error however way you would wish in any client-side application like React, Angular or Vue.


# PUT - /user/change-password/

Here, the password can be changed via the above endpoint.
This change must be made via http headers - i.e. the `Authorization` header.
The parameters that should be provided are as follows:

####

```json
{ "old_password": "password", "new_password": "password2" }
```

#### old_password: string; new_password: string

# GET - /profile/

The fields existing for uploading a profile are `username`, `first_name`, `last_name`, `profile_photo`, `bio`, `country`, `gender` and `phone_number`. None of these fields are required. It is advisable to only make queries with `user_id`, not modify it. You can query the user profile via the `user_id` if your intention is to get the user's profile details. `user_details` is automatically generated from the user object. This is because a Profile object is created alongside a User object by default. Hence, the user_id and profile_id are the same.
Do not send a POST request to the profile object. POST request is not permitted. You can only send a POST request to the user, i.e. WHEN YOUR INTENTION IS TO CREATE A USER. Use a PUT request instead.
A PUT request is ideal for updating the user profile.

This means that you can use the user_id or profile_id interchangeably. We do this to ensure that every user instance is connected to a Profile object. You can make your queries with the endpoints below:
For list view:

```
{Base_Url}/profile/
```

The above request will fetch you all the user profiles in the database.

# PUT, GET, DELETE - /profile/:id/

For detail view:

```
{Base_Url}/profile/{id}/
```

## Request via PUT

You can choose to modify any of the following via a PUT request.

```json
{
  "username": "",
  "first_name": "",
  "last_name": "",
  "profile_photo": "/path/to/media/file",
  "bio": "",
  "country": "",
  "gender": "",
  "phone_number": ""
}
```

Note that every PUT request made gives you back the same object.
If you wish to give back a custom reponse to your user. You can make use of your status_code attribute.
Every successfully request has a status code of 200.

## Response via GET

```json
{
  "user_details": {
    "id": 1,
    "email": "peter@gmail.com",
    "is_superuser": true,
    "is_active": true,
    "date_joined": "2023-01-22T02:53:33.065144Z"
  },
  "username": "",
  "first_name": "",
  "last_name": "",
  "profile_photo": null,
  "bio": "",
  "favourite_videos": [],
  "country": "",
  "gender": "",
  "phone_number": ""
}
```

# GET, POST - /video/

The video object can be queried via a GET request using the endpoints below the endpoint below:

```
{Base_Url}/video/
```

The above gives you the array (or list) of videos and their respected a respective `id`, `title`, `thumbnail`, `author`, `category`,`likes`, `date_uploaded`, `last_modified`, etc. A typical response from a GET request is as follows:

```json
{
  "id": 1,
  "title": "Be my Val",
  "mobile_thumbnail": "https://res.cloudinary.com/daf9tr3lf/image/upload/v1/media/thumbnail/7F8503DA-D9A0-423A-BFC1-96635A16DF5C_c5jybf",
  "desktop_thumbnail": "https://res.cloudinary.com/daf9tr3lf/image/upload/v1/media/thumbnail/7F8503DA-D9A0-423A-BFC1-96635A16DF5C_gmdmbm",
  "mobile_banner": "https://res.cloudinary.com/daf9tr3lf/image/upload/v1/media/banner/7F8503DA-D9A0-423A-BFC1-96635A16DF5C_izgfdl",
  "desktop_banner": "https://res.cloudinary.com/daf9tr3lf/image/upload/v1/media/banner/7F8503DA-D9A0-423A-BFC1-96635A16DF5C_rhdklw",
  "description": "This is the season of love",
  "video_link": "http://youtube.com",
  "_category": {
    "id": 1,
    "name": "Hot Stuff"
  },
  "likes": 0,
  "actors": [
    {
      "id": 1,
      "name": "Matilda",
      "bio": "",
      "image": "https://res.cloudinary.com/daf9tr3lf/image/upload/v1/media/profile/actors/7F8503DA-D9A0-423A-BFC1-96635A16DF5C_i89gws"
    },
    {
      "id": 2,
      "name": "Jennifer",
      "bio": "",
      "image": "https://res.cloudinary.com/daf9tr3lf/image/upload/v1/media/profile/actors/7F8503DA-D9A0-423A-BFC1-96635A16DF5C_hkcmqo"
    }
  ],
  "playlist": 1,
  "rating": "18+",
  "mood": ["Lovely", "Happy"],
  "genres": ["Classic", "Sci Fy"],
  "publish": false,
  "date_uploaded": "2023-02-01T10:34:36.327152Z",
  "last_modified": "2023-02-01T10:34:36.327196Z"
}
```

When sending a POST request to a upload a video file, it is mandatory to use a form data instance. Since images are also uploaded via a POST request, the `Content-Type` header must be `multipart/form-data` as opposed to `application/json`.
A typical POST request can be sent in the following format:

```json
{
"title":"string",
"category":"id",
"age_rating":"number",
"playlist":"id"
"_actors":"[list[id]]"
"director":"id",
"desktop_thumbnail":"image",
"mobile_thumbnail":"image",
"mobile_banner":"image",
"desktop_banner":"image",
"_genres":"[list[id]]",
"_moods":"[list[id]]",
"video_link":"url",
"description":"string",
"author":"id",
"publish":"bool",
}
```

# How to Implement User Feedback Functionality

The goal of every commercial application is to serve and satisfy users. How we know our users
are satisfied with our content is when they give us feedback on how our app benefits them.
The most common, viable and effective way to get users' feedback is when they `like` our video posts or add a few of them to their list of favourites.

## POST /video/:id/likes/

Here, you are only required to send the `user_id` as follows:

```json
{
  "user_id": "1"
}
```

Yes, it is that simple! Sending a simple POST request with the above json body will do.
How we are able to determine which video was liked is in the url. The `:id` parameter is a number that represents the
`video_id`. By specifying a numerical value in the url helps identify the video a particular user likes.
If the `user_id` and the `video_id` exists, the state of the user's `like` instance changes. Either of the following
responses are gotten from our API depending on the state of the user's like instance.

```python
{
  "detail": "peter@gmail.com liked NameOfVideo"
}
# or
{
  "detail": "peter@gmail.com unliked NameOfVideo"
}
```

If, on the other hand, a video or a user with the specified ids do not exist,
an `invalid video and user id` response is sent back.

```json
{
  "details": "Invalid video_id and user_id"
}
```

A video can also be added to users' `favourites` using the same convention.

## POST /video/:id/favourites/

Here, the users can add videos to their list of `favourites`. Such videos would be seen in their profile,
although the client side can use this however way they wish. The only difference that exists between adding to `favourites` and
`liking` a particular video is that `profile_id` is used in this case instead of the `user_id`.
The video to be added to a given list is represented by the `id` parameter in the url.
The expected request can be send via a `profile_id`.

```json
{
  "profile_id": "1"
}
```

The following responses are gotten from our API depending on the state of the user's addition to their list of favourites:

```json
{
  "detail": "dan@gmail.com added NameOfVideo to list"
}
// or
{
  "detail": "dan@gmail.com removed NameOfVideo from list"
}
```
# Other Important Endpoints

## POST, GET /actor/
Expected Request Body:
```json
{
  "name":"string",
  "bio": "string",
  "image":"image"
}
```

Expected Response Body:
```json
{
    "id": 2,
    "name": "Matilda",
    "bio": "I am Matilda. And you?",
    "image": null,
    "_videos": []
}
```

The `_videos` attribute is not modifiable, meaning you cannot change its content. The `_video` attribute is a list of videos acted by the specified actor.

Note that when sending a POST request to a upload an image or video file, it is mandatory to use a form data instance. Since images are also uploaded via a POST request, the `Content-Type` header must be `multipart/form-data` as opposed to `application/json`.


## GET, PUT, PATCH, DELETE /actor/:id/
You can perform the above http method operations to an individual Actor instance given the actor `id` specified in the endpoint or url.

```json
  {
    "name":"string",
    "bio": "string",
    "image":"image"
  }
```

## POST, GET /director/
Expected Request Body:
```json
{
  "name":"string",
  "bio": "string",
  "image":"image"
}
```

Expected Response Body:
```json
{
    "id": 2,
    "name": "Mr. James",
    "bio": "I am James.",
    "image": null,
    "_videos": []
}
```

The `_videos` attribute is not modifiable, meaning you cannot change its content. The `_video` is a list of videos directed by the specified director.

Note that when sending a POST request to a upload an image or video file, it is mandatory to use a form data instance. Since images are also uploaded via a POST request, the `Content-Type` header must be `multipart/form-data` as opposed to `application/json`.


## GET, PUT, PATCH, DELETE /director/:id/
You can perform the above http method operations to an individual Director instance given the actor `id` specified in the endpoint or url.

```json
  {
    "name":"string",
    "bio": "string",
    "image":"image"
  }
```

## POST, GET /mood/
Expected Request Body:
```json
{
  "id":"number",
  "name":"string"
}
```

Expected Response Body:
```json
{
    "id": 2,
    "name": "Exciting",
    "_videos": []
}
```

The `_videos` attribute is not modifiable, meaning you cannot change its content. The `_video` is a list of videos that fall under this mood.

Note that when sending a POST request to a upload an image or video file, it is mandatory to use a form data instance. Since images are also uploaded via a POST request, the `Content-Type` header must be `multipart/form-data` as opposed to `application/json`.


## GET, PUT, PATCH, DELETE /mood/:id/
You can perform the above http method operations to an individual Mood instance given the actor `id` specified in the endpoint or url.

```json
  {
    "id":"number",
    "name":"string"
  }
```


## POST, GET /playlist/
Expected Request Body:
```json
{
  "name":"string"
}
```

Expected Response Body:
```json
{
    "id": 2,
    "name": "My Playlist",
    "_videos": []
}
```

The `_videos` attribute is not modifiable, meaning you cannot change its content. The `_video` is a list of videos that fall under this playlist.

Note that when sending a POST request to a upload an image or video file, it is mandatory to use a form data instance. Since images are also uploaded via a POST request, the `Content-Type` header must be `multipart/form-data` as opposed to `application/json`.


## GET, PUT, PATCH, DELETE /playlist/:id/
You can perform the above http method operations to an individual PlatList instance given the actor `id` specified in the endpoint or url.

```json
  {
    "id":"number",
    "name":"string"
  }
```

