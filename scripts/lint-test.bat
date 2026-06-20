@echo off
echo ========================================
echo  Python Project Automation Script
echo ========================================
echo.

echo [1/3] Running ruff check...
ruff check .
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Ruff check failed!
    exit /b 1
)
echo [OK] Ruff check passed.
echo.

echo [2/3] Running ruff format...
ruff format .
echo [OK] Ruff format completed.
echo.

echo [3/3] Running pytest...
python -m pytest tests/ -v
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Pytest failed!
    exit /b 1
)
echo.
echo ========================================
echo  All checks passed!
echo ========================================
