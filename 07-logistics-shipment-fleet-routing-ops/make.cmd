@echo off
rem Runs make.ps1 without changing the machine execution policy (bypass applies to this call only).
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0make.ps1" %*
exit /b %ERRORLEVEL%
