##############
# Disclosure Dialog Button - ddialog
# Part of TclMacBag by Peter Caffin, 2008.
##############

if {[info patchlevel] < 8.5 } { package require tile }
package require snit

snit::widgetadaptor ::tclmacbag::ddialog {
 ##########################

 component ttkbutton

 delegate method * to ttkbutton

 constructor {args} {
  ::tclmacbag::ddialog_init
  if {[catch {array set arg $args}]} { bgerror "Unbalanced args for ::tclmadbag::frame" ; return }
  variable ttkbutton
  ttk::frame $win
  installhull $win -padx 0 -pady 0
  if {![info exists arg(-image)]} { 
   set ::tclmacbag::ddialogclosedimage($win) TclMacBag.ddialogimage(closed) 
   set ::tclmacbag::ddialogopenimage($win) TclMacBag.ddialogimage(open) 
   } else {
   set ::tclmacbag::ddialogclosedimage($win) $arg(-image)
   set ::tclmacbag::ddialogopenimage($win) $arg(-image)
   }
  ::tclmacbag::stylebutton ${win}.button -style gel-small -image $::tclmacbag::ddialogclosedimage($win) -command "::tclmacbag::ddialog::Toggle $win"
  set ttkbutton ${win}.button
  if {[info exists arg(-command)]} { 
   ${win}.button config -command "
    ::tclmacbag::ddialog::ToggleTo $win -state open
    $arg(-command)
    ::tclmacbag::ddialog::ToggleTo $win -state closed
    "
   }
  # tk_messageBox -message $args
  grid $win.button -row 1 -column 1 -padx 0 -pady 0
  grid columnconfigure $win 1 -weight 1
  grid rowconfigure $win 1 -weight 1
  bind $win <Destroy> " catch { unset ::tclmacbag::ddialogtoggle($win) ::tclmacbag::ddialogclosedimage($win) ::tclmacbag::ddialogopenimage } "
  }

 proc Toggle {w} {
  if {[info exists ::tclmacbag::ddialogtoggle($w)]} {
   # Hide the toolbar
   catch {unset ::tclmacbag::ddialogtoggle($w) }
   ${w}.button configure -image $::tclmacbag::ddialogclosedimage($w)
   } else {
   # Show the toolbar
   set ::tclmacbag::ddialogtoggle($w) 1
   ${w}.button configure -image $::tclmacbag::ddialogopenimage($w)
   }
  }

proc ToggleTo {w args} {
 if {[catch {array set arg $args}]} { bgerror "Unbalanced args for ::tclmacbag::ddialog::ToggleTo"; return }
 if {![info exists arg(-state)]} { bgerror "::tclmacbag::ddialog::ToggleTo requires -state option" ; return }
 if {$arg(-state)=="open"} {
  # Switch on
  catch { unset ::tclmacbag::ddialogtoggle($w) }
  ::tclmacbag::ddialog::Toggle $w
  } else {
  # Switch off
  set ::tclmacbag::ddialogtoggle($w) 1
  ::tclmacbag::ddialog::Toggle $w
  }
 }

 ##########################
 } ;# End of snit widget
