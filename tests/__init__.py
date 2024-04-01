import subprocess

compile = input("Compile (Y/n) ?")
if compile.lower() == "y":
    subprocess.run(["python", "generate.py"])


print("Start test...")

testFiles = [
    "main.py"
]
errors = []

for file in testFiles:
    outcome = subprocess.run(["python", "tests/" + file], check=False, capture_output=True)
    if outcome.returncode != 0:
        errors.append(outcome)

if len(errors) == 0:
    print("All test are good!")
else:
    for error in errors:
        print(outcome.stderr.decode("utf-8"))