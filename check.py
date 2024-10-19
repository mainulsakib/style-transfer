import os

print("Current working directory:", os.getcwd())
print("\nContents of current directory:")
for item in os.listdir():
    print(item)

print("\nContents of 'templates' directory (if it exists):")
if os.path.exists('templates'):
    for item in os.listdir('templates'):
        print(item)
else:
    print("'templates' directory not found")

print("\nContents of 'static' directory (if it exists):")
if os.path.exists('static'):
    for item in os.listdir('static'):
        print(item)
else:
    print("'static' directory not found")