from tkinter import Listbox


def listbox_dnd_package():
    """
    拖放列表框列表

    根据https://wiki.tcl-lang.org/page/Listbox+Drag-and-Drop文章修改而来
    """

    from tkinter import _default_root

    ListboxDnD = """
    namespace eval ::ListboxDnD {
        variable data;
        variable state;
}

bind ListboxDnD <1> [list ::ListboxDnD::start %W %x %y]
bind ListboxDnD <Escape> "[list ::ListboxDnD::cancel %W %x %y];break"
bind ListboxDnD <B1-Motion> [list ::ListboxDnD::drag %W %x %y]
bind ListboxDnD <ButtonRelease-1> [list ::ListboxDnD::stop %W %x %y]

# Enable listbox $lb to be re-ordered with drag and drop
# Possible args:
#        -command $cmd   -   run $cmd after the list has been rearranged, replacing %W with the window path
proc ::ListboxDnD::enable {lb {args}} {
        variable data;
        if { ![winfo exists $lb] || [winfo class $lb] ne "Listbox" } {
                return 0;
        }
        set bt [bindtags $lb]
        if { [set bti [lsearch -exact $bt "Listbox"]] < 0 } {
                return 0;
        }
        foreach {x y} $args {
                if { $x eq "-command" } {
                        if { $y eq "" } {
                                unset -nocomplain data($lb,-command)
                        } else {
                                set data($lb,-command) $y
                        }
                } else {
                        error "Invalid option $x: Must be -command"
                }
        }
        if { "ListboxDnD" in $bt } {
                return 1;# already done
        }
        bindtags $lb [linsert $bt $bti+1 "ListboxDnD"]
        return 1;
};#enable

# Called on B1 press to set up for a drag
proc ::ListboxDnD::start {lb x y} {
        variable state;
        if { [$lb cget -state] ne "normal" || [$lb cget -selectmode] ni [list "single" "multiple"] } {
                return;
        }
        
        set _listvar [$lb cget -listvariable]
        if { $_listvar eq "" } {
                return;
        }
        upvar #0 $_listvar listvar
        if { ![info exists listvar] || [llength $listvar] < 2 } {
                return;
        }
        
        set state($lb,list) $listvar
        set state($lb,startindex) [$lb index @$x,$y]
        set state($lb,currindex) $state($lb,startindex)
        set state($lb,startsel) [$lb curselection]
        
        return;
};# start

# Called on B1 motion, as an item is being dragged
proc ::ListboxDnD::drag {lb x y} {
        variable state;
        
        set _listvar [$lb cget -listvariable]
        if { $_listvar eq "" || ![info exists state($lb,list)] } {
                return;
        }
        upvar #0 $_listvar listvar
        
        set newpos [$lb nearest $y]
        set oldpos $state($lb,currindex)
        if { $newpos == $oldpos } {
                return;
        }
        set sel [$lb curselection]
        if { $oldpos in $sel && $newpos ni $sel } {
                $lb selection clear $oldpos
                $lb selection set $newpos
        } elseif { $oldpos ni $sel && $newpos in $sel } {
                $lb selection clear $newpos
                $lb selection set $oldpos
        }
        set newlist $listvar
        set oldval [lindex $newlist $oldpos]
        set newval [lindex $newlist $newpos]
        set newlist [lreplace $newlist $oldpos $oldpos $newval]
        set newlist [lreplace $newlist $newpos $newpos $oldval]
        set listvar $newlist
        set state($lb,currindex) $newpos

        return;
};# drag

# Called when Escape is pressed; cancel a drag
proc ::ListboxDnD::cancel {lb x y} {
        variable state;
        
        if { ![info exists state($lb,list)] } {
                return;
        }
        
        set _listvar [$lb cget -listvariable]
        if { $_listvar eq "" } {
                return;
        }
        upvar #0 $_listvar listvar
        set listvar $state($lb,list)
        $lb selection clear 0 end
        foreach x $state($lb,startsel) {
                $lb selection set $x
        }
        
        array unset state $lb,*
        
        return;
};# cancel

# Called on B1 release; finalise a drag
proc ::ListboxDnD::stop {lb x y} {
        variable state;
        variable data;
        
        if { ![info exists state($lb,startindex)] } {
                return; # drag was cancelled
        }
        
        set start $state($lb,startindex)
        set curr $state($lb,currindex)
        array unset state $lb,*
        if { $start == $curr } {
                return;# Wasn't dragged anyway
        }
                
        if { [info exists data($lb,-command)] } {
                catch {uplevel #0 [string map [list %W $lb] $data($lb,-command)]}
        }
        
        return;
};# stop

package provide ListboxDnD 1.0
    """

    _default_root.eval(ListboxDnD)


def listbox_dnd_enable(listbox: Listbox):
    """
    启用拖放列表框列表

    根据https://wiki.tcl-lang.org/page/Listbox+Drag-and-Drop文章修改而来

    Attributes:
        listbox (Listbox): 选择目标列表框
    """

    from tkinter import _default_root

    _default_root.eval("package require ListboxDnD")

    _default_root.eval(f"ListboxDnD::enable {listbox}")


def window_dnd():
    """
    无边框窗口拖放

    根据https://wiki.tcl-lang.org/page/Drag+and+Drop+a+Window文章修改而来
    """

    from tkinter import _default_root

    dndwin = """
    ##########################################################
    # Name:  dndwin.tcl
    # Author: Martin Eder, snofix@users.sourceforge.net
    # Description: A toplevel window without window decoration
    #         that can be moved by drag-and-drop
    ##########################################################
    
    package require Tk
    
    variable xoff
    variable yoff
    
    proc move {x y} {
        set xpos [expr $x - $::xoff]
        set ypos [expr $y - $::yoff]
        wm geometry . "+$xpos+$ypos"
    }
    
    proc gui {} {
        ### Create some GUI    
        . configure -padx 5 -pady 5 -relief ridge -borderwidth 4
        label .llab -text "Use drag-and-drop\nto move this window"
        button .bexit -text "Exit" -command exit
        button .babout -text "About"  -command about
        pack .llab -padx 10 -pady 10
        pack .bexit .babout -padx 10 -pady 10 -side left -expand 1
    }
    
    proc init {} {
        ### Hide the Window Decoration
        wm overrideredirect . true
        
        ### DnD Binding
        bind . <ButtonPress-1> {
            set ::xoff [expr %X - [winfo rootx .]]
            set ::yoff [expr %Y - [winfo rooty .]]
        }
        bind . <B1-Motion> [list move %X %Y]    
    }
    
    proc about {} {
        wm withdraw .
        tk_messageBox -title "About" -message "DnD Toplevel\n2006 by Martin Eder\n(snofix@users.sourceforge.net)"
        wm deiconify .
    }
    
    init
    ### End of Script

    """

    _default_root.eval(dndwin)
