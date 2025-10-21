@echo off
echo 🚀 Starting MCP App Starter...

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed. Please install Node.js 20+ first.
    pause
    exit /b 1
)

echo ✅ Node.js version:
node --version

echo 📦 Installing dependencies...
cd servers\billing
call npm install
call npm run build
cd ..\..\backend
call npm install
call npm run build
cd ..\frontend
call npm install

echo 🎯 Starting services...

REM Start backend
cd ..\backend
start "Backend" cmd /k "npm run dev"

REM Wait a moment
timeout /t 3 /nobreak >nul

REM Start frontend
cd ..\frontend
start "Frontend" cmd /k "npm run dev"

echo ✅ Services started!
echo 📱 Frontend: http://localhost:5173
echo 🔧 Backend: http://localhost:3001
echo.
echo Press any key to exit...
pause >nul
