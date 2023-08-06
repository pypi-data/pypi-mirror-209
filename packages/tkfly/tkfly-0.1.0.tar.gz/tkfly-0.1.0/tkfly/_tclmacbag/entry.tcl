##############
# Part of TclMacBag (C) by Peter Caffin, 2007-.
# Tile's Entry widget with handy right-click popup menu.
# License at http://tclmacbag.autons.net/
##############

if {[info patchlevel] < 8.5 } { package require tile }

proc ::tclmacbag::entry {wn args} {
 eval ttk::entry $wn $args -exportselection 1
 # Default popup menus
 bind $wn <<RightClick>> { ::tclmacbag::entry_popup %W }
 # Finish
 return $wn
 }

proc ::tclmacbag::entry_popup {w} {
 set ::tclmacbag::entry_applywidget $w
 # Reset menu state
 set c 0 ; while {$c < 7} { catch { .tclmacbag_popup_entry entryconfigure $c -state normal } ; incr c }
 # Test for value length
 set key [lindex [$::tclmacbag::entry_applywidget configure -textvariable] 4] ; upvar $key value
 if {[string length $value] < 1} {
  .tclmacbag_popup_entry entryconfigure 0 -state disabled
  .tclmacbag_popup_entry entryconfigure 1 -state disabled
  .tclmacbag_popup_entry entryconfigure 5 -state disabled
  .tclmacbag_popup_entry entryconfigure 6 -state disabled
  }
 # Anything in the selection?
 if {![$::tclmacbag::entry_applywidget selection present]} { 
  .tclmacbag_popup_entry entryconfigure 0 -state disabled
  .tclmacbag_popup_entry entryconfigure 1 -state disabled
  .tclmacbag_popup_entry entryconfigure 3 -state disabled
  }
 # Anything in the clipboard buffer?
 if {1==0} {
  .tclmacbag_popup_text entryconfigure 2 -state disabled ;# Lets always assume Yes.
  }
 # Pop up the menu
 tk_popup .tclmacbag_popup_entry [expr { [winfo pointerx  .] -10 }] [expr { [winfo pointery .] -10 }]
 }

proc ::tclmacbag::entry_delete {} {
 catch { set [lindex [$::tclmacbag::entry_applywidget configure -textvariable] 4] "" }
 }

if {[tk windowingsystem] != "aqua"} { set ctrlprefix "Ctrl+" ; set altprefix "Alt+" } else { set ctrlprefix "Command-" ; set altprefix "Apple-" }
menu .tclmacbag_popup_entry -tearoff 0 -relief groove -borderwidth 1
.tclmacbag_popup_entry add command -label Cut -accel ${ctrlprefix}X -command { ttk::entry::Cut $::tclmacbag::entry_applywidget }
.tclmacbag_popup_entry add command -label Copy -accel ${ctrlprefix}C -command { ttk::entry::Copy $::tclmacbag::entry_applywidget }
.tclmacbag_popup_entry add command -label Paste -accel ${ctrlprefix}V -command { ttk::entry::Paste $::tclmacbag::entry_applywidget }
.tclmacbag_popup_entry add command -label Delete -accel Del -command { ::tclmacbag::entry_delete }
.tclmacbag_popup_entry add separator
.tclmacbag_popup_entry add command -label "Select all" -accel ${altprefix}A -command { $::tclmacbag::entry_applywidget selection range 0 end }
.tclmacbag_popup_entry add command -label Clear -command { ttk::entry::Clear $::tclmacbag::entry_applywidget }
unset ctrlprefix altprefix

