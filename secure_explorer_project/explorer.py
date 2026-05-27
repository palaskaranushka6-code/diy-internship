import os

BASE_DIR = os.path.abspath("./workspace")

def list_files():
    try:
        files = os.listdir(BASE_DIR)
        print("Files in base directory:")
        for f in files:
            print(f)
    except Exception as e:
        print(f"Error: Could not list files. {e}")

def open_file(filename):
    try:
        abs_path = os.path.abspath(os.path.join(BASE_DIR, filename))
        if not abs_path.startswith(BASE_DIR):
            raise PermissionError("Access outside base directory is not allowed.")
        
        with open(abs_path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception:
        print("Error: An unexpected issue occurred.")

# Demo
list_files()
open_file("example.txt")
