@echo off
:: Use the 'call' command for the venv script
call "D:\Ai Superjack\dev\ai-superjack-mcp-mongo\venv\Scripts\activate.bat"
:: Use -u (unbuffered) to prevent buffering issues with JSON-RPC
"D:\Ai Superjack\dev\ai-superjack-mcp-mongo\venv\Scripts\python.exe" -u -m src.server