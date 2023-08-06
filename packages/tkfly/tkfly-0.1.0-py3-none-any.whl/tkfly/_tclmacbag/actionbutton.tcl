##############
# Actionbutton
# Part of TclMacBag (C) by Peter Caffin, 2008.
# See license at http://tclmacbag.autons.net/license.phtml
##############

if {[info patchlevel] < 8.5 } { package require tile }

proc ::tclmacbag::actionbutton {win args} {
 if {[tk windowingsystem]!="aqua"} {
  ttk::label $win
  return $win 
  } ;# Mac is the only platform which needs an Action button. Everyone else understands left-click for Select, right-click for Action.
 if {[catch {array set arg $args}]} { bgerror "Unbalanced args for ::tclmacbag::actionbutton"; return }
 if {![info exists arg(-menu)]} { bgerror "::tclmacbag::actionbutton requires -menu option" ; return }
 if {![info exists arg(-style)]} { bgerror "::tclmacbag::actionbutton requires -style option" ; return }
 set cmd "$win state pressed ; update idletasks ; eval tk_popup $arg(-menu) \[::tclmacbag::actionbuttonPostPosition $win $arg(-menu)\] ; $win state !pressed ; update idletasks"
 if {[info exists arg(-background)]} { 
  ::tclmacbag::stylebutton ${win} -text {} -style $arg(-style) -background $arg(-background) -command [list eval $cmd]
  } else {
  ::tclmacbag::stylebutton ${win} -text {} -style $arg(-style) -command [list eval $cmd]
  }
 if {![info exists arg(-image)]} { 
  ::tclmacbag::actionbutton_init gears ; $win configure -image TclMacBag.action-gears 
  } else {
  ::tclmacbag::actionbutton_init $arg(-image)
  switch -- $arg(-image) { 
   "gears" { $win configure -image TclMacBag.action-gears }
   "plus" { $win configure -image TclMacBag.action-plus }
   "minus" { $win configure -image TclMacBag.action-minus }
   default { bgerror "::tclmacbag::actionbutton -image Imagename... Must be: gears, plus or minus" ; return }
   }
  }
 bind $win <ButtonPress-1> { catch { $cmd } }
 return $win
 }

proc ::tclmacbag::actionbuttonPostPosition {mb menu} {
 # This proc nicked from Ttk/Tile
 set x [winfo rootx $mb]
 set y [winfo rooty $mb]
 set dir below

 set bw [winfo width $mb]
 set bh [winfo height $mb]
 set mw [winfo reqwidth $menu]
 set mh [winfo reqheight $menu]
 set sw [expr {[winfo screenwidth  $menu] - $bw - $mw}]
 set sh [expr {[winfo screenheight $menu] - $bh - $mh}]

 switch -- $dir {
	above { if {$y >= $mh} { incr y -$mh } { incr y  $bh } }
	below { if {$y <= $sh} { incr y [expr $bh+6] } { incr y -$mh } }
	left  { if {$x >= $mw} { incr x -$mw } { incr x  $bw } }
	right { if {$x <= $sw} { incr x  $bw } { incr x -$mw } }
	flush { 
	    # post menu atop menubutton.
	    # If there's a menu entry whose label matches the
	    # menubutton -text, assume this is an optionmenu
	    # and place that entry over the menubutton.
	    set index [FindMenuEntry $menu [$mb cget -text]]
	    if {$index ne ""} { incr y -[$menu yposition $index]
	    }
	}
  }
 return [list $x $y]
 }
