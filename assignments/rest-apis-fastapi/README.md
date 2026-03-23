# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a simple REST API using FastAPI. You will learn how to define endpoints, validate request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️	Build Core API Endpoints

#### Description
Create a FastAPI application with endpoints to manage a small collection of orders in memory.

#### Requirements
Completed program should:

- Include a root endpoint (`GET /`) that returns a welcome message.
- Include an endpoint to list all orders (`GET /orders`).
- Include an endpoint to add a new order (`POST /orders`) using JSON input.
- Return JSON responses with clear field names and values.
- Keep the application runnable with a standard FastAPI command.


### 🛠️	Add Validation, Error Handling, and REST Naming Checks

#### Description
Improve your API by validating incoming data, enforcing REST naming conventions for routes, and returning meaningful errors for invalid requests.

#### Requirements
Completed program should:

- Define a Pydantic model for order data (for example: `order_id`, `customer_name`, `total_amount`).
- Reject invalid order payloads with appropriate validation errors.
- Handle requests for missing resources with clear error messages.
- Verify that REST endpoints follow naming conventions: use plural resource names, lowercase path segments, and nouns instead of action verbs.
- Avoid route names such as `/getOrders` or `/create-order`, and use resource-based names such as `/orders` instead.
- Return suitable HTTP status codes for success and failure cases.
- Demonstrate at least one successful and one failing request using example API calls.
