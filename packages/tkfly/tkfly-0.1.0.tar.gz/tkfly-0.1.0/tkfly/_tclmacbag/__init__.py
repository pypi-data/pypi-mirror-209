from tkfly import fly_local, fly_root, fly_load5


def _load_tclmacbag():
    from tkfly.tkimg import _load_tkimg
    _load_tkimg()
    from tkfly.snit import _load_snit
    _load_snit()
    fly_load5(fly_local()+"\\_tclmacbag")


if __name__ == '__main__':
    from tkinter import Tk

    root = Tk()

    _load_tclmacbag()

    root.eval("""
package require tclmacbag

if {[tk windowingsystem] == "x11"} { $::tclmacbag::ttkstylecmd theme use alt }

# Setup a dialog box
wm withdraw .
set w .main
::tclmacbag::toplevel $w
wm protocol $w WM_DELETE_WINDOW { exit }
wm title $w "Stylebutton styles"
wm resizable $w off off

# Init
set pic [image create photo -file [file join [file dirname [info script]] Images imageA.gif]]

# Lone buttons
set color #B2B2B2

grid [::tclmacbag::colorframe .main.menu -background $color -force yes] -row 1 -column 1 -sticky nsew
set i 1 ; set row 1
foreach style $::tclmacbag::allowedpnbstyles {
 if {$style eq "tnb"} { continue } ;# The 'tnb' style is only for tab notebook tabs.
 set S .main.menu.$style
 grid [::tclmacbag::colorframe $S -background $color -force yes] -row $row -column $i -sticky nsew
 grid [::tclmacbag::stylebutton $S.b1 -background $color -image $pic -style $style -command {puts Test} -force yes] -row 1 -column 1 -padx 5 -pady 5
 grid [label $S.l1 -text "${style}" -background $color] -row 1 -column 2 -sticky w -padx 5 -pady 5
 incr i ; if {$i == 5} { set i 1 ; incr row }
 }
grid columnconfigure .main.menu 1 -weight 1

# Group buttons (pics)

set color #A1A1A1
grid [::tclmacbag::colorframe .main.multi -background $color -force yes] -row 2 -column 1 -sticky nsew

set i 1 ; set row 1
foreach style $::tclmacbag::allowedpnbstyles {
 if {$style eq "tnb"} { continue } ;# The 'tnb' style is only for tab notebook tabs.
 set S .main.multi.$style
 grid [::tclmacbag::colorframe .main.multi.$style -background $color -force yes] -row $row -column $i -sticky nsew -padx {5 0}
 grid [::tclmacbag::colorframe .main.multi.${style}lf -background $color -force yes] -row $row -column [expr $i+1] -sticky nsew -padx 5
 grid [::tclmacbag::stylebutton $S.b1 -background $color -image $pic -style ${style}-left   -command {puts Test} -force yes -variable ::${style}-var -onwhen 1 ] -row 1 -column 1 -pady 5 
 grid [::tclmacbag::stylebutton $S.b2 -background $color -image $pic -style ${style}-middle -command {puts Test} -force yes -variable ::${style}-var -onwhen 2 ] -row 1 -column 2 -pady 5
 grid [::tclmacbag::stylebutton $S.b3 -background $color -image $pic -style ${style}-right  -command {puts Test} -force yes -variable ::${style}-var -onwhen 3 ] -row 1 -column 3 -pady 5 
 grid [label .main.multi.${style}lf.l -text "Image using '${style}-left', '${style}-middle' & '${style}-right'" -background $color] -row 1 -column 1 -sticky w -pady 5
 incr i ; if {$i == 2} { set i 1 ; incr row }
 }

grid columnconfigure .main.multi 1 -weight 1

# Group buttons (text)

set color #b1b1b1
grid [::tclmacbag::colorframe .main.tb -background $color -force yes] -row 3 -column 1 -sticky nsew

set i 1 ; set row 1
foreach style $::tclmacbag::allowedpnbstyles {
 if {$style eq "tnb"} { continue } ;# The 'tnb' style is only for tab notebook tabs.
 set S .main.tb.$style
 grid [::tclmacbag::colorframe .main.tb.$style -background $color -force yes] -row $row -column $i -sticky nsew -padx {5 0}
 grid [::tclmacbag::colorframe .main.tb.${style}lf -background $color -force yes] -row $row -column [expr $i+1] -sticky nsew -padx 5
 grid [::tclmacbag::stylebutton $S.b1 -background $color -text "Cats and Dogs" -style ${style}-left   -command {puts Test} -force yes -variable ::${style}-var -onwhen 1 ] -row 1 -column 1 -pady 5 
 grid [::tclmacbag::stylebutton $S.b2 -background $color -text "Men and Women" -style ${style}-middle -command {puts Test} -force yes -variable ::${style}-var -onwhen 2 ] -row 1 -column 2 -pady 5
 grid [::tclmacbag::stylebutton $S.b3 -background $color -text "Giraffes" -style ${style}-right  -command {puts Test} -force yes -variable ::${style}-var -onwhen 3 ] -row 1 -column 3 -pady 5
 grid [label .main.tb.${style}lf.l -text "Text in '$style' style buttons" -background $color] -row 1 -column 4 -sticky w -padx {0 5} -pady 5
 incr i ; if {$i == 2} { set i 1 ; incr row }
 }
 
grid columnconfigure .main.tb 1 -weight 1

# Finish up

grid rowconfigure      .main 10 -weight 1
grid columnconfigure   .main 1 -weight 1
grid columnconfigure   .main.menu 10 -weight 1
grid columnconfigure   .main.multi 10 -weight 1
grid columnconfigure   .main.tb 10 -weight 1

vwait end
after 20 exit

    """)

    root.mainloop()