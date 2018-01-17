                                ; Demo 1: HELLO WORLDS / 2018 hxlnt
                                ; Assemble with Zmac 1.3

            INCLUDE "HVGLIB.H"
            ORG    FIRSTC       ; Initialize memory address ($2000)
            DB     "U"          ; Set up cartridge
            DW     MENUST       ; Astrocade menu address
            DW     PrgName      ; Address of title for program
            DW     PrgStart     ; Entry point if user selects title on menu screen
PrgName:    DB     "HELLO, WORLDS!"
            DB     $00
PrgStart:   DI                  ; Initialization
            SYSTEM (INTPC)
            DO     (SETOUT)
            DB     $B0       
            DB     $1C          ; Vertical color boundary location
            DB     $08      
            DO     (COLSET)
            DW     Palettes     ; Set color palettes
            DO     (FILL)       ; Fill background with a tile
            DW     NORMEM       
            DW     4000D        
            DB     01000100B    ; Background tile to repeat
            DO     (STRDIS)
            DB     0D           ; X coordinate
            DB     37D          ; Y coordinate
            DB     $0C          
            DW     PrgName      ; Address of string to display
            EXIT
Loop:       JP     Loop         ; Infinite loop
Palettes:   DB     $BF          ; Left palette: Color 3
            DB     $00          ; Left palette: Color 2
            DB     $00          ; Left palette: Color 1
            DB     $00          ; Left palette: Color 0
            DB     $E7          ; Right palette: Color 3
            DB     $9A          ; Right palette: Color 2
            DB     $39          ; Right palette: Color 1
            DB     $19          ; Right palette: Color 0
