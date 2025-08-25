import os

def list_with_listdir(path='.'):
    """List directory contents using os.listdir()"""
    print("\n--- Using os.listdir() ---")
    try:
        entries = os.listdir(path)
        for entry in entries:
            print(entry)
    except Exception as e:
        print(f"Error: {e}")


def list_with_scandir(path='.'):
    """List directory contents with details using os.scandir()"""
    print("\n--- Using os.scandir() ---")
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    except Exception as e:
        print(f"Error: {e}")


def list_with_walk(path='.'):
    """Recursively list all subdirectories and files using os.walk()"""
    print("\n--- Using os.walk() ---")
    try:
        for root, dirs, files in os.walk(path):
            print(f"\nCurrent Directory: {root}")
            print("Subdirectories:", dirs)
            print("Files:", files)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    directory = '.'   # You can change this to any path you like
    
    list_with_listdir(directory)
    list_with_scandir(directory)
    list_with_walk(directory)
