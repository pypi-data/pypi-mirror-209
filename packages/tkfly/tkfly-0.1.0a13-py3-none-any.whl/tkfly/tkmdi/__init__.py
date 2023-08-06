# From https://github.com/m0x3/Python3-Mutliple-Document-Interface/tree/master

try:
    import Pmw
except:
    pass
else:
    from tkfly.tkmdi.Widgets.MDI import MDIChild as FlyXMDIChild, MDIParent as FlyXMDIParent
    from tkfly.tkmdi.Widgets.iconPath import path as FlyXMDIIconPath
    from tkfly.tkmdi.Widgets.FlatButtons import Flatbutton as FlyXFlatButton, FlatRadiobutton as FlyXFlatRadioButton, \
        FlatRadiogroup as FlyXFlatRadioGroup
    from tkfly.tkmdi.Widgets.Toolbar import Toolbar as FlyXToolBar
    from tkfly.tkmdi.Widgets.Tree import Tree as FlyXTreeView
    from tkfly.tkmdi.Widgets.ProgressBar import ProgressBar as FlyXProgressBar