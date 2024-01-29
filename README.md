# Building-a-Task-Management-API
Authentication
Token-based Authentication
To access protected endpoints, you need to include a valid JSON Web Token (JWT) in the Authorization header of your HTTP requests. Obtain the token by:

Sign In
Endpoint: /api/signin/
Method: POST
Parameters:

username (string): User's username
password (string): User's password

Example:
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://localhost:8000/api/signin/

Response:
{
    "status": "success",
    "user_id": 1,
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}


Registration
Endpoint: /api/register/
Method: POST
Parameters:

username (string): User's username
password (string): User's password

Example:
curl -X POST -H "Content-Type: application/json" -d '{"username": "new_user", "password": "new_password"}' http://localhost:8000/api/register/

Response:
{
    "status": "success",
    "user_id": 2,
    "refresh": "new_user_refresh_token",
    "access": "new_user_access_token"
}

Using Tokens
Include the obtained access token in the Authorization header for subsequent requests:

-H "Authorization: Bearer your_access_token"

Endpoints
Task Endpoints
List Tasks
Endpoint: /api/tasks/
Method: GET
Authenticated: Yes
Parameters: None

Example:
curl -H "Authorization: Bearer your_access_token" http://localhost:8000/api/tasks/

Retrieve Task
Endpoint: /api/tasks/<task_id>/
Method: GET
Authenticated: Yes
Parameters: task_id (integer) - ID of the task

Example:
curl -H "Authorization: Bearer your_access_token" http://localhost:8000/api/tasks/1/

Create Task
Endpoint: /api/tasks/
Method: POST
Authenticated: Yes
Parameters:

title (string): Task title
description (string): Task description
due_date (string, format: YYYY-MM-DD): Due date
status (string): Task status

Example:
curl -X POST -H "Authorization: Bearer your_access_token" -H "Content-Type: application/json" -d '{"title": "New Task", "description": "Task description", "due_date": "2022-03-01", "status": "Pending"}' http://localhost:8000/api/tasks/

Update Task
Endpoint: /api/tasks/<task_id>/
Method: PATCH
Authenticated: Yes
Parameters:

title (string, optional): Task title
description (string, optional): Task description
due_date (string, format: YYYY-MM-DD, optional): Due date
status (string, optional): Task status

Example:
curl -X PATCH -H "Authorization: Bearer your_access_token" -H "Content-Type: application/json" -d '{"status": "In Progress"}' http://localhost:8000/api/tasks/1/

Delete Task
Endpoint: /api/tasks/<task_id>/
Method: DELETE
Authenticated: Yes
Parameters: task_id (integer) - ID of the task

Example:
curl -X DELETE -H "Authorization: Bearer your_access_token" http://localhost:8000/api/tasks/1/

Error Handling
HTTP Status Codes
200 OK: Request was successful
201 Created: Resource was successfully created
204 No Content: Request was successful, but there is no response body
400 Bad Request: Invalid request parameters or data
401 Unauthorized: Authentication failed or user lacks necessary permissions
404 Not Found: Requested resource does not exist
500 Internal Server Error: Server encountered an error

Error Response Format
{
    "error": {
        "code": "error_code",
        "message": "Error message"
    }
}

Example:

{
    "error": {
        "code": "invalid_request",
        "message": "Invalid request parameters"
    }
}

Task API Test Cases
to check the test cases:- --> python manage.py test tasks.tests

1. Test List Tasks
Description
Tests the endpoint for listing all tasks.

Test Steps
Make a GET request to the /api/tasks/ endpoint.
Include a valid JWT token in the Authorization header.
Expected Result
Status Code: 200 (OK)
List of tasks returned successfully.
2. Test Retrieve Task
Description
Tests the endpoint for retrieving a specific task.

Test Steps
Make a GET request to the /api/tasks/<task_id>/ endpoint.
Include a valid JWT token in the Authorization header.
Replace <task_id> with the ID of an existing task.
Expected Result
Status Code: 200 (OK)
Task details returned successfully.
3. Test Create Task
Description
Tests the endpoint for creating a new task.

Test Steps
Make a POST request to the /api/tasks/ endpoint.
Include a valid JWT token in the Authorization header.
Provide valid data (title, description, due_date, status) in the request body.
Expected Result
Status Code: 201 (Created)
New task created successfully.
4. Test Update Task
Description
Tests the endpoint for updating an existing task.

Test Steps
Make a PATCH request to the /api/tasks/<task_id>/ endpoint.
Include a valid JWT token in the Authorization header.
Replace <task_id> with the ID of an existing task.
Provide valid data (title, description, due_date, status) in the request body.
Expected Result
Status Code: 200 (OK)
Task updated successfully.
5. Test Delete Task
Description
Tests the endpoint for deleting an existing task.

Test Steps
Make a DELETE request to the /api/tasks/<task_id>/ endpoint.
Include a valid JWT token in the Authorization header.
Replace <task_id> with the ID of an existing task.
Expected Result
Status Code: 204 (No Content)
Task deleted successfully.
Error Handling
1. Test Invalid Token
Description
Tests the scenario where an invalid token is provided.

Test Steps
Include an invalid token in the Authorization header.
Make a request to any protected endpoint (e.g., /api/tasks/).
Expected Result
Status Code: 401 (Unauthorized)
Error message indicating invalid credentials.
2. Test Missing Token
Description
Tests the scenario where no token is provided.

Test Steps
Make a request to any protected endpoint without including a token.
Expected Result
Status Code: 401 (Unauthorized)
Error message indicating missing credentials.
3. Test Non-existent Task
Description
Tests the scenario where a request is made for a non-existent task.

Test Steps
Make a request to the /api/tasks/<non_existent_id>/ endpoint.
Include a valid JWT token in the Authorization header.
Expected Result
Status Code: 404 (Not Found)
Error message indicating the task does not exist.

