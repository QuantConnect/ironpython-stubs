project_path=C:\Projects\QuantConnect\JoeYuZhou\ironpython-stubs
ironpython_path=E:\Projects\QuantConnect\IronPythonNew\ironpython2\bin\Debug\net45
cd %project_path%\release\stubs\QuantConnect
DEL /f /q /s *.* > NUL
cd ..
rmdir /q /s QuantConnect
cd ..
%ironpython_path%\ipy -X:FullFrames -m ironstubs make all
python -m stubsGenerator --path=%project_path%\\release\stubs\QuantConnect --partition --keep-partial

