############
# TclMacBag Example
############

package require tclmacbag

wm withdraw .
tclmacbag::toplevel .tl
wm minsize  .tl 350 1
wm resizable .tl 0 0 
wm title .tl "PNB Using Styles"

if {[tk windowingsystem]=="x11"} { $::tclmacbag::ttkstylecmd theme use alt } ;# Looks nicest :)

############
# PNB (Panther Notebook)
############

set i 1 ; set row 1
foreach style $::tclmacbag::allowedpnbstyles { 
 set pnb .tl.pnb_$style
 grid [::tclmacbag::pnb .tl.pnb_$style -style $style] -row $row -column $i -sticky nsew -padx 10 -pady 10
 $pnb add [ttk::frame $pnb.a1] -text "Left"
 $pnb add [ttk::frame $pnb.a2] -text "Middle"
 $pnb add [ttk::frame $pnb.a3] -text "Right"
 grid [ttk::label $pnb.a1.l -text "Left tab using the '$style' style."] -padx 20 -sticky w -pady {5 0}
 grid [ttk::label $pnb.a2.l -text "Middle tab using the '$style' style."] -padx 20 -sticky w -pady {5 0}
 grid [ttk::label $pnb.a3.l -text "Right tab using the '$style' style."] -padx 20 -sticky w -pady {5 0}
 if {$style == "tnb"} { 
  grid [ttk::label $pnb.a1.l2 -text "(The standard and default PNB style.)"] -padx 20 -pady 10 -sticky w
  grid [ttk::label $pnb.a2.l2 -text "(The standard and default PNB style.)"] -padx 20 -pady 10 -sticky w
  grid [ttk::label $pnb.a3.l2 -text "(The standard and default PNB style.)"] -padx 20 -pady 10 -sticky w
  } else {
  grid [ttk::label $pnb.a1.l2 -text "(Not particularly standard.)"] -padx 20 -pady 10 -sticky w
  grid [ttk::label $pnb.a2.l2 -text "(Not particularly standard.)"] -padx 20 -pady 10 -sticky w
  grid [ttk::label $pnb.a3.l2 -text "(Not particularly standard.)"] -padx 20 -pady 10 -sticky w
  }
  
 grid columnconfigure $pnb.a1 1 -weight 0
 grid columnconfigure $pnb.a2 1 -weight 0
 grid columnconfigure $pnb.a3 1 -weight 0

 incr i ; if {$i == 3} { set i 1 ; incr row }
 }
 
grid columnconfigure .tl 1 -weight 1

#############
# The End.
#############

vwait forever
exit
