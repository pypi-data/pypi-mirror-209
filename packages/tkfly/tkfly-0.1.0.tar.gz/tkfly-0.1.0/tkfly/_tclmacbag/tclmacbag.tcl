####################################################################
# TclMacBag
# Copyright (C) 2007-2009, Peter Caffin and other parties.
# For more info: http://tclmacbag.autons.net/
####################################################################

# Package requires - Img (only require if no binary libs are already loaded)
set ::tclmacbag_loaded {} ; foreach i [info loaded] { lappend ::tclmacbag_loaded [lindex $i 1] }
if {[lsearch -exact $::tclmacbag_loaded Tkimggif ] == -1 || [lsearch -exact $::tclmacbag_loaded Tkimgpng ] == -1 } { 
 package require img::base
 package require img::gif
 package require img::png
 }
unset ::tclmacbag_loaded

# Package requires - Tile/Ttk etc
if {[info patchlevel] < 8.5 } { package require tile } else { package require Ttk }

package provide tclmacbag 0.20

namespace eval tclmacbag {
#############################################################################################
set ::tclmacbag::version 0.20
set ::tclmacbag::basedir [file dirname [info script]]

############
# Combo/Drop-Box
############

proc combo {wn args} {
 # Check for bad/incomplete options.
 if {[winfo exists $wn]} { bgerror "While executing ::tclmacbag::combo $wn $args:\nWidget already exists." }
 set req 0 ; foreach {opt value} $args {
  switch -- $opt {
   "-textvariable" { incr req }
   "-values" {}
   "-postcommand" {}
   "-state" {}
   "-background" {}
   default { bgerror "While executing ::tclmacbag::combo $wn $args:\nUnknown option $opt $value\nMust be -textvariable, -values, -bind or -postcommand.\n" }
   }
  }
 if {![info exists req] || $req < 1} { bgerror "While executing ::tclmacbag::combo $wn $args\nRequires -textvariable declared.\n" }
 # Start
 foreach {opt value} $args { set arg($opt) $value }
 if {[tk windowingsystem]=="aqua" || ([info exists arg(-force)] && $arg(-force)=="yes") } {
  menubutton $wn -menu $wn.menu -direction flush ; menu $wn.menu
  if {[tk windowingsystem] eq "aqua" && ![info exists arg(-background)]} { $wn configure -background systemModelessDialogBackgroundActive }
  if {[info exists arg(-background)]} { ::tclmacbag::combo_Set $wn -background $arg(-background) }
  if {[info exists arg(-textvariable)]} { ::tclmacbag::combo_Set $wn -textvariable $arg(-textvariable) }
  if {[info exists arg(-values)]} { ::tclmacbag::combo_Set $wn -values $arg(-values) }
  if {[info exists arg(-postcommand)]} { ::tclmacbag::combo_Set $wn -postcommand $arg(-postcommand) }
  if {[info exists arg(-state)]} { 
  if {$value == "readonly" && [winfo class $wn]=="Menubutton"} { set arg(-state) normal }
   ::tclmacbag::combo_Set $wn -state $arg(-state) 
   }
  # Set the width
  if {[info exists arg(-values)]} {
   set max 0 ; foreach value $::tclmacbag::combovalues($wn) { if {[string length [list $value]] >= $max} { set max [string length [list $value]] } ; set txt $value }
   if {$max > 5} { set mod $::tclmacbag::combo_charsizemod } else { set mod 1.5 }
   if {$max > 10} { set mod [expr $mod-0.1] } 
   if {$max > 15} { set mod [expr $mod-0.1] } 
   }
  } else {
  # Tile/Ttk on Windows/X11. Just a simple read-only combobox using Tile.
  ttk::combobox $wn -state readonly
  foreach {opt value} $args {
   switch -- $opt {
    "-textvariable" { ::tclmacbag::combo_Set $wn -textvariable $value }
    "-values" { ::tclmacbag::combo_Set $wn -values $value }
    "-postcommand" {::tclmacbag::combo_Set $wn -postcommand $value }
    "-state" { ::tclmacbag::combo_Set $wn -state $value }
    }
   }
  }
 # Finish up.
 return $wn
 }

switch -- [tk windowingsystem] { 
 "win32" { set ::tclmacbag::combo_charsizemod 1.02 }
 "aqua" { set ::tclmacbag::combo_charsizemod 1.00 }
 default { set ::tclmacbag::combo_charsizemod 1.08 }
 }

proc combo_Set {wn args} {
 # Check for bad options.
 set req 0 ; foreach {opt value} $args {
  switch -- $opt {
   "-background" {}
   "-textvariable" {}
   "-values" {}
   "-state" {}
   "-postcommand" {}
  default { bgerror "Unknown option while executing ::tclmacbag::combo_Set $wn:\n$opt $value\nMust be -textvariable, -values or -postcommand.\n" }
  }
 }
 if {[winfo class $wn]=="Menubutton"} { eval combo_Set_Menubutton $wn $args } else { eval combo_Set_Combobox $wn $args }
 return $wn
 }

proc combo_Set_Menubutton {wn args} { 
 foreach {key value} $args { set arg($key) $value }
 # Mac
 if {[info exists arg(-values)]} { set ::tclmacbag::combovalues($wn) $arg(-values) } ;# Temp thing until I sort out querying the menu for its items.
 # Create the menu
 set var [$wn cget -textvariable]
 catch { destroy $wn.menu } ; menu $wn.menu
 if {[info exists arg(-postcommand)]} {
  if {[info exists ::tclmacbag::combovalues($wn)]} { foreach {val} $::tclmacbag::combovalues($wn) { $wn.menu add radiobutton -variable $var -label $val -value $val -command "after 50 \" $arg(-postcommand) \" ; update idletasks" } }
  } else {
  if {[info exists ::tclmacbag::combovalues($wn)]} { foreach {val} $::tclmacbag::combovalues($wn) { $wn.menu add radiobutton -variable $var -label $val -value $val } }
  }
 # Set the width
 if {[info exists ::tclmacbag::combovalues($wn)]} {
  set max 0 ; foreach value $::tclmacbag::combovalues($wn) { if {[string length [list $value]] >= $max} { set max [string length [list $value]] } ; set txt $value }
  if {$max > 5} { set mod $::tclmacbag::combo_charsizemod } else { set mod 1.5 }
  if {$max > 10} { set mod [expr $mod-0.1] } 
  if {$max > 15} { set mod [expr $mod-0.1] } 
  $wn configure -width [expr int($max * $mod)]
  }
 # Finish up
 if {[info exists arg(-background)]} { $wn configure -background $arg(-background) }
 if {[info exists arg(-textvariable)]} { $wn configure -textvariable $arg(-textvariable) }
 if {[info exists arg(-state)]} { 
  if {$value == "readonly" && [winfo class $wn]=="Menubutton"} { set arg(-state) normal }
  catch { $wn configure -state $arg(-state) } ; catch { $wn state $arg(-state) }
  }
 }

proc combo_Set_Combobox {wn args} { 
 foreach {key value} $args { set arg($key) $value }
 # X11/Windows
 if {[info exists arg(-values)]} {
  # Add the value
  set ::tclmacbag::combovalues($wn) $arg(-values)
  $wn configure -values $arg(-values)
  # Set the width
  set max 0 ; foreach value $::tclmacbag::combovalues($wn) { if {[string length [list $value]] >= $max} { set max [string length [list $value]] } ; set txt $value }
  if {$max > 5} { set mod $::tclmacbag::combo_charsizemod } else { set mod 1.5 }
  if {$max > 10} { set mod [expr $mod-0.1] } 
  if {$max > 15} { set mod [expr $mod-0.1] } 
  $wn configure -width [expr int($max * $mod)]
  }
 # Finish up
 if {[info exists arg(-textvariable)]} { $wn configure -textvariable $arg(-textvariable) }
 if {[info exists arg(-state)]} { $wn configure -state $arg(-state) ; $wn state $arg(-state) }
 if {[info exists arg(-postcommand)] && [tk windowingsystem]!="aqua"} { bind $wn <<ComboboxSelected>> $arg(-postcommand) }
 }


############
# Flat Button
############

proc flatbutton {wn args} {
 # Check for bad options.
 if {[winfo exists $wn]} { bgerror "While executing ::tclmacbag::flatbutton $wn $args:\nWidget already exists." }
 foreach {opt value} $args {
  switch -- $opt {
   "-image" {}
   "-command" {}
   "-state" {}
   "-force" {}
   default { bgerror "Unknown option while executing ::tclmacbag::flatbutton $wn:\n$opt $value\nMust be -image, -command, -state or -force.\n" }
   }
  }
 # Go ahead.
 foreach {opt value} $args { set arg($opt) $value }
 if {[tk windowingsystem]=="aqua" || ([info exists arg(-force)] && $arg(-force)=="yes")} {
  # Aqua style
  ttk::label $wn
  if {[info exists arg(-image)]} { flatbutton_Set $wn -image $arg(-image) } else { bgerror "While executing ::tclmacbag::flatbutton $wn $args:\nWidget must set an image with -image." }
  if {[info exists arg(-command)]} { ::tclmacbag::flatbutton_Set $wn -command $arg(-command) }
  if {[info exists arg(-state)] } { ::tclmacbag::flatbutton_Set $wn -state $arg(-state) }
  # Mouse bindings
  bind $wn <Enter> { ::tclmacbag::flatbutton_ButtonEnter %W }
  bind $wn <Leave> { ::tclmacbag::flatbutton_ButtonLeave %W }
  bind $wn <ButtonPress-1> { ::tclmacbag::flatbutton_ButtonDown %W }
  } else {
  # Tile style
  ttk::button $wn
  foreach {opt value} $args {
   if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
   if {$opt=="-state"} { ::tclmacbag::flatbutton_Set $wn -state $arg(-state) }
   }
  }
 return $wn
 }

proc flatbutton_Set {wn args} {
 # Check for bad options.
 foreach {opt value} $args {
  switch -- $opt {
   "-image" {}
   "-command" {}
   "-state" {}
   default { bgerror "Unknown option while executing ::tclmacbag::flatbutton_Set $wn:\n$opt $value\nMust be -image, -command or -state.\n" }
   }
  }
 # Start
 foreach {opt value} $args { set arg($opt) $value }
 if {[winfo class $wn]=="TLabel"} {
  # Aqua style
  if {[info exists arg(-image)]} {
	set h [image height $arg(-image)]
	set w [image width $arg(-image)]
	set id [image create photo -width $w -height $h]
	$id copy $arg(-image)
	$wn configure -image $id
  	}
  if {[info exists arg(-command)]} {
	bind $wn <ButtonRelease-1> "
	 if {\[$wn cget -state\] != \"disabled\" && \[info exists ::tclmacbag::flatbuttonpressable($wn)\]} {
	  ::tclmacbag::flatbutton_ButtonUp $wn
	  $arg(-command)
	  }
	 "
	}
  if {[info exists arg(-state)] } {
        set img [$wn cget -image]
        if {$arg(-state) == "enabled" || $arg(-state) == "normal" } { $img configure -palette fullcolor -gamma 1.0 ; $wn state !disabled ; $wn configure -state normal }
        if {$arg(-state) == "disabled" } { $wn state disabled ; $wn configure -state disabled ; $img configure -palette fullcolor -gamma 2.2 }
   	}
  } else {
  # Tile style
  foreach {opt value} $args {
   if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
   }
  if {[info exists arg(-state)]} {
   if {$arg(-state) == "enabled" || $arg(-state) == "normal" } { $wn configure -state normal }
   if {$arg(-state) == "disabled" } { $wn configure -state disabled }
   }
  }
 return $wn
 }

proc flatbutton_ButtonEnter {wn} {
 set ::tclmacbag::flatbuttonpressable($wn) 1
 }
proc flatbutton_ButtonLeave {wn} {
 if {[$wn cget -state] == "disabled"} return
 set img [$wn cget -image] ; $img configure -gamma 1.0
 catch { unset ::tclmacbag::flatbuttonpressable($wn) }
 }
proc flatbutton_ButtonDown {wn} {
 if {[$wn cget -state] == "disabled"} return
 set img [$wn cget -image] ; $img configure -gamma 0.3
 set ::tclmacbag::flatbuttonpressable($wn) 1
 }
proc flatbutton_ButtonUp {wn} {
 set img [$wn cget -image]
 if {[$wn cget -state] == "disabled"} {
  $img configure -palette fullcolor -gamma 2.2
  } else {
  $img configure -palette fullcolor -gamma 1.0
  }
 catch { unset ::tclmacbag::flatbuttonpressable($wn) }
 }

############
# Help Button
############

proc helpbutton {wn args} {
 if {[winfo exists $wn]} { bgerror "While executing ::tclmacbag::helpbutton $wn $args:\nWidget already exists." }
 ::tclmacbag::helpbutton_init ;# Create resources if needed
 set req 0 ; foreach {opt value} $args {
  switch -- $opt {
   "-command" { incr req }
   default { bgerror "While executing ::tclmacbag::helpbutton $wn $args:\nUnknown option $opt $value\nMust be -command.\n" }
   }
  }
 if {![info exists req] || $req < 1} { bgerror "While executing ::tclmacbag::helpbutton $wn $args\nRequires -command\n" }
 # Flatbutton as a template
 ::tclmacbag::flatbutton $wn -image TclMacBag.helpbutton -force yes
 # Allocate
 foreach {opt value} $args { set arg($opt) $value }
 if {[info exists arg(-command)]} { ::tclmacbag::helpbutton_Set $wn -command $arg(-command) }
 # Bindings for Mac version
 if {[info exists ::tile::currentTheme]} { set ThemeNow $::tile::currentTheme } else { set ThemeNow $::ttk::currentTheme }
 if {$ThemeNow=="aqua"} {
  # Mouse bindings
  bind $wn <Enter> { ::tclmacbag::helpbutton_Mac_ButtonEnter %W }
  bind $wn <Leave> { ::tclmacbag::helpbutton_Mac_ButtonLeave %W }
  bind $wn <1> { ::tclmacbag::helpbutton_Mac_ButtonDown %W }
  set img [$wn cget -image] ; $img configure -gamma 1.0
  }
 return $wn
 }

proc helpbutton_Set {wn args} {
 # Check for bad options.
 foreach {opt value} $args {
  switch -- $opt {
   "-command" {}
   default { bgerror "Unknown option while executing ::tclmacbag::helpbutton_Set $wn:\n$opt $value\nMust be -command.\n" }
   }
  }
 # Start
 foreach {opt value} $args { set arg($opt) $value }
 if {[info exists arg(-command)]} {
  bind $wn <ButtonRelease-1> "
   if {\[$wn cget -state\] != \"disabled\" && \[info exists ::tclmacbag::flatbuttonpressable($wn)\]} {
    ::tclmacbag::flatbutton_ButtonUp $wn
    $arg(-command)
    }
   "
  }
 }

proc helpbutton_Mac_ButtonEnter {wn} {
 set ::tclmacbag::flatbuttonpressable($wn) 1
 }
proc helpbutton_Mac_ButtonLeave {wn} {
 if {[$wn cget -state] == "disabled"} return
 set img [$wn cget -image] ; $img configure -gamma 1.0
 catch { unset ::tclmacbag::flatbuttonpressable($wn) }
 }
proc helpbutton_Mac_ButtonDown {wn} {
 if {[$wn cget -state] == "disabled"} return
 set img [$wn cget -image] ; $img configure -gamma 0.4
 set ::tclmacbag::flatbuttonpressable($wn) 1
 }
proc helpbutton_Mac_ButtonUp {wn} {
 if {[$wn cget -state] == "disabled"} {
  $img configure -palette fullcolor -gamma 1.0
  } else {
  $img configure -palette fullcolor -gamma 0.4
  }
 catch { unset ::tclmacbag::flatbuttonpressable($wn) }
 }

############
# Style Button
############

proc stylebutton {wn args} {
 # Check for bad/incomplete options.
 if {[winfo exists $wn]} { bgerror "While executing ::tclmacbag::stylebutton $wn $args:\nWidget already exists.\n" ; return }
 # Collect options
 foreach {opt value} $args { set arg($opt) $value }
 if {![info exists arg(-style)]} { set arg(-style) "pill" } ;# Pill button is our default
 ::tclmacbag::stylebutton_init $arg(-style)
 # Is this a supported style?
 if {[lsearch -exact $::tclmacbag::allowedbuttonstyles $arg(-style)] == -1 } {
  bgerror "While executing ::tclmacbag::stylebutton $wn $args:\n$arg(-style) is not a supported style.\nAllowed: $::tclmacbag::allowedbuttonstyles\n\n" ; return
  }
 if {[tk windowingsystem]=="aqua" || ([info exists arg(-force)] && $arg(-force)=="yes")} {
  # If there's no image, we'll use a default one to start off with (extension user can use -text to override it later).
  if {![info exists arg(-image)]} { set arg(-image) TclMacBag.search-magglass ; set lrborder 10 } else { set lrborder 0 }
  # Carry on
  if {[info exists arg(-background)]} {
   # Create new images with the user specified background.
   set id1 [image create photo -format PNG -width [image width TclMacBag.${arg(-style)}1] -height [image height TclMacBag.${arg(-style)}1] -data [TclMacBag.${arg(-style)}1 data -format PNG -background $arg(-background)]]
   set id2 [image create photo -format PNG -width [image width TclMacBag.${arg(-style)}2] -height [image height TclMacBag.${arg(-style)}2] -data [TclMacBag.${arg(-style)}2 data -format PNG -background $arg(-background)]]
   } else {
   # No background specified. Lets hope the Tile widget defaults are nice.
   set id1 [image create photo -format PNG -width [image width TclMacBag.${arg(-style)}1] -height [image height TclMacBag.${arg(-style)}1] -data [TclMacBag.${arg(-style)}1 data -format PNG]]
   set id2 [image create photo -format PNG -width [image width TclMacBag.${arg(-style)}2] -height [image height TclMacBag.${arg(-style)}2] -data [TclMacBag.${arg(-style)}2 data -format PNG]]
   }
  if {[lsearch -exact [$::tclmacbag::ttkstylecmd element names] "$wn.${arg(-style)}.button"] == -1 } {
   if {[info exists ::tile::version] && $::tile::version <= "0.7.8" } {
    # Create the style - the Tile 0.7.8 method
    $::tclmacbag::ttkstylecmd configure $wn.${arg(-style)} -relief flat -anchor center
    $::tclmacbag::ttkstylecmd element create $wn.${arg(-style)}.button image $id2 -map [list disabled $id2 pressed $id1 active $id2] -border [list $lrborder 0 $lrborder] -sticky nsew
    $::tclmacbag::ttkstylecmd layout $wn.${arg(-style)} "$wn.${arg(-style)}.button -children { Button.label } "
    } else {
    # Tile 0.8.x+ method. Given some testing by Joe English and tweaks provided. Should work.
    $::tclmacbag::ttkstylecmd configure $wn.${arg(-style)} -relief flat -anchor center
    $::tclmacbag::ttkstylecmd element create $wn.${arg(-style)}.button image [list $id2 disabled $id2 pressed $id1 active $id2] -border [list $lrborder 0 $lrborder] -sticky nsew
    $::tclmacbag::ttkstylecmd layout $wn.${arg(-style)} "$wn.${arg(-style)}.button -children { Button.label } "
    }
   }
  # Create button
  if {[tk windowingsystem]=="aqua"} {
   # Mac doesn't support the stippling for greyed images well, so Tile doesn't at all. Lets create a "greyed" user image variant.
   set h [image height $arg(-image)]
   set w [image width $arg(-image)]
   set disabledpic [image create photo -width $w -height $h]
   $disabledpic copy $arg(-image)
   $disabledpic configure -gamma 2.0 -palette 16
   ttk::button $wn -style $wn.$arg(-style) -image "$arg(-image) disabled $disabledpic pressed $arg(-image) active $arg(-image)"
   } else {
   # Other platforms have stippling, so we'll leave it compatible with the default Tile method for easy tclmacbag/ttk co-existence.
   ttk::button $wn -style $wn.$arg(-style) -image $arg(-image)
   }
  # Set various Tile settings.
  foreach {opt value} $args {
   if {$opt eq "-style"} continue
   if {$opt eq "-force"} continue
   # if {$opt eq "-command"} continue
   if {$opt eq "-text"} continue
   if {$opt eq "-variable"} continue
   if {$opt eq "-onwhen"} continue
   if {$opt eq "-background"} continue
   if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
   }
  } else {
  # X11/Windows
  ttk::button $wn ;# -style Toolbutton
  # Set various Tile settings.
  foreach {opt value} $args {
   if {$opt eq "-style"} continue
   if {$opt eq "-force"} continue
   # if {$opt eq "-command"} continue
   if {$opt eq "-text"} continue
   if {$opt eq "-variable"} continue
   if {$opt eq "-onwhen"} continue
   if {$opt eq "-background"} continue
   if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
   }
  }
 # Using a -text option? Cancel the user image and set the text
 if {[info exists arg(-text)]} { $wn configure -image {} -text $arg(-text) }
 # End of style stuff. Now lets set general options.
 return $wn
 }

############
# View Button
############

proc viewbutton {wn args} {
 # Check for bad/incomplete options.
 if {[winfo exists $wn]} { bgerror "While executing ::tclmacbag::stylebutton $wn $args:\nWidget already exists.\n" ; return }
 # Collect options
 foreach {opt value} $args { set arg($opt) $value }
 if {![info exists arg(-style)]} { set arg(-style) "pill" } ;# Pill button is our default
 ::tclmacbag::stylebutton_init $arg(-style)
 # Is this a supported style?
 if {[lsearch -exact $::tclmacbag::allowedbuttonstyles $arg(-style)] == -1 } {
  bgerror "While executing ::tclmacbag::stylebutton $wn $args:\n$arg(-style) is not a supported style.\nAllowed: $::tclmacbag::allowedbuttonstyles\n\n" ; return
  }
 if {[tk windowingsystem]=="aqua" || ([info exists arg(-force)] && $arg(-force)=="yes")} {
  # If there's no image, we'll use a default one to start off with (extension user can use -text to override it later).
  if {![info exists arg(-image)]} { set arg(-image) TclMacBag.search-magglass ; set lrborder 10 } else { set lrborder 0 }
  # Carry on
  if {[info exists arg(-background)]} {
   # Create new images with the user specified background.
   set id1 [image create photo -format PNG -width [image width TclMacBag.${arg(-style)}1] -height [image height TclMacBag.${arg(-style)}1] -data [TclMacBag.${arg(-style)}1 data -format PNG -background $arg(-background)]]
   set id2 [image create photo -format PNG -width [image width TclMacBag.${arg(-style)}2] -height [image height TclMacBag.${arg(-style)}2] -data [TclMacBag.${arg(-style)}2 data -format PNG -background $arg(-background)]]
   } else {
   # No background specified. Lets hope the Tile widget defaults are nice.
   set id1 [image create photo -format PNG -width [image width TclMacBag.${arg(-style)}1] -height [image height TclMacBag.${arg(-style)}1] -data [TclMacBag.${arg(-style)}1 data -format PNG]]
   set id2 [image create photo -format PNG -width [image width TclMacBag.${arg(-style)}2] -height [image height TclMacBag.${arg(-style)}2] -data [TclMacBag.${arg(-style)}2 data -format PNG]]
   }
  if {[lsearch -exact [$::tclmacbag::ttkstylecmd element names] "$wn.${arg(-style)}.button"] == -1 } {
   if {[info exists ::tile::version] && $::tile::version <= "0.7.8" } {
    # Create the style - the Tile 0.7.8 method
    $::tclmacbag::ttkstylecmd configure $wn.${arg(-style)} -relief flat
    $::tclmacbag::ttkstylecmd element create $wn.${arg(-style)}.button image $id2 -map [list disabled $id2 pressed $id1 active $id2] -border [list $lrborder 0 $lrborder] -sticky nsew
    $::tclmacbag::ttkstylecmd layout $wn.${arg(-style)} "$wn.${arg(-style)}.button -children { Button.label } "
    } else {
    # Tile 0.8.x+ method. Given some testing by Joe English and tweaks provided. Should work.
    $::tclmacbag::ttkstylecmd configure $wn.${arg(-style)} -relief flat -anchor center
    $::tclmacbag::ttkstylecmd element create $wn.${arg(-style)}.button image [list $id2 disabled $id2 pressed $id1 active $id2] -border [list $lrborder 0 $lrborder] -sticky nsew
    $::tclmacbag::ttkstylecmd layout $wn.${arg(-style)} "$wn.${arg(-style)}.button -children { Button.label } "
    }
   } ;# No 'style element configure' or 'style element delete' in Tile...
  # Create button
  if {[tk windowingsystem]=="aqua"} {
   # Mac doesn't support the stippling for greyed images well, so Tile doesn't at all. Lets create a "greyed" user image variant.
   set h [image height $arg(-image)]
   set w [image width $arg(-image)]
   set disabledpic [image create photo -width $w -height $h]
   $disabledpic copy $arg(-image)
   $disabledpic configure -gamma 2.0 -palette 16
   ttk::button $wn -style $wn.$arg(-style) -image "$arg(-image) disabled $disabledpic pressed $arg(-image) active $arg(-image)"
   } else {
   # Other platforms have stippling, so we'll leave it compatible with the default Tile method for easy tclmacbag/ttk co-existence.
   ttk::button $wn -style $wn.$arg(-style) -image $arg(-image)
   }
  # Set various Tile settings.
  foreach {opt value} $args {
   if {$opt eq "-style"} continue
   if {$opt eq "-force"} continue
   # if {$opt eq "-command"} continue
   if {$opt eq "-text"} continue
   if {$opt eq "-variable"} continue
   if {$opt eq "-onwhen"} continue
   if {$opt eq "-background"} continue
   if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
   }
  } else {
  # X11/Windows
  ttk::button $wn
  # Set various Tile settings.
  foreach {opt value} $args {
   if {$opt eq "-style"} continue
   if {$opt eq "-force"} continue
   # if {$opt eq "-command"} continue
   if {$opt eq "-text"} continue
   if {$opt eq "-variable"} continue
   if {$opt eq "-onwhen"} continue
   if {$opt eq "-background"} continue
   if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
   }
  }
 # Using a -text option? Cancel the user image and set the text
 if {[info exists arg(-text)]} { $wn configure -image {} -text $arg(-text) }
 # Set up the command, ensuring the first thing done is to set the traced variable to the value of this button.
 if {[info exists arg(-command)]} { $wn configure -command "set $arg(-variable) $arg(-onwhen) ; $arg(-command)" }
 # Now we set up our variable trace which sets the button states
 trace variable $arg(-variable) rwu "::tclmacbag::viewbutton_State $wn -variable $arg(-variable) -onwhen $arg(-onwhen)"
 # Any click (including cancelled clicks) also cause us to update the button state:
 # this resets any greyed tristate appearance settings.
 bind $wn <1> "::tclmacbag::viewbutton_State $wn -variable $arg(-variable) -onwhen $arg(-onwhen)"
 # End of style stuff. Now lets set general options.
 return $wn
 }

proc viewbutton_State {wn args} {
 # Collect options
 foreach {opt value} $args { set arg($opt) $value }
 upvar $arg(-variable) val
 if {$val==$arg(-onwhen)} { $wn state pressed } else { $wn state !pressed }
 }

############
# Search Entry
# Originally based on the search field by Schelte Bron: http://wiki.tcl.tk/18188
# ... who is not to blame for its feature creep ;-).
############

proc searchentry {wn args} {
 foreach {opt value} $args { set arg($opt) $value }
 # Check for bad/incomplete options.
 if {[winfo exists $wn]} { bgerror "While executing ::tclmacbag::searchentry $wn $args:\nWidget already exists." ; return }
 # Init resources
 ::tclmacbag::searchentry_init
 # Start
 if {[::tclmacbag::TileThemeNow]=="aqua" || ([info exists arg(-force)] && $arg(-force)=="yes")} {
  # Mac
  switch [::tclmacbag::TileThemeNow] {
   "aqua"      { set color White }
   "winnative" { set color "SystemButtonFace" }
   "xpnative"  { set color "SystemButtonFace" }
   "clam"      { set color "#dcdad5" }
   "step"      { set color "#a0a0a0" }
   default     { set color "#d9d9d9" }
   } ;# Set styles (with care taken to produce images with backgrounds matching their surrounding frames).
  if {[info exists arg(-background)]} {
   # Standard method
   set id1 [image create photo -format PNG -width [image width TclMacBag.search-mac1] -height [image height TclMacBag.search-mac1] -data [TclMacBag.search-mac1 data -format PNG -background $arg(-background)]]
   set id2 [image create photo -format PNG -width [image width TclMacBag.search-mac2] -height [image height TclMacBag.search-mac2] -data [TclMacBag.search-mac2 data -format PNG -background $arg(-background)]]
   } else {
   # Testing this code out at times to see if it produces satisfactory results. Shouldn't be triggered in dist versions yet.
   set id1 [image create photo -format PNG -width [image width TclMacBag.search-mac1] -height [image height TclMacBag.search-mac1] -data [TclMacBag.search-mac1 data -format PNG]]
   set id2 [image create photo -format PNG -width [image width TclMacBag.search-mac2] -height [image height TclMacBag.search-mac2] -data [TclMacBag.search-mac2 data -format PNG]]
   }
  if {[info exists arg(-image)]} {
   # User image
   if {[image width $arg(-image)] != 13 || [image height $arg(-image)] != 13} { bgerror "While executing ::tclmacbag::searchentry $wn $args:\nImages for this widget must be 13x13." ; return }
   $id1 copy $arg(-image) -compositingrule overlay -from 0 0 13 13 -to 7 7
   $id2 copy $arg(-image) -compositingrule overlay -from 0 0 13 13 -to 7 7
   } else {
   # Default image
   $id1 copy TclMacBag.search-magglass -compositingrule overlay -from 0 0 13 13 -to 7 7
   $id2 copy TclMacBag.search-magglass -compositingrule overlay -from 0 0 13 13 -to 7 7
   }
  if {[lsearch -exact [$::tclmacbag::ttkstylecmd element names] "$wn.Search.field"] == -1 } {
   if {[info exists ::tile::version] && $::tile::version <= "0.7.8" } {
    $::tclmacbag::ttkstylecmd element create $wn.Search.field image $id1 -border {22 4 14} -sticky ew -map "focus $id2" ;# Tile 0.7.x
    } else {
    $::tclmacbag::ttkstylecmd element create $wn.Search.field image [list $id1 focus $id2] -border {22 4 14} -sticky ew ;# Tile 0.8.x
    }
   $::tclmacbag::ttkstylecmd layout $wn.Search.entry " $wn.Search.field -sticky nswe -border 1 -children { Entry.padding -sticky nswe -children { Entry.textarea -sticky nswe } } "
   } ;# Elements may only be created once and cannot be deleted.
  ttk::entry $wn -style $wn.Search.entry
  # Other opts
  foreach {opt value} $args {
   if {$opt eq "-image"} { continue }
   if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
   }
  } else {
  # X11/Windows
  if {[::tclmacbag::TileThemeNow] == "xpnative"} { 
   set id1 [image create photo -format PNG -width [image width TclMacBag.search-xp] -height [image height TclMacBag.search-xp] -data [TclMacBag.search-xp data -format PNG]]
   } else {
   set id1 [image create photo -format PNG -width [image width TclMacBag.search-x11] -height [image height TclMacBag.search-x11] -data [TclMacBag.search-x11 data -format PNG]]
   }
  if {[info exists arg(-image)]} {
   $id1 copy $arg(-image) -compositingrule overlay -from 0 0 13 13 -to 3 4
   } else {
   $id1 copy TclMacBag.search-magglass -compositingrule overlay -from 0 0 13 13 -to 3 4
   }
  if {[lsearch -exact [$::tclmacbag::ttkstylecmd element names] "$wn.Search.field"] == -1 } {
   $::tclmacbag::ttkstylecmd element create $wn.Search.field image $id1 -border {18 4 1} -sticky ew
   $::tclmacbag::ttkstylecmd layout $wn.Search.entry " $wn.Search.field -sticky nswe -border 3 -children { Entry.padding -sticky nswe -children { Entry.textarea -sticky nswe } } "
   } ;# Elements may only be created once and cannot be deleted.
  ttk::entry $wn -style $wn.Search.entry
  foreach {opt value} $args {
   if {$opt eq "-image"} { continue }
   if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
   }
  }
 # RightClick bindings
 bind $wn <<RightClick>> "::tclmacbag::entry_popup ${wn}"
 # Return
 return $wn
 }

############
# Colourful frame
# From the Wiki.
############

proc colorframe {wn args} {
 # Check for bad/incomplete options.
 if {[winfo exists $wn]} { bgerror "While executing ::tclmacbag::colorframe $wn $args:\nWidget already exists." }
 # Start
 foreach {opt value} $args { set arg($opt) $value }
 if {([info exists arg(-background)] && [::tclmacbag::TileThemeNow] == "aqua") || ([info exists arg(-background)] && [info exists arg(-force)] && $arg(-force)=="yes")} { frame $wn -background $arg(-background) } else { ttk::frame $wn } ;# #B2B2B2 suggested for Mac
 return $wn
 }

############
# Top Level
# By Schelte Bron http://wiki.tcl.tk/11075
############

proc toplevel {w args} {
 eval [linsert $args 0 ::toplevel $w]
 place [ttk::frame $w.tilebg] -x 0 -y 0 -relwidth 1 -relheight 1
 set w
 }

############
# Removable Toolbar:
# Similar idea to Kevin Walzer's Mac toolbar extension, but, a bit differently done.
############

proc toolbar {wn args} {
 # Check for bad/incomplete options.
 foreach {opt value} $args { set arg($opt) $value }
 # Set up the button, if we're on a Mac and using Aqua.
 if {[tk windowingsystem] eq "aqua"} { 
  tk::unsupported::MacWindowStyle style [winfo toplevel $wn] document {toolbarButton closeBox collapseBox resizable horizontalZoom verticalZoom} 
  }
 set ::tclmacbag::toolbarargs($wn) $args
 eval grid $wn $::tclmacbag::toolbarargs($wn)
 set w [winfo toplevel $wn]
 bind $w <<ToolbarButton>> "::tclmacbag::toolbar_Toggle $wn"
 set ::tclmacbag::toolbarisdisplayed($w) 1
 }

proc toolbar_Toggle {wn} {
 set tl [winfo toplevel $wn]
 if {![info exists ::tclmacbag::toolbarhidden($tl)]} {
  # Hide the toolbar
  set ::tclmacbag::toolbarhidden($tl) 1
  set ::tclmacbag::toolbarisdisplayed($tl) 0
  grid forget $wn
  } else {
  # Show the toolbar
  catch { unset ::tclmacbag::toolbarhidden($tl) }
  set ::tclmacbag::toolbarisdisplayed($tl) 1
  eval grid $wn $::tclmacbag::toolbarargs($wn)
  }
 }

proc toolbar_ToggleTo {wn args} {
 set tl [winfo toplevel $wn]
 foreach {opt value} $args { set arg($opt) $value }
 if {$arg(-state)=="on"} {
  # Switch on
  catch { unset ::tclmacbag::toolbarhidden($tl) }
  ::tclmacbag::toolbar_Toggle $w
  } else {
  # Switch off
  set ::tclmacbag::toolbarhidden($tl) 1
  set ::tclmacbag::toolbarisdisplayed($tl) 0
  ::tclmacbag::toolbar_Toggle $w
  }
 }

############
# Plain Box:
# Cheers to Joe English for the info used for this.
# This is a convenience widget.
############

proc boxframe {w} { 
 if {[info exists ::tile::currentTheme]} { set ThemeNow $::tile::currentTheme } else { set ThemeNow $::ttk::currentTheme }
 if {$ThemeNow == "aqua" || $ThemeNow == "xpnative" || $ThemeNow == "winnative" } { 
  ttk::frame $w -style Boxframe -padding 3 -borderwidth 3 
  } else { 
  ::frame $w -borderwidth 1 -relief sunken -padx 3 -pady 3
  }
 return $w
 }

############
# Scrollbar
# This replaces the old interp alias method in v0.11.
############

proc ::tclmacbag::scrollbar {wn args} { 
 if {[info exists ::tile::currentTheme]} { set ThemeNow $::tile::currentTheme } else { set ThemeNow $::ttk::currentTheme }
 if {[::tclmacbag::TileThemeNow] == "aqua" || $::win32(APIVendor) eq "ReactOS"} { 
  eval ::scrollbar $wn $args 
  } else {
  eval ttk::scrollbar $wn $args
  }
 return $wn
 }

############
# Checkbutton
# Same as the Tile one except with a a work around to remove tri-state (which 
# should never have been made a default, let alone a mandatory option).
############

proc ::tclmacbag::checkbutton {wn args} { 
 foreach {opt value} $args { set arg($opt) $value }
 if {[info exists arg(-variable)] && ![info exists $arg(-variable)]} { set arg(-variable) "" }
 ttk::checkbutton $wn
 foreach {opt value} $args { 
  if {[catch { $wn configure $opt $value } err]} { bgerror "$wn: $err" }
  }
 return $wn
 }

############
# Tile Information Querying
# As Tile's innards change, we need to keep track of basics.
############

# Urgh. Tile/Ttk namespace name changes in the switch from 0.7.x to 0.8.x.
if {[package require tile] <= "0.7.8" } { set ::tclmacbag::ttkstylecmd style } else { set ::tclmacbag::ttkstylecmd ttk::style }

proc ::tclmacbag::TileThemeNow {} {
 if {[info exists ::tile::currentTheme]} { set ThemeNow $::tile::currentTheme } else { set ThemeNow $::ttk::currentTheme }
 return "$ThemeNow"
 }

############
# Inits and other Miscellanea
############

# What's a right-click? Mac differs from everyone else.
catch { event delete <<RightClick>> }
switch -- [lindex $tcl_platform(os) 0] {
 "Aqua"  { event add <<RightClick>> <Control-ButtonPress-1> }
 default { event add <<RightClick>> <ButtonRelease-3> }
 }

# Stylebutton images
set ::tclmacbag::allowedbuttonstyles {}
lappend ::tclmacbag::allowedbuttonstyles pill pill-left pill-middle pill-right
lappend ::tclmacbag::allowedbuttonstyles chrome chrome-left chrome-middle chrome-right
lappend ::tclmacbag::allowedbuttonstyles steel steel-left steel-middle steel-right
lappend ::tclmacbag::allowedbuttonstyles simple simple-left simple-middle simple-right
lappend ::tclmacbag::allowedbuttonstyles safari safari-left safari-middle safari-right
lappend ::tclmacbag::allowedbuttonstyles capsule capsule-left capsule-middle capsule-right
lappend ::tclmacbag::allowedbuttonstyles tnb tnb-left tnb-middle tnb-right
lappend ::tclmacbag::allowedbuttonstyles mail mail-left mail-middle mail-right
lappend ::tclmacbag::allowedbuttonstyles clearcap clearcap-left clearcap-middle clearcap-right

# Disclosure buttons
lappend ::tclmacbag::allowedbuttonstyles gel gel-small
set ::tclmacbag::allowedpnbstyles [list tnb pill steel safari chrome simple mail capsule clearcap]

# Spinbox buttons - Image creation handled elsewhere
# lappend ::tclmacbag::allowedbuttonstyles spinbox-top spinbox-bottom

# Whose Windows API is this, anyway?
proc ::tclmacbag::getWindowsAPIVendor {} {
 set ::win32(APIVendor) "Unknown"
 if {[tk windowingsystem] != "win32"} { return -1 }
 package require registry
 if {![catch { registry keys "HKEY_CURRENT_USER\\Software\\Wine" } junk]} {
  set ::win32(APIVendor) Wine
  } elseif {![catch { registry keys "HKEY_CURRENT_USER\\Software\\ReactOS" } junk]} {
  set ::win32(APIVendor) ReactOS
  } else {
  # If neither, we're (probably) on Microsoft Windows
  set ::win32(APIVendor) Microsoft
  }
 return "$::win32(APIVendor)"
 } ; ::tclmacbag::getWindowsAPIVendor ;# Populate the info variable


proc pnb_viewbutton_State {wn args} {
 # Collect options
 foreach {opt value} $args { set arg($opt) $value }
 upvar $arg(-variable) val
 if {$val==$arg(-onwhen)} { $wn state { pressed !active !alternate} } else { $wn state { !pressed !active !alternate} }
 }

# Mouse click bindings - Names follow Windows/X11 standards
switch -- [string tolower [lindex $tcl_platform(os) 0]] {
 "darwin"	{
 		event add <<RightClick>> <ButtonPress-2>
 		event add <<RightClick>> <Control-ButtonPress-1>
 		event add <<MiddleClick>> <ButtonRelease-3>
 		event add <<LeftClick>> <ButtonRelease-1>
 		}
 default 	{
 		event add <<RightClick>> <ButtonRelease-3>
 		event add <<MiddleClick>> <ButtonRelease-2>
 		event add <<LeftClick>> <ButtonRelease-1>
 		}
 }

# Creates a plain notebook style for Groupbox and Pamphlet.
$::tclmacbag::ttkstylecmd layout Plain.TNotebook.Tab null
$::tclmacbag::ttkstylecmd layout Plain.TNotebook null
$::tclmacbag::ttkstylecmd configure Groupbox.TLabelframe -labeloutside false
$::tclmacbag::ttkstylecmd configure Groupbox.TMenubutton
$::tclmacbag::ttkstylecmd theme settings default "$::tclmacbag::ttkstylecmd layout Plain.TNotebook.Tab null"

# Boxframe
$::tclmacbag::ttkstylecmd layout Boxframe { Labelframe.border }
$::tclmacbag::ttkstylecmd configure Boxframe -borderwidth 2 -relief sunken

# Margins/Padding default values.
# ipad = inner padding/margins, opad = outer padding/margins
switch [::tclmacbag::TileThemeNow] {
 "aqua"     {set ::tclmacbag::ipad 20 ; set ::tclmacbag::opad 20 ; set ::tclmacbag::thinpad 5 ; set ::tclmacbag::tbxpad 10 ; set ::tclmacbag::tbypad 10} 
 "aero"     {set ::tclmacbag::ipad 20 ; set ::tclmacbag::opad 20 ; set ::tclmacbag::thinpad 5 ; set ::tclmacbag::tbxpad 5 ; set ::tclmacbag::tbypad 3} 
 default    {set ::tclmacbag::ipad 5 ; set ::tclmacbag::opad 5 ; set ::tclmacbag::thinpad 0 ; set ::tclmacbag::tbxpad 5 ; set ::tclmacbag::tbypad 3}
 }

# Labelframes
font create TclMacBagBold ; font configure TclMacBagBold -family [font configure TkDefaultFont -family] -size [font configure TkDefaultFont -size] -weight bold
font create TclMacBagLarger ; font configure TclMacBagLarger -family [font configure TkDefaultFont -family] -size [expr [font configure TkDefaultFont -size]+1] -weight bold
font create TclMacBagVista ; font configure TclMacBagLarger -family [font configure TkDefaultFont -family] -size [expr [font configure TkDefaultFont -size]+3]
switch [::tclmacbag::TileThemeNow] {
 "aqua"     { ttk::style configure TLabelframe.Label -font TclMacBagBold -foreground black } 
 "win32"    { ttk::style configure TLabelframe.Label -font TkDefaultFont -foreground black } 
 "xpnative" { 
  if {$::tcl_platform(osVersion) < 6} {
   # Windows XP
   ttk::style configure TLabelframe.Label -font TkDefaultFont -foreground {#00009C}
   } else {
   # Vista and Seven
   ttk::style configure TLabelframe.Label -font TclMacBagVista -foreground darkgreen
   }
  } 
 "vista"     { ttk::style configure TLabelframe.Label -font TclMacBagVista -foreground darkgreen } 
 default    { ttk::style configure TLabelframe.Label -font TclMacBagBold -foreground black}
 }

#############################################################################################
}
