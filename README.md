
# To generate QuantConnect stubs. 
1. open ironstubs\default_settings.py. Edit "debug_" array (line 6-13) to point to your QC asembly location. (optional) edit "ASSEMBLIES" array (line 18-21) if you have other aseembly to include
2. open QCStubGenerator.bat. Edit line 1 to the local location where your downloaded/cloned this project. Edit line 2 to point to your iron python's "ipy.exe" location.
3. delete existing QC stubs under release\stubs\QuantConnect folder. Or you can uncomment line 3 - 8 to do this in the batch.
4. run QCStubGenerator.bat for a fresh generation

# Enhancements on original project
The purpose of this project is to generate QuantConnect stubs enable local IDE intellisense.
The original project (old generator) has following issues and are addressed in this project
1. module overwritten: when multiple assemblies share same namespace. old generator either skipped or overwrote existing stubs.  The new generator solve this with Python AST manipulation.
 
2. Old generator can't deal with non ascii characters. Error will throw. Such as in QC QuantConnect\Data\Market\Greeks.cs has method description "...the underlying asset'sprice. (∂V/∂S)..." ∂ broke the older generator

3. Generated stub is too big for PyCharm (such as QuantConnect\Data\Fundamental which is over 2 Mb). The new generator splits it with a default/adjustable 1 Mb size.

4. Old generator can't generate some methods in QC, generated wrong code "None = None" in some stubs and used reserved word, such as "from", as parameters (which is legal in C#). They caused compilation error and broke the stubs.  New generator fix them in the stubs. <b>However a better solution could be to use the same C# to Python engine as QC uses</b>, to read the assemblies instead of IronPython. The reason is as QC C# to Python code works, that engine should be able to translate the C# code better I assume.   

# Credits for other projects
Thanks for google pasta project https://github.com/google/pasta. A modify version of it is used in this project. 

# !The following are the readme from original author!

# IronPython Stubs

Stubs for common IronPython CLR assemblies.
These stubs are intended to be used by the autocomplete engine of editors like Atom, Sublime, and Visual Studio Code.

## Why IronPython Stubs?

If your are writing python code that targets IronPython, and using modules loaded through the Common Language Runtime (clr),
your editor's autocomplete engine (which runs on regular python) will not be able to access those non-native modules.
In other words, modules/or packages loaded through `clr.AddReference()` are not available on your autocomplete engine.

The workaround here is simple: Use IronPython to crawl through these libraries,
and create 'stubs' or ['mock objects'](https://en.wikipedia.org/wiki/Mock_object).
These 'stubs' can then be used by the CPython autocomplete engine.
The stubs include doc strings as well as constructor/function/method signatures.

This repository contains the code to create these stubs, and also stores an
a version of them that can be used by autocomplete-python.

![sublime-large-demo](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/sublime/sublime-demo-large.gif)

------------------------------------

# Documentation

[Wiki](https://github.com/gtalarico/ironpython-stubs/wiki)

The [wiki](https://github.com/gtalarico/ironpython-stubs/wiki) has step-by-step instructions for setting up your stubs for Atom, Sublime, Vim, Visual Studio Code.

For a list of supported Assemblies, see [this list](https://github.com/gtalarico/ironpython-stubs/tree/master/logs)

If you haven't yet, read [Note on Performance](https://github.com/gtalarico/ironpython-stubs/wiki/A-Note-on-Performance)
Large Namespaces such as `Autodesk.Revit.DB` can take a long time to be parsed and cached and might not show up right away.

------------------------------------

# Contribute - WIP

### Generate Stubs - Examples
`ipy -m ironstubs make RhinoCommon`
`ipy -m ironstubs make --all`
`ipy -m ironstubs make DSCoreNodes --folder="DSCore" --directory="C:/Program Files/Dynamo/Dynamo Core/1.3"`
### Process Stubs
WIP

### Known Issues
* Performance is not great for some of the larger classes. If you know how this can be improved please let me know.
* Some of the function/constructor signatures are missing or incorrect. This is a problem with Generator3. Please send a PR or let me know if you have a fix.
* Overloaded Methods do not show correct arguments

### Credits
This project is a fork of the repository started by Gary Edwards on [Gitlab](https://gitlab.com/reje/revit-python-stubs).
Thank you for your work Gary - and thank you [Ehsan](https://github.com/eirannejad) for pointing me to it.

It uses PyCharm's [Generator3](https://github.com/JetBrains/intellij-community/blob/master/python/helpers/generator3.py)
to create the stubs.

