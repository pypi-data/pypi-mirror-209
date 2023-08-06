package require tclmacbag


proc drawGUI {} {


    global masterlist 

    wm title . "Scopebutton Demo"

    set masterlist ""

    ttk::frame .f 
    pack .f -fill both -expand yes


    ttk::frame .f.top -padding 5
    pack .f.top -fill both -expand no

    foreach item {All Foo Bar Baz} {
	pack [tclmacbag::scopebutton .f.top.[string tolower $item]  -text $item -value $item -variable searchterm  -command {eval searchlist [list $masterlist] $searchterm}] -side left -fill x -expand no
    }

    ttk::separator .f.sep
    pack .f.sep -side top -fill both -expand no

    ttk::frame .f.bottom
    pack .f.bottom -fill both -expand yes

    tclmacbag::listbox .f.bottom.l

    set masterlist  {Foo Foo Foo Bar Bar Bar Baz Baz Baz} 

    foreach item $masterlist {
	.f.bottom.l insert end $item
    }

    pack .f.bottom.l -side bottom -fill both -expand yes

}

proc searchlist {listname searchterm} {

    global masterlist

    .f.bottom.l delete 0 end

    if {$searchterm == "All"} {
	foreach item $masterlist {
	    .f.bottom.l insert end $item
	}
	return
    } else {
	
	set parselist [lsearch -all -inline $masterlist $searchterm ]
	
	foreach item $parselist {
	    .f.bottom.l insert end $item
	}
    }
}

drawGUI