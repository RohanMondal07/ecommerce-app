# Ecommerce Application Documentation

Welcome to the documentation for the Ecommerce Application. This documentation provides an overview of the application, its API endpoints, and instructions on how to use them.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Reference](#api-reference)
  - [List Products](#list-products)
  - [Create Order](#create-order)
  - [Fetch Orders](#fetch-orders)
  - [Fetch Single Order](#fetch-single-order)
  - [Update Product](#update-product)
- [Contributing](#contributing)

## Introduction

The Ecommerce Application is a backend system built using FastAPI and MongoDB. It provides a set of APIs for managing products, orders, and user information in an ecommerce platform. The application allows users to perform various operations such as listing products, creating orders, fetching orders, and updating product quantities.

## Getting Started

To get started with the Ecommerce Application, follow the steps below.

### Installation

1. Clone the repository:

   
   git clone https://github.com/RohanMondal07/ecommerce-app
   
2. Change into the project directory:
   ```bash
   cd ecommerce-app
    ```
3. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
     ```bash  
   venv\Scripts\activate
     ```  
5. Install the required packages:
    ```bash
    pip install fastapi uvicorn pymongo pydantic motor
      ```
6. Access the API at:
    ```bash
    http://127.0.0.1:8000/docs
      ```
   

### Running the Application

To run the Ecommerce Application, execute the following command:
```bash
uvicorn main:app --reload
```


The application will be accessible at http://localhost:8000.

## API Reference

The Ecommerce Application provides the following API endpoints:

### List Products

- **Endpoint:** \`/products\`
- **Method:** GET
- **Description:** Retrieves the list of available products in the system.
- **Parameters:** None
- **Response:** Returns a list of product objects, each containing the product name, price, and available quantity.

### Create Order

- **Endpoint:** \`/orders\`
- **Method:** POST
- **Description:** Creates a new order with the provided information.
- **Request Body:** The request body should contain the order details, including the timestamp, items purchased, total amount, and user address.
- **Response:** Returns the created order object.

### Fetch Orders

- **Endpoint:** \`/orders\`
- **Method:** GET
- **Description:** Fetches all orders from the system with pagination support.
- **Parameters:**
  - \`limit\` (optional): The maximum number of orders to retrieve. Defaults to 10.
  - \`offset\` (optional): The offset from where to start fetching orders. Defaults to 0.
- **Response:** Returns a list of orders based on the specified \`limit\` and \`offset\` values.

### Fetch Single Order

- **Endpoint:** \`/orders/{order_id}\`
- **Method:** GET
- **Description:** Fetches a specific order by its order ID.
- **Parameters:**
  - \`order_id\`: The unique identifier of the order.
- **Response:** Returns the order object with the specified order ID if it exists.

### Update Product

- **Endpoint:** \`/products/{product_id}\`
- **Method:** PUT
- **Description:** Updates the available quantity of a product.
- **Parameters:**
  - \`product_id\`: The unique identifier of the product to update.
- **Request Body:** The request body should contain the new quantity value for the product.
- **Response:** Returns the updated product object.

Refer to the specific API endpoints for more details on the request/response structures and parameters.
##### Scheme of Order
```
{
  "timestamp": "2023-07-09T00:08:37.563897",
  "items": [
    {
      "product_id": "string",
      "bought_quantity": 0
    }
  ],
  "user_address": {
    "city": "string",
    "country": "string",
    "zip_code": "string"
  }
}
```


## Authors

- [@RohanMondal07](https://www.github.com/RohanMondal07)


