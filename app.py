from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def list_files():
    directory = '.'

    files_data = []

    for item in os.listdir(directory):
        path = os.path.join(directory, item)

        file_info = {
            "name": item,
            "is_folder": os.path.isdir(path),
            "size": os.path.getsize(path),
            "last_modified": os.path.getmtime(path)
        }

        files_data.append(file_info)

    return jsonify(files_data)

if __name__ == '__main__':
    app.run(debug=True)