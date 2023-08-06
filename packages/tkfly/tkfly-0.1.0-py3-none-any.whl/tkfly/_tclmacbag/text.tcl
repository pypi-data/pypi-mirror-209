##############
# Text widget wrapping
# Part of TclMacBag by Peter Caffin, 2007.
##############

if {[info patchlevel] < 8.5 } { package require tile }
package require snit

snit::widgetadaptor ::tclmacbag::text {
 component tktext
 component ttkentry

 delegate method * to tktext except state
 delegate method state to ttkentry

 constructor {args} { 
  foreach {opt value} $args { set arg($opt) $value } 
  variable ttkentry
  # We're packing a text widget into a an entry widget to scavenge the entry widget's focus stuff.
  ttk::frame $win
  ttk::entry ${win}_Entry
  installhull $win -padx 0 -pady 0 -sticky nsew
  set ttkentry ${win}_Entry
  install tktext using ::text ${win}_Text -borderwidth 0 -highlightthickness 0 -exportselection 1
  bind $tktext <FocusIn> "$win state focus"
  bind $tktext <FocusOut> "$win state !focus"
  if {[::tclmacbag::TileThemeNow] == "aqua"} { set pad 4 } else { set pad 2 }
  if {[info exists arg(-rmargin)]} { set rpad [expr $pad+$arg(-rmargin)] } else { set rpad $pad }
  pack $ttkentry -in $win -padx 0 -pady 0 -expand true -fill both
  pack $tktext -in $ttkentry -padx "$pad $rpad" -pady $pad -expand true -fill both
  # Apply args
  foreach {opt value} $args {
   foreach o {-borderwidth -highlightthickness -background -bg -rmargin} { if {$opt eq $o} continue } 
   catch { $tktext configure $opt $value }
   }
  bind $tktext <Configure> [list $self updateState]
  bind $ttkentry <Key> "focus $tktext"
  bind $ttkentry <<LeftClick>> "focus $tktext"
  # Default popup menus
  bind ${win}_Text <<RightClick>> { ::tclmacbag::text_popup %W }
  }

 method updateState {} {
  variable ttkentry
  variable tktext
  if {[info exists ::tile::currentTheme]} { set ThemeNow $::tile::currentTheme } else { set ThemeNow $::ttk::currentTheme }
  switch $ThemeNow {
   "aqua"      { set bgcolor white ; set dacolor white } 
   "winnative" { set bgcolor white ; set dacolor white }
   "xpnative"  { set bgcolor white ; set dacolor white }
   "clam"      { set bgcolor white ; set dacolor "#dcdad5" }
   "step"      { set bgcolor white ; set dacolor "#a0a0a0" }
   default     { set bgcolor white ; set dacolor "#d9d9d9" }
   }
  set state [lindex [$tktext configure -state] 4]
  if {$state=="disabled" } { 
   $win configure -background "$dacolor"
   } else { 
   $win configure -background "$bgcolor"
   }
  }
 # Ends
 }

proc ::tclmacbag::text_popup {w} {
 set ::tclmacbag::text_applywidget $w
 # Reset menu state
 set c 0 ; while {$c < 10} { catch { .tclmacbag_popup_text entryconfigure $c -state normal } ; incr c }
 # Test for value length
 if {[string length [$::tclmacbag::text_applywidget get 1.0 end-1c]] < 1} { 
  .tclmacbag_popup_text entryconfigure 0 -state disabled
  .tclmacbag_popup_text entryconfigure 1 -state disabled
  .tclmacbag_popup_text entryconfigure 3 -state disabled
  .tclmacbag_popup_text entryconfigure 8 -state disabled
  .tclmacbag_popup_text entryconfigure 9 -state disabled
  }
 # Anything in the selection?
 catch { unset contents }
 if {[catch {selection get} contents]} { set contents "" }
 if {$contents==""} { 
  .tclmacbag_popup_text entryconfigure 0 -state disabled
  .tclmacbag_popup_text entryconfigure 1 -state disabled
  .tclmacbag_popup_text entryconfigure 3 -state disabled
  }
 # Anything in the clipboard buffer?
 if {1==0} {
  .tclmacbag_popup_text entryconfigure 2 -state disabled ;# Lets always assume Yes.
  }
 # Test Undo and Redo queue
 if {![$::tclmacbag::text_applywidget edit modified]} {
  .tclmacbag_popup_text entryconfigure 5 -state disabled
  .tclmacbag_popup_text entryconfigure 6 -state disabled
  }
 # Pop up the menu
 tk_popup .tclmacbag_popup_text [expr { [winfo pointerx  .] -10 }] [expr { [winfo pointery .] -10 }]
 }

if {[tk windowingsystem] != "aqua"} { set prefix "Ctrl+" } else { set prefix "Command-" }
menu .tclmacbag_popup_text -tearoff 0 -relief groove -borderwidth 1
.tclmacbag_popup_text add command -label Cut -accel ${prefix}X -command { tk_textCut $::tclmacbag::text_applywidget }
.tclmacbag_popup_text add command -label Copy -accel ${prefix}C -command { tk_textCopy $::tclmacbag::text_applywidget }
.tclmacbag_popup_text add command -label Paste -accel ${prefix}V -command { tk_textPaste $::tclmacbag::text_applywidget }
.tclmacbag_popup_text add command -label Delete -accel Del -command { $::tclmacbag::text_applywidget delete 1.0 end-1c }
.tclmacbag_popup_text add separator
.tclmacbag_popup_text add command -label Undo -accel ${prefix}Z -command { catch { $::tclmacbag::text_applywidget edit undo } }
.tclmacbag_popup_text add command -label Redo -accel ${prefix}Y -command { catch { $::tclmacbag::text_applywidget edit redo } }
.tclmacbag_popup_text add separator
.tclmacbag_popup_text add command -label "Select all" -command { $::tclmacbag::text_applywidget tag add sel 1.0 end-1c }
.tclmacbag_popup_text add command -label Clear -command { catch {$::tclmacbag::text_applywidget delete sel.first sel.last} }
unset prefix
