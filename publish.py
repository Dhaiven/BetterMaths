import subprocess

subprocess.run(["pythonn", "generate.py"])

isTest = input("Is a test version ? (Y,n)")
token = input("Put your token: ")

if isTest.lower() == "y":
    subprocess.run(["python", "-m", "twine", "upload", "testpypi", "dist/*", "-p", token])
else:
    subprocess.run(["python", "-m", "twine", "upload", "dist/*", "-p", token])