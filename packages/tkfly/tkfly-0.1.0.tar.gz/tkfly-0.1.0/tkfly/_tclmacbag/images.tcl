##############
# Image Init
# Part of TclMacBag by Peter Caffin, 2007.
##############

proc ::tclmacbag::stylebutton_init {name} {
 # Bail if the image exists
 if {[lsearch [image names] "TclMacBag.${name}-left"]>=0} return
 if {$name=="tnb"} return
 # Create
 image create photo TclMacBag.${name}1 -file [file join $::tclmacbag::basedir Resources ${name}-down.gif]
 image create photo TclMacBag.${name}2 -file [file join $::tclmacbag::basedir Resources ${name}-up.gif]
 }

proc ::tclmacbag::dframe_init {} {
 if {[lsearch [image names] "TclMacBag.dframeimage(open)"]>=0} return
 # Images for dframe
 if {[tk windowingsystem] == "win32"} {
  image create photo TclMacBag.dframeimage(open)   -file [file join $::tclmacbag::basedir Resources dframe-minus.png]
  image create photo TclMacBag.dframeimage(closed) -file [file join $::tclmacbag::basedir Resources dframe-plus.png]
  } else {
  image create photo TclMacBag.dframeimage(open)   -file [file join $::tclmacbag::basedir Resources dframe-open.png]
  image create photo TclMacBag.dframeimage(closed) -file [file join $::tclmacbag::basedir Resources dframe-closed.png]
  }
 }

proc ::tclmacbag::ddialog_init {} {
 if {[lsearch [image names] "TclMacBag.ddialogimage(open)"]>=0} return
 # Images for dframe
 if {[tk windowingsystem] == "win32"} {
  image create photo TclMacBag.ddialogimage(open)   -file [file join $::tclmacbag::basedir Resources ddialog-winopen.png]
  image create photo TclMacBag.ddialogimage(closed) -file [file join $::tclmacbag::basedir Resources ddialog-winclosed.png]
  } else {
  image create photo TclMacBag.ddialogimage(open)   -file [file join $::tclmacbag::basedir Resources ddialog-open.png]
  image create photo TclMacBag.ddialogimage(closed) -file [file join $::tclmacbag::basedir Resources ddialog-closed.png]
  }
 }

proc ::tclmacbag::dbutton_init {} {
 if {[lsearch [image names] "TclMacBag.dbuttonimage(open)"]>=0} return
 # Images for dframe
 if {[tk windowingsystem] == "win32"} {
  image create photo TclMacBag.dbuttonimage(open)   -file [file join $::tclmacbag::basedir Resources dbutton-winopen.png]
  image create photo TclMacBag.dbuttonimage(closed) -file [file join $::tclmacbag::basedir Resources dbutton-winclosed.png]
  } else {
  image create photo TclMacBag.dbuttonimage(open)   -file [file join $::tclmacbag::basedir Resources dbutton-open.png]
  image create photo TclMacBag.dbuttonimage(closed) -file [file join $::tclmacbag::basedir Resources dbutton-closed.png]
  }
 }

proc ::tclmacbag::pnb_init {name} {
 # Bail if the image exists
 if {[lsearch [image names] "TclMacBag.${name}1"]>=0} return
 # Create
 image create photo TclMacBag.${name}1 -file [file join $::tclmacbag::basedir Resources ${name}-down.gif]
 image create photo TclMacBag.${name}2 -file [file join $::tclmacbag::basedir Resources ${name}-up.gif]
 }


proc ::tclmacbag::helpbutton_init {} {
 # Bail if the image exists
 if {[lsearch [image names] "TclMacBag.helpbutton"]>=0} return
 # Create
 switch -- [string tolower [lindex $::tcl_platform(os) 0]] {
  "windows" { image create photo TclMacBag.helpbutton -file [file join $::tclmacbag::basedir Resources help-windows.gif] }
  "darwin"  { image create photo TclMacBag.helpbutton -file [file join $::tclmacbag::basedir Resources help-mac.gif] }
  default   { image create photo TclMacBag.helpbutton -file [file join $::tclmacbag::basedir Resources help-x11.gif] }
  }
 }

proc ::tclmacbag::actionbutton_init {name} {
 # Bail if the image exists
 if {[lsearch [image names] "TclMacBag.action-$name"]>=0} return
 # Create (will be one of: gear, plus, minus)
 image create photo TclMacBag.action-$name -file [file join $::tclmacbag::basedir Resources action-$name.png]
 }

proc ::tclmacbag::scopebutton_init {} {
 # Bail if the image exists
 if {[lsearch [image names] "TclMacBag.scope-blank"]>=0} return
 image create photo TclMacBag.scope-blank -file [file join $::tclmacbag::basedir Resources scope-blank12x12.png]
 image create photo TclMacBag.scope-crossAqua -file [file join $::tclmacbag::basedir Resources scope-crossAqua.png]
 image create photo TclMacBag.scope-crossAquaActive -file [file join $::tclmacbag::basedir Resources scope-crossAquaActive.png]
 image create photo TclMacBag.scope-oval -file [file join $::tclmacbag::basedir Resources scope-oval.png]
 image create photo TclMacBag.scope-ovalBlank -file [file join $::tclmacbag::basedir Resources scope-ovalBlank.png]
 image create photo TclMacBag.scope-ovalDark -file [file join $::tclmacbag::basedir Resources scope-ovalDark.png]
 image create photo TclMacBag.scope-ovalLight -file [file join $::tclmacbag::basedir Resources scope-ovalLight.png]
 # Ttk layout
 ttk::style element create scope.background image \
     [list  TclMacBag.scope-blank                        \
 	 {background}                 TclMacBag.scope-blank  \
 	 {active !disabled !pressed}  TclMacBag.scope-oval   \
 	 {pressed !disabled}          TclMacBag.scope-ovalDark \
 	 {selected !disabled !pressed} TclMacBag.scope-ovalDark\
 	 {selected disabled} TclMacBag.scope-ovalDark]\
         \
     -border {6 6 6 6} -padding {0} -sticky news
 ttk::style layout scope {
     scope.background -children {
 	scope.padding -children {
 	    scope.label
 	}
     }
  }	  
 ttk::style configure scope  \
  -padding {6 0 6 1} -relief flat -font {-size 12}
 ttk::style map scope -foreground {
  {active !disabled !pressed} white
  {pressed !disabled !disabled} white
  {selected !disabled !pressed} white
  } 
 }

proc ::tclmacbag::searchentry_init {{arg "none"}} {
 # Create
 switch -- [string tolower [lindex $::tcl_platform(os) 0]] {
  "windows" {
   if {[lsearch [image names] "TclMacBag.search-xp"]>=0} return
   image create photo TclMacBag.search-xp  -file [file join $::tclmacbag::basedir Resources search-xp.gif]
   }
  "darwin" { 
   if {[lsearch [image names] "TclMacBag.search-mac1"]>=0} return
   image create photo TclMacBag.search-mac1  -file [file join $::tclmacbag::basedir Resources search-mac1.gif]
   image create photo TclMacBag.search-mac2  -file [file join $::tclmacbag::basedir Resources search-mac2.gif]
   }
  default { 
   if {[lsearch [image names] "TclMacBag.search-x11"]>=0} return
   image create photo TclMacBag.search-x11  -file [file join $::tclmacbag::basedir Resources search-x11.gif]
   }
  }
 }
# The Searchentry magnifying glass is used as a default pic in various places.
image create photo TclMacBag.search-magglass -file [file join $::tclmacbag::basedir Resources search-magglass.gif]
