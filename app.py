from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/create-file', methods=['POST'])
def create_file():
    data = request.get_json()
    file_path = data.get('path')
    content = data.get('content')
    
    if not file_path or not content:
        return jsonify({"error": "Missing 'path' or 'content'"}), 400
    
    # Write content to the file on persistent disk
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return jsonify({"message": f"File created at {file_path}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
