
##############
# Panther Notebook (PNB)
# Part of TclMacBag by Peter Caffin, 2007.
# My first Snit widget. Guaranteed to prove cringwworthy when I look at it in 6-12 months time :-).
##############

if {[info patchlevel] < 8.5 } { package require tile }
package require snit

snit::widgetadaptor ::tclmacbag::__Mac_pnb {
 #################
 component notebook
 component labelframe
 delegate method hide to notebook
 delegate method tab to notebook
 delegate method add to notebook
 delegate method select to notebook
 delegate method Configure to notebook
 delegate method configure to notebook
 delegate method * to labelframe

 constructor {args} { 
  foreach {opt value} $args { set arg($opt) $value }
  if {[info exists arg(-style)]} { 
   # Is this a supported style?
   if {[lsearch -exact $::tclmacbag::allowedpnbstyles $arg(-style)] == -1 } { bgerror "While executing ::tclmacbag::viewbutton $win $args:\n$arg(-style) is not a supported style.\nAllowed: $::tclmacbag::allowedbuttonstyles\n\n" ; return }
   # OK, it is. 
   ::tclmacbag::stylebutton_init $arg(-style)
   set ::tclmacbag::pnbstyle($win) $arg(-style)
   } else { set ::tclmacbag::pnbstyle($win) tnb }
  ttk::frame $win
  ttk::labelframe $win.lf -labelanchor n -text {}
  ttk::notebook $win.lf.nb -style Plain.TNotebook -padding {0 15 0 0} ;# left top right bottom
#  ttk::notebook $win.lf.nb -padding {0 15 0 0} ;# left top right bottom
  installhull $win -padx 0 -pady 0 -sticky nsew
  set labelframe $win.lf
  set notebook $win.lf.nb
  grid rowconfigure $win.lf 0 -weight 1 ; grid columnconfigure $win.lf 0 -weight 1
  grid rowconfigure $win 0 -weight 1 ; grid columnconfigure $win 0 -weight 1
  grid $labelframe -sticky nsew -padx 0 -pady 0
  grid $notebook -sticky nsew -padx 0 -pady 0
  ttk::frame $win.buttons
  bind $win <Configure> "$self _updateControls"
  bind $notebook <<NotebookTabChanged>> "$self _updateControls"
  bind $notebook <Destroy> "catch { unset ::tclmacbag::pnbvalue($win) ; unset ::tclmacbag::pnbwidth($win) }"
  }

 method _updateControls {} {
  variable notebook
  # Anything changed?
  # if {[info exists ::tclmacbag::pnbwidth($win)] && $::tclmacbag::pnbwidth($win) == [winfo width $win]} { return }
  # Set up the buttons
  set last [expr [llength [$notebook tabs]]-1]
  # Add any viewbuttons not installed
  set i 0 ; set last [expr [llength [$notebook tabs]] - 1]
  foreach tab [$notebook tabs] {
   switch -- $i {
    0     { set St "$::tclmacbag::pnbstyle($win)-left" } 
    default { set St "$::tclmacbag::pnbstyle($win)-middle" }
    } 
   if {$i == $last} { set St "$::tclmacbag::pnbstyle($win)-right" } 
   if {![winfo exists $win.buttons.b$i] } { 
    grid [::tclmacbag::viewbutton $win.buttons.b$i -text [$notebook tab $tab -text] -style $St -command "$win.lf.nb select $tab" -variable ::tclmacbag::pnbvalue($win) -onwhen $i ] -row 1 -column $i
    }
   incr i
   }
#  $win.buttons.b$i configure -style viewbutton.pill-right ;# Last one in is a rotten right-button
  if {![info exists ::tclmacbag::pnbvalue($win)]} {
   set first [lindex [$notebook tabs] 0]
   set ::tclmacbag::pnbvalue($win) 0
   $win.lf.nb select $first
   } ;# Set a default value.
  # Mac
  set ypad -12
  set winmiddle [expr [winfo width $win]/2]
  set halfbuttons [expr [winfo reqwidth $win.buttons]/2]
  set w [expr $winmiddle-$halfbuttons] ;# Centered.

  place $win.buttons -in $win -y 10 -x $w -anchor nw
  set ::tclmacbag::pnbwidth($win) [winfo width $win]
  }

 #################
 }

proc ::tclmacbag::pnb {w args} { 
 switch [::tclmacbag::TileThemeNow] {
  "aqua"  { eval ::tclmacbag::__Mac_pnb $w "$args" } 
  default { regsub -all -- {\-style [a-z]*} $args "" args ; eval ttk::notebook [list $w] "$args -padding {0 5 0 0}" }
  }
 }
