                                ; Demo 1: HELLO, WORLDS! / 2018 hxlnt
                                ; Assemble with Zmac 1.3

INCLUDE "HVGLIB.H"              ; Include HVGLIB library

            ORG    FIRSTC       ; Initialize at beginning of cartridge ROM area
            DB     "U"          ; ... with the code for a normal menued cartridge
            DW     MENUST       ; Initialize menu
            DW     PrgName      ; ... with string at PrgName
            DW     PrgStart     ; ... such that selecting the program enters PrgStart
PrgName:    DB     "HELLO, WORLDS!", $00
PrgStart:   DI                  ; Disable interrupts
            SYSTEM (INTPC)      ; Begin interpreter mode
            DO     (SETOUT)     ; Set output ports
            DB     $B0          ; ... with VBLANK line set to $B0
            DB     112d/4       ; ... with color boundary 112 pixels from the left of the screen
            DB     00001000b    ; ... with screen interrupts reenabled 
            DO     (COLSET)     ; Set color palettes
            DW     Palettes     ; ... with the values at Palettes
            DO     (FILL)       ; Set background fill
            DW     NORMEM       ; ... starting at the beginning of screen RAM
            DW     10d*BYTEPL   ; ... and going for 16 lines
            DB     00011011b    ; ... with a fill pattern of four different colored pixels
            DO     (STRDIS)     ; Set string display
            DB     0d           ; ... starting 0 pixels from the left of the screen
            DB     37d          ; ... and 37 pixels from the top of the screen
            DB     00001100b    ; ... with no enlargement, foreground color = 11, background color = 00          
            DW     PrgName      ; ... to show string at PrgName
            EXIT                ; Exit interpreter mode
Loop:       JP     Loop         ; Play infinite loop
Palettes:   DB     $BF, $00, $00, $00
            DB     $E7, $9A, $39, $19
