# Ecommerce Application

This is a sample ecommerce application built with FastAPI and MongoDB.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Ecommerce Application is a backend system built using FastAPI and MongoDB. It provides a set of APIs to manage products, orders, and user information for an ecommerce platform. The application allows users to list products, create orders, fetch orders, update product quantities, and more.

## Features

- List all available products in the system.
- Create a new order with timestamp, items, total amount, and user address.
- Fetch all orders from the system with pagination.
- Fetch a single order by ID.
- Update a product's available quantity.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ecommerce-application.git
2.Change into the project directory:
	``bash
	cd ecommerce-application

3.Create a virtual environment:

	``bash
	python -m venv venv

4.Activate the virtual environment:

On Windows:

	``bash
	venv\Scripts\activate
On macOS/Linux:

	``bash
	source venv/bin/activate

5.Install the required packages:

	``bash
	pip install fastapi uvicorn pymongo
6.Start the FastAPI application:

	``bash
	uvicorn main:app --reload
Usage
Open your web browser and navigate to http://localhost:8000 to access the application's APIs.

Use API testing tools like cURL, Postman, or a web browser extension to interact with the available APIs.

API Endpoints
GET /products - Get the list of available products in the system.
POST /orders - Create a new order.
GET /orders - Fetch all orders from the system with pagination.
GET /orders/{order_id} - Fetch a single order by order ID.
PUT /products/{product_id} - Update a product's available quantity.
Refer to the API documentation or code implementation for more details on request/response structures and parameters.

Technologies Used
FastAPI - Python web framework for building APIs.
MongoDB - NoSQL database for storing product and order information.
Contributing
Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please submit a pull request.

License
This project is licensed under none.