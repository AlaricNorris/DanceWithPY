@echo off&setlocal enabledelayedexpansion&title ���ǳ�ֵ
echo Please input params Like: 5,5,5,5 
set /p input_params=
C:  
cd C:\Users\AlaricNorris\Desktop
python amazonjp.py !input_params!
