package require tclmacbag
if {[tk windowingsystem] == "x11"} {$::tclmacbag::ttkstylecmd theme use alt }
# Init
set pic [image create photo -file [file join [file dirname [info script]] Images imageA.gif]]
set color #B2B2B2


# Setup a dialog box
wm withdraw .
set w .main
toplevel $w -bg $color
wm protocol $w WM_DELETE_WINDOW {exit }
wm title $w "Actionbuttons and Viewbutton (Image and Text) Demo"
wm resizable $w off off

# Action buttons
if {[tk windowingsystem] eq "aqua"} { 
 grid [::tclmacbag::colorframe .main.action2 -background $color -force yes] -row 0 -column 1 -sticky w -pady 5
 set i 1 ; set row 1
 foreach style $::tclmacbag::allowedpnbstyles {
  if {$style eq "tnb"} { continue } ;# The 'tnb' style is only for tab notebook tabs.
  set S .main.action2.$style
  grid [::tclmacbag::colorframe $S -background $color -force yes] -row $row -column $i -sticky nsew
  grid [::tclmacbag::actionbutton $S.b -style $style -background $color -menu .popup -background $color] -row 1 -column 1 -padx 5 -pady 5
  grid [label $S.l1 -text "${style}" -background $color] -row 1 -column 2 -sticky w -padx 5 -pady 5
  incr i ; if {$i == 5} { set i 1 ; incr row }
  }
 grid columnconfigure .main.action2 1 -weight 1
 }

# View buttons (pics)
grid [::tclmacbag::colorframe .main.multiimg -background $color -force yes] -row 2 -column 1 -sticky w -pady 5
set i 1 ; set row 1
foreach style $::tclmacbag::allowedpnbstyles {
 if {$style eq "tnb"} { continue } ;# The 'tnb' style is only for tab notebook tabs.
 set S .main.multiimg.$style
 grid [::tclmacbag::colorframe .main.multiimg.$style -background $color -force yes] -row $row -column $i -sticky nsew -padx {5 0}
 grid [::tclmacbag::colorframe .main.multiimg.${style}lf -background $color -force yes] -row $row -column [expr $i+1] -sticky nsew -padx 5
 grid [::tclmacbag::viewbutton $S.b1 -background $color -image $pic -style ${style}-left   -command {puts Test} -force yes -variable "::${style}-ivar" -onwhen 1 ] -row 1 -column 1 -pady 5 
 grid [::tclmacbag::viewbutton $S.b2 -background $color -image $pic -style ${style}-middle -command {puts Test} -force yes -variable "::${style}-ivar" -onwhen 2 ] -row 1 -column 2 -pady 5
 grid [::tclmacbag::viewbutton $S.b3 -background $color -image $pic -style ${style}-right  -command {puts Test} -force yes -variable "::${style}-ivar" -onwhen 3 ] -row 1 -column 3 -pady 5 
 grid [label .main.multiimg.${style}lf.l -text "${style}" -background $color] -row 1 -column 1 -sticky w -pady 5
 set "::${style}-ivar" [expr int(rand()*3)+1]
 incr i 2 ; if {$i > 4} { set i 1 ; incr row }
 }
grid columnconfigure .main.multiimg 1 -weight 1

# View buttons (text)
grid [::tclmacbag::colorframe .main.multitext -background $color -force yes] -row 3 -column 1 -sticky w -pady 5
set i 1 ; set row 1
foreach style $::tclmacbag::allowedpnbstyles {
 if {$style eq "tnb"} { continue } ;# The 'tnb' style is only for tab notebook tabs.
 set S .main.multitext.$style
 grid [::tclmacbag::colorframe .main.multitext.$style -background $color -force yes] -row $row -column $i -sticky nsew -padx {5 0}
 grid [::tclmacbag::colorframe .main.multitext.${style}lf -background $color -force yes] -row $row -column [expr $i+1] -sticky nsew -padx 5
 grid [::tclmacbag::viewbutton $S.b1 -background $color -text "Cats and Dogs" -style ${style}-left   -command {puts Test} -force yes -variable ::${style}-tvar -onwhen 1 ] -row 1 -column 1 -pady 5 
 grid [::tclmacbag::viewbutton $S.b2 -background $color -text "Men and Women" -style ${style}-middle -command {puts Test} -force yes -variable ::${style}-tvar -onwhen 2 ] -row 1 -column 2 -pady 5
 grid [::tclmacbag::viewbutton $S.b3 -background $color -text "Giraffes" -style ${style}-right  -command {puts Test} -force yes -variable ::${style}-tvar -onwhen 3 ] -row 1 -column 3 -pady 5 
 grid [label .main.multitext.${style}lf.l -text "${style}" -background $color] -row 1 -column 1 -sticky w -pady 5
 set "::${style}-tvar" [expr int(rand()*3)+1]
 incr i ; if {$i == 2} { set i 1 ; incr row }
 }
grid columnconfigure .main.multitext 1 -weight 1

# Popup 
catch { destroy .popup }
menu .popup -tearoff 0 -relief groove -borderwidth 1 -activebackground #068 -activeforeground white -activeborderwidth 1 -selectcolor black
.popup add command -label "Hello world #1" -command { puts "Hello world 1." }
.popup add command -label "Hello world #2" -command { puts "Hello world 2." }
.popup add command -label "Hello world #3" -command { puts "Hello world 3." }
.popup add separator
.popup add command -label "Hello world #4" -command { puts "Hello world 4." }
.popup add command -label "Hello world #5" -command { puts "Hello world 5." }
.popup add command -label "Hello world #6" -command { puts "Hello world 6." }

vwait end
after 20 exit
