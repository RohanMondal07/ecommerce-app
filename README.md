# Ecommerce Application

The Ecommerce Application is a backend system built with FastAPI and MongoDB. It provides a set of APIs for managing products, orders, and user information in an ecommerce platform. The application allows users to list available products, create new orders, fetch existing orders, update product quantities, and more.

## Features

- **List all available products**: Retrieve a list of products available in the system. Each product includes details such as the product name, price, and available quantity.

- **Create a new order**: Place a new order with a timestamp, items purchased, total amount, and user address. Each order can contain multiple items, with each item specifying the product ID and the quantity bought.

- **Fetch all orders with pagination**: Retrieve all orders from the system, implementing pagination using the `limit` and `offset` parameters. This allows for fetching a subset of orders at a time.

- **Fetch a single order by ID**: Get details of a specific order by providing its unique order ID.

- **Update product quantity**: Update the available quantity of a product by specifying the product ID and the new quantity.

