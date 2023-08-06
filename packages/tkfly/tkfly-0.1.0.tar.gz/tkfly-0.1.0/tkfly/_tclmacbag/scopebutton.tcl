#Includes code (styling and graphics) from the Coccinella application.  
#    
#  Copyright (c) 2005-2008  Mats Bengtsson
#  
#  This file is BSD style licensed.
#  

# Additional modifications (c) 2009 Kevin Walzer/WordTech Communications LLC. 

# Further modifications for inclusion into TclMacBag (C) 2007-2009 Peter Caffin and other parties.

# From Apple's Human Interface Guidelines: 
# "The scope button is used in a scope bar to specify the scope of an operation, such as search... 
# Scope buttons are designed to be used in scope bars and related filter
# rows only. They are not intended to be used in the toolbar or bottom-bar areas or outside of a scope bar in the 
# window body. The recessed scope button style is used to display types or groups of objects or locations the 
# user can select to narrow the focus of a search or other operation."

# In this context, we are implementing a scopebutton as a styled ttk::radiobutton. 
# A command will fire when the ttk::radiobutton variable changes. 
# The "scope bar" should be a simple frame widget. 
# We are not implementing scope-style menubuttons because they add interface and programming complexity. 

proc ::tclmacbag::scopebutton {win args} {
 ::tclmacbag::scopebutton_init
 if {[catch {array set arg $args}]} { bgerror "Unbalanced args for ::tclmacbag::scopebutton"; return }
 if {![info exists arg(-text)]} { bgerror "::tclmacbag::scopebutton requires -text option" ; return }
 if {![info exists arg(-value)]} { bgerror "::tclmacbag::scopebutton requires -value option" ; return }
 if {![info exists arg(-variable)]} { bgerror "::tclmacbag::scopebutton requires -variable option" ; return }
 if {![info exists arg(-command)]} { bgerror "::tclmacbag::scopebutton requires -commamd option" ; return }

 ttk::radiobutton $win -style scope -text $arg(-text) -value $arg(-value) -variable $arg(-variable) -command $arg(-command)
 }