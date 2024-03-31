@echo off

python -version >nul 2>&1 && (
  start python -m build
) || (
  start python3.12 -m build
  pause
)

if %errorlevel%==0 echo line=%*

echo "y" | [pip uninstall BetterMaths]
start pip install dist\bettermaths-0.0.2-py3-none-any.whl
pause