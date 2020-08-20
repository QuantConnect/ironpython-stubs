import os

debug_ = [
    # | Local Binaries
    'C:\\Projects\\QuantConnect\\JoeYuZhou\\ironpython-stubs\\bin'
    # # | Quanconnect.Algorithm
    , 'E:\\Projects\\Lean\\Algorithm\\bin\\Debug'
    # | Quanconnect.Common
    , 'E:\\Projects\\Lean\\Common\\bin\\Debug'
    # # | Quanconnect.Algorithm.Framework
    , 'E:\\Projects\\Lean\\Algorithm.Framework\\bin\\Debug'
    # Quanconnect.Indicators
    , 'E:\\Projects\\Lean\\Indicators\\bin\\Debug'
]
PATHS = debug_

ASSEMBLIES = [
    'QuantConnect.Algorithm',
    # 'QuantConnect.Algorithm.Framework',
    # 'QuantConnect.Indicators',
    # 'QuantConnect.Common',
    ]

BUILTINS = [
    ]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()

REVIT_ASSEMBLIES = [
    # | Revit
    'RevitAPI',
    'RevitAPIUI',
    'RevitServices',
    'RevitNodes',
    ]

# | If running inside Revit, Process Revit Assemblies Only
try:
    __revit__
except NameError:
    pass
else:
    ASSEMBLIES = REVIT_ASSEMBLIES
