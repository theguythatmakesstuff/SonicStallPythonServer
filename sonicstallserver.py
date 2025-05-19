from flask import Flask, request, jsonify
import logging
import sys

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO,  # Set the logging level
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)])  # Log to console

# Define the server address and port
SERVER_HOST = '127.0.0.1'  # Change this to '0.0.0.0'
SERVER_PORT = 8013

# --- Routes for Sonic Stall App ---

@app.route('/', methods=['GET'])
def home():
    """
    Handles the root endpoint.  Useful for a basic "are you alive" check.
    Returns:
        A JSON response indicating the server is running.
    """
    logging.info("Root endpoint '/' hit")
    return jsonify(message="Sonic Stall Server is running!"), 200

@app.route('/api/order', methods=['POST'])
def create_order():
    """
    Handles the creation of a new order.
    Expected Input:
        JSON data containing order details (e.g., items, customer info).
    Returns:
        A JSON response indicating the order status.
    """
    try:
        order_data = request.get_json()
        if not order_data:
            logging.error("No data received in /api/order POST request")
            return jsonify(error="No data received"), 400

        # Process the order (replace with actual order processing logic)
        logging.info(f"Received order: {order_data}")
        # Placeholder for order processing (e.g., save to database, send to kitchen)
        order_id = "ORDER-12345"  # Replace with actual order ID from your system

        response_data = {
            "message": "Order created successfully",
            "order_id": order_id,
            "status": "pending" # Or "confirmed", "processing", etc.
        }
        return jsonify(response_data), 201  # 201 Created

    except Exception as e:
        logging.exception("Error processing order")
        return jsonify(error=f"Error creating order: {str(e)}"), 500

@app.route('/api/order/<order_id>', methods=['GET'])
def get_order_status(order_id):
    """
    Retrieves the status of a specific order.
    Args:
        order_id: The ID of the order to retrieve.
    Returns:
        A JSON response containing the order status, or an error if not found.
    """
    try:
        logging.info(f"Getting status for order: {order_id}")
        # Placeholder for order status retrieval (e.g., from database)
        if order_id == "ORDER-12345":  # Replace with actual order ID check
            order_status = {
                "order_id": order_id,
                "status": "processing",
                "items": ["Sonic Burger", "Tater Tots", "Large Coke"] #Add dummy data
            }
            return jsonify(order_status), 200
        else:
            return jsonify(error="Order not found"), 404
    except Exception as e:
        logging.exception("Error getting order status")
        return jsonify(error=f"Error getting order status: {str(e)}"), 500

@app.route('/api/menu', methods=['GET'])
def get_menu():
    """
    Retrieves the current menu.
    Returns:
        A JSON response containing the menu.
    """
    try:
        logging.info("Getting menu")
        # Placeholder for menu data (e.g., from database or config file)
        menu_data = {
            "items": [
                {"id": "burger", "name": "Sonic Burger", "price": 4.99, "category": "Burgers"},
                {"id": "tots", "name": "Tater Tots", "price": 2.49, "category": "Sides"},
                {"id": "coke", "name": "Large Coke", "price": 1.99, "category": "Drinks"},
                {"id": "shake", "name": "Oreo Shake", "price": 3.99, "category": "Desserts"},
                {"id": "hotdog", "name": "Corn Dog", "price": 2.99, "category": "Entrees"}
            ],
            "categories": ["Burgers", "Sides", "Drinks", "Desserts", "Entrees"]
        }
        return jsonify(menu_data), 200
    except Exception as e:
        logging.exception("Error getting menu")
        return jsonify(error=f"Error getting menu: {str(e)}"), 500

# --- Main App Execution ---

if __name__ == "__main__":
    """
    Main entry point for the application.
    Starts the Flask development server.
    """
    logging.info(f"Starting server on {SERVER_HOST}:{SERVER_PORT}")
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True) # Set debug=False for production
