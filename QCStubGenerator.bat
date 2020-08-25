set project_path=C:\Projects\QuantConnect\JoeYuZhou\ironpython-stubs
set ironpython_path=E:\Projects\QuantConnect\IronPythonNew\ironpython2\bin\Debug\net45
REM cd %project_path%\release\stubs\QuantConnect
REM DEL /f /q /s *.* > NUL
REM cd ..
REM rmdir /q /s QuantConnect
REM cd ..
REM cd ..
%ironpython_path%\ipy -X:FullFrames -m ironstubs make --all --keep-partial
python -m stubsGenerator --path=%project_path%\\release\stubs\QuantConnect --partition


