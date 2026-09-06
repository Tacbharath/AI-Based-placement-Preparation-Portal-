@echo off
:: Auto-elevation to Administrator
IF '%PROCESSOR_ARCHITECTURE%' EQU 'amd64' (
   >nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
   >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

if '%errorlevel%' NEQ '0' (
    echo Requesting Administrator privileges...
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0""", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B
)

pushd "%CD%"
CD /D "%~dp0"

echo ==========================================================
echo   Resetting MySQL Root Password to: root123
echo ==========================================================
echo [1/4] Stopping MySQL80 service...
net stop MySQL80
timeout /t 2 /nobreak >nul

echo [2/4] Applying password reset script (mysql_reset.sql)...
start /b "" "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqld.exe" --defaults-file="C:\ProgramData\MySQL\MySQL Server 8.0\my.ini" --init-file="%~dp0mysql_reset.sql"
timeout /t 6 /nobreak >nul

echo [3/4] Stopping temporary mysqld instance...
taskkill /f /im mysqld.exe >nul 2>&1
timeout /t 2 /nobreak >nul

echo [4/4] Starting MySQL80 service...
net start MySQL80

echo.
echo ==========================================================
echo   SUCCESS! MySQL root password is now set to: root123
echo ==========================================================
pause
