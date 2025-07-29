from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample To-Do List
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1 description"},
    {"id": 2, "name": "Item 2", "description": "This is item 2 description"}
]

@app.route('/')
def home():
    return "Welcome to To-Do app"

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])  # Fixed syntax error
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404  # Added status code
    return jsonify(item)

# Add a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"message": "Missing name in request"}), 400  # Added return & status code

    new_item = {
        "id": len(items) + 1,
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }
    items.append(new_item)
    return jsonify(new_item), 201  # Status code for created resource

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404  # Added status code

    # Update item fields
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404  # Added status code
    
    # Reassign items after removing the item
    items = [i for i in items if i['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200  # Success status code

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample To-Do List
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1 description"},
    {"id": 2, "name": "Item 2", "description": "This is item 2 description"}
]

@app.route('/')
def home():
    return "Welcome to To-Do app"

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])  # Fixed syntax error
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404  # Added status code
    return jsonify(item)

# Add a new item -API
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"message": "Missing name in request"}), 400  # Added return & status code

    new_item = {
        "id": len(items) + 1,
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }
    items.append(new_item)
    return jsonify(new_item), 201  # Status code for created resource

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404  # Added status code

    # Update item fields
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404  # Added status code
    
    # Reassign items after removing the item
    items = [i for i in items if i['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200  # Success status code

if __name__ == '__main__':
    app.run(debug=True)
