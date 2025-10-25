@echo off
echo The icon cache will be rebuilt. This may take a few moments.
echo Please save all your work before continuing.
pause
taskkill /f /im explorer.exe
cd /d %userprofile%\AppData\Local
attrib -h IconCache.db
del IconCache.db /a
start explorer.exe
echo The icon cache has been rebuilt successfully.
pause
