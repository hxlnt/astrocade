;; Demo 1: HELLO WORLDS
;; Assemble with zmac 1.3: zmac -o helloworlds.bin helloworlds.asm
;; 2018 hxlnt

            INCLUDE "HVGLIB.H"
            ORG     FIRSTC      ; Initialize memory address ($2000)
            DB      "U"         ; Set up cartridge
            DW      MENUST      ; Astrocade menu address
            DW      PrgName     ; Address of title for program
            DW      PrgStart    ; Entry point if user selects title on menu screen

PrgStart:   DI                  ; Initialization
            SYSTEM  (INTPC)     
            DO      (SETOUT)
            DB      $B0         
            DB      $12         ; Vertical color boundary location
            DB      00001000B
            DO      (COLSET)    ; Set color palettes
            DW      Palettes
            DO      (FILL)      ; Fill screen with background color
            DW      NORMEM      
            DW      4000D       
            DB      $00         
            DO      (STRDIS)    ; Display string on screen
            DB      29d         ; X coordinate of string
            DB      37d         ; Y coordinate of string
            DB      $0C         
            DW      PrgName     ; Address of string
            EXIT

Loop:       JP      Loop        ; Infinite loop

Palettes:   DB      $CF         ; Left palette: Color 3
            DB      $2E         ; Left palette: Color 2
            DB      $69         ; Left palette: Color 1 
            DB      $00         ; Left palette: Color 0 
            DB      $FF         ; Right palette: Color 3
            DB      $4F         ; Right palette: Color 2
            DB      $DD         ; Right palette: Color 1
            DB      $00         ; Color 0

PrgName:    DB      "HELLO, WORLDS", 0
