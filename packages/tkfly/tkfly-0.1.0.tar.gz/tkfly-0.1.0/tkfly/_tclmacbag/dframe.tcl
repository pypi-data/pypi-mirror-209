##############
# Disclosure Frame - dframe
# Part of TclMacBag by Peter Caffin, 2007.
##############

if {[info patchlevel] < 8.5 } { package require tile }
package require snit

snit::widgetadaptor ::tclmacbag::dframe {
 ##########################

 component ttklabel
 component ttkimage
 delegate method * to ttklabel

 constructor {args} {
  ::tclmacbag::dframe_init
  if {[catch {array set arg $args}]} { bgerror "Unbalanced args for ::tclmadbag::frame"; return }
  if {[info exists arg(-autoresize)] && $arg(-autoresize)=="on"} { set ::tclmacbag::dframeautoresize($win) 1 }
  variable ttklabel
  ttk::frame $win
  installhull $win -padx 0 -pady 0 -sticky nsew
  ttk::frame ${win}.frame
  ttk::frame ${win}.int
  set f ${win}.int
  if {![info exists arg(-label)]} { set arg(-label) "!! No label found" } 
  ttk::label $f.label -text " $arg(-label)" -takefocus 1 -border 1 -compound left -image TclMacBag.dframeimage(closed)

  set ttklabel ${win}.label
  set ttkimage ${win}.label
  if {$arg(-label) != "!! No label found"} { 
   grid $f.label -row 1 -column 1 -sticky w -padx 0 -pady 0
   }
  grid $f       -row 1 -column 1 -sticky w -padx 0 -pady 0
  grid columnconfigure $win 1 -weight 1
  grid columnconfigure $win.frame 1 -weight 1
  grid rowconfigure $win 2 -weight 1
  grid rowconfigure $win.frame 1 -weight 1
  bind $f.label <Button-1> "::tclmacbag::dframe::Toggle $win"
  bind $win <Destroy> "catch { unset ::tclmacbag::dframetoggle($win) }"
#  bind $f.label <<TraverseIn>> "$f.label configure -relief solid"
#  bind $f.label <<TraverseOut>> "$f.label configure -relief flat"
  bind $f.label <Up> "::tclmacbag::dframe::ToggleTo $win -state closed"
  bind $f.label <Left> "::tclmacbag::dframe::ToggleTo $win -state closed"
  bind $f.label <Down> "::tclmacbag::dframe::ToggleTo $win -state open"
  bind $f.label <Right> "::tclmacbag::dframe::ToggleTo $win -state open"
  bind $f.label <Key-space> "::tclmacbag::dframe::Toggle $win"
  if {[info exists arg(-font)]} { $f.label configure -font $arg(-font) }
  }

proc Toggle {w} {
 if {[info exists ::tclmacbag::dframetoggle($w)]} {
  # Hide the toolbar
  unset ::tclmacbag::dframetoggle($w)
  set ::tclmacbag::dframeisdisplayed($w) 0
  ${w}.int.label configure -image TclMacBag.dframeimage(closed)
  grid forget ${w}.frame
  } else {
  # Show the toolbar
  set ::tclmacbag::dframetoggle($w) 1
  set ::tclmacbag::dframeisdisplayed($w) 1
  eval grid ${w}.frame -row 2 -column 1 -rowspan 2 -sticky nsew -padx 0 -pady 0
  ${w}.int.label configure -image TclMacBag.dframeimage(open)
  }
 if {[info exists ::tclmacbag::dframeautoresize($w)]} { ::tclmacbag::dbutton::Resize $w }
 if {[winfo exists [winfo parent [winfo parent $w]]]} { after 80 "event generate [winfo parent [winfo parent $w]] <Configure> -when now" ; update }
 }

proc ToggleTo {w args} {
 if {[catch {array set arg $args}]} { bgerror "Unbalanced args for ::tclmacbag::dframe::ToggleTo"; return }
 if {![info exists arg(-state)]} { bgerror "::tclmacbag::dframe::ToggleTo requires -state option" ; return }
 if {$arg(-state)=="open"} {
  # Switch on
  catch { unset ::tclmacbag::dframetoggle($w) }
  ::tclmacbag::dframe::Toggle $w
  } else {
  # Switch off
  set ::tclmacbag::dframetoggle($w) 1
  ::tclmacbag::dframe::Toggle $w
  }
 if {[winfo exists [winfo parent [winfo parent $w]]]} { after 80 "event generate [winfo parent [winfo parent $w]] <Configure> -when now" ; update }
 }

proc Resize {w} {
 update idletasks
 # Has the height changed? If not, lets bail out.
 if {[winfo reqheight [winfo toplevel $w]] == [winfo height [winfo toplevel $w]]} { return }
 # Resize
 wm geometry [winfo toplevel $w] [winfo reqwidth [winfo toplevel $w]]x[winfo reqheight [winfo toplevel $w]]
 if {[winfo exists [winfo parent [winfo parent $w]]]} { after 50 "event generate [winfo parent [winfo parent $w]] <Configure> -when now" }
 }

 ##########################
 } ;# End of snit widget



