if {[info exists ::bagsf::version]} { return }

namespace eval ::bagsf {
#############################################################################################

set sfversion 0.9.1
set (debug,place) 0

proc scrolledframe {w args} {
 variable {}
 # Allocate vars
 foreach {opt value} $args { set arg($opt) $value }
 # create a scrolled frame
 if {[::tclmacbag::TileThemeNow] == "aqua"} { frame $w -background systemModelessDialogBackgroundActive } else { ttk::frame $w } 
 # trap the reference
 rename $w ::bagsf::_$w
 # redirect to dispatch
 interp alias {} $w {} ::bagsf::dispatch $w
 # create scrollable internal frame
 if {[::tclmacbag::TileThemeNow] == "aqua"} { frame $w.scrolled -background systemModelessDialogBackgroundActive } else { ttk::frame $w.scrolled }
 # init internal data
 set ::bagsf::vheight($w) 0
 set ::bagsf::vwidth($w) 0
 set ::bagsf::vtop($w) 0
 set ::bagsf::vleft($w) 0
 set ::bagsf::xscroll($w) ""
 set ::bagsf::yscroll($w) ""
 set ::bagsf::width($w) 0
 set ::bagsf::height($w)   0
 set ::bagsf::fillx($w) 0
 set ::bagsf::filly($w) 0
 # configure
 if {$args != ""} { uplevel 1 ::bagsf::config $w $args }
 # bind <Configure>
 bind $w <Configure> "[namespace code [list resize $w]]"
 bind $w.scrolled <Configure> "[namespace code [list resize $w]]"
 bind $w <MouseWheel> {%W yview scroll [expr {- (%D)}] units}
 # return widget ref
 # after 100 ::bagsf::resize $w force
 # place it
 place $w.scrolled -in $w -x 0 -y 0
 update 
 return $w
 }

proc dispatch {w cmd args} {
 variable {}
 switch -glob -- $cmd {
  con*    { uplevel 1 [linsert $args 0 ::bagsf::config $w] }
  xvi*    { uplevel 1 [linsert $args 0 ::bagsf::xview  $w] }
  yvi*    { uplevel 1 [linsert $args 0 ::bagsf::yview  $w] }
  default { uplevel 1 [linsert $args 0 ::bagsf::_$w    $cmd] }
  }
 }

proc config {w args} {
 variable {}
 set options {}
 set flag 0
 foreach {key value} $args {
  switch -glob -- $key {
   -fill {
          # new fill option: what should the scrolled object do if it is smaller than the viewing window?
          if {$value == "none"}       { set ::bagsf::fillx($w) 0 ; set ::bagsf::filly($w) 0
           } elseif {$value == "x"}    { set ::bagsf::fillx($w) 1 ; Set ::bagsf::filly($w) 0
           } elseif {$value == "y"}    { set ::bagsf::fillx($w) 0 ; set ::bagsf::filly($w) 1
           } elseif {$value == "both"} { set ::bagsf::fillx($w) 1 ; set ::bagsf::filly($w) 1
           } else { error "invalid value: should be \"$w configure -fill value\", where \"value\" is \"x\", \"y\", \"none\", or \"both\"" }
           resize $w force
           set flag 1
           }
  -xsc*   { set ::bagsf::xscroll($w) $value ; set flag 1 ;# new xscroll option }
  -ysc*   { set ::bagsf::yscroll($w) $value ; set flag 1 ;# new yscroll option }
  default { lappend options $key $value }
  }
 }
 # check if needed
 if {!$flag || $options != ""} { uplevel 1 [linsert $options 0 ::bagsf::_$w config] }
 }

proc resize {w args} {
 variable {}
 set _vheight     $::bagsf::vheight($w)
 set _vwidth      $::bagsf::vwidth($w)
 # compute new height & width
 set ::bagsf::vheight($w) [winfo reqheight $w.scrolled]
 set ::bagsf::vwidth($w)  [winfo reqwidth  $w.scrolled]
 # The size may have changed, e.g. by manual resizing of the window
 set _height     $::bagsf::height($w)
 set _width      $::bagsf::width($w)
 set ::bagsf::height($w) [winfo height $w] ;# gives the actual height of the viewing window
 set ::bagsf::width($w)  [winfo width  $w] ;# gives the actual width of the viewing window

 if {$args == "force" || $::bagsf::vheight($w) != $_vheight || $::bagsf::height($w) != $_height} { yview $w scroll 0 unit ; yset $w } ;# resize the vertical scroll bar
 if {$args == "force" || $::bagsf::vwidth($w) != $_vwidth || $::bagsf::width($w) != $_width} { xview $w scroll 0 unit ; xset $w } ;# resize the horizontal scroll bar
 } 

proc xset {w} {
 # resize the visible part
 variable {}
 # call the xscroll command
 set cmd $::bagsf::xscroll($w)
 if {$cmd != ""} { catch { eval $cmd [xview $w] } }
 }

proc yset {w} {
 # resize the visible part
 variable {}
 # call the yscroll command
 set cmd $::bagsf::yscroll($w)
 if {$cmd != ""} { catch { eval $cmd [yview $w] } }
 }

proc xview {w {cmd ""} args} {
 # called on horizontal scrolling
 # parm1: widget path
 # parm2: optional moveto or scroll
 # parm3: fraction if parm2 == moveto, count unit if parm2 == scroll
 # return: scrolling info if parm2 is empty
 variable {}
 # check args
 set len [llength $args]
 switch -glob -- $cmd {
  ""      {set args {}}
  mov*    { if {$len != 1} { error "wrong # args: should be \"$w xview moveto fraction\"" } }
  scr*    { if {$len != 2} { error "wrong # args: should be \"$w xview scroll count unit\"" } }
  default { error "unknown operation \"$cmd\": should be empty, moveto or scroll" }
  }
 # save old values:
 set _vleft $::bagsf::vleft($w)
 set _vwidth $::bagsf::vwidth($w)
 set _width  $::bagsf::width($w)
 # compute new vleft
 set count ""
 switch $len {
  0 {
     # return fractions
     if {$_vwidth == 0} { return {0 1} }
     set first [expr {double($_vleft) / $_vwidth}]
     set last [expr {double($_vleft + $_width) / $_vwidth}]
     if {$last > 1.0} { return {0 1} }
     return [list [format %g $first] [format %g $last]]
     }
  1 { set vleft [expr {int(double($args) * $_vwidth)}] }
  2 {
    # relative movement
    foreach {count unit} $args break
    if {[string match p* $unit]} { set count [expr {$count * 9}] }
    set vleft [expr {$_vleft + $count * 0.1 * $_width}]
    }
   }
 if {$vleft + $_width > $_vwidth} { set vleft [expr {$_vwidth - $_width}] }
 if {$vleft < 0} { set vleft 0 }
 if {$vleft != $_vleft || $count == 0} {
  set ::bagsf::vleft($w) $vleft
  xset $w
  if {$::bagsf::fillx($w) && ($_vwidth < $_width || $::bagsf::xscroll($w) == "") } {
   # "scrolled object" is not scrolled, because it is too small or because no scrollbar was requested
   # fillx means that, in these cases, we must tell the object what its width should be
   place $w.scrolled -in $w -x [expr {-$vleft}] -width $_width ; update idletasks
   } else {
   place $w.scrolled -in $w -x [expr {-$vleft}] -width {} ; update idletasks
   }
  }
 }

proc yview {w {cmd ""} args} {
 # called on vertical scrolling
 # parm1: widget path
 # parm2: optional moveto or scroll
 # parm3: fraction if parm2 == moveto, count unit if parm2 == scroll
 # return: scrolling info if parm2 is empty
 variable {}
 # check args
 set len [llength $args]
 switch -glob -- $cmd {
  ""      {set args {}}
  mov*    { if {$len != 1} { error "wrong # args: should be \"$w yview moveto fraction\"" } }
  scr*    { if {$len != 2} { error "wrong # args: should be \"$w yview scroll count unit\"" } }
  default { error "unknown operation \"$cmd\": should be empty, moveto or scroll" }
  }
 # save old values
 set _vtop $::bagsf::vtop($w)
 set _vheight $::bagsf::vheight($w)
 set _height $::bagsf::height($w)
 # compute new vtop
 set count ""
 switch $len {
  0      {
     # return fractions
     if {$_vheight == 0} { return {0 1} }
     set first [expr {double($_vtop) / $_vheight}]
     set last [expr {double($_vtop + $_height) / $_vheight}]
     if {$last > 1.0} { return {0 1} }
     return [list [format %g $first] [format %g $last]]
          }
  1      { set vtop [expr {int(double($args) * $_vheight)}] }
  2      {
     # relative movement
     foreach {count unit} $args break
     if {[string match p* $unit]} { set count [expr {$count * 9}] }
     set vtop [expr {$_vtop + $count * 0.1 * $_height}]
          }
 }
 if {$vtop + $_height > $_vheight} { set vtop [expr {$_vheight - $_height}] }
 if {$vtop < 0} { set vtop 0 }
 if {$vtop != $_vtop || $count == 0} { 
  set ::bagsf::vtop($w) $vtop
  yset $w
  if {$_vheight < $_height } {
   # "scrolled object" is not scrolled, because it is too small or because no scrollbar was requested
   # filly means that, in these cases, we must tell the object what its height should be
   # place $w.scrolled -in $w -y [expr {-$vtop}] -height $_height ; update idletasks
   } else {
   place $w.scrolled -in $w -y [expr {-$vtop}] -height {} ; update idletasks
   }
  }
 }

#############################################################################################
}

# Linux has no MouseWheel
bind all <Button-4> { event generate [focus -displayof %W] <MouseWheel> -delta  120 }
bind all <Button-5> { event generate [focus -displayof %W] <MouseWheel> -delta -120 }

# Finish up
interp alias {} tclmacbag::scrolledframe {} ::bagsf::scrolledframe
