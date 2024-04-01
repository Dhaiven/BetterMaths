import subprocess

compile = input("Compile (Y/n) ?")
if compile.lower() == "y":
    subprocess.run(["python", "generate.py"])


print("Start test...")

testFiles = [
    "main.py"
]

for file in testFiles:
    subprocess.run(["python", "tests/" + file])

print("All test are good!")