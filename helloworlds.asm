; Demo #1: Hello Worlds!
; 2018 hxlnt

; To assemble with zmac: zmac -o titledis.bin titledis.asm

INCLUDE     "HVGLIB.H"

ORG         FIRSTC   
DB          "U"      
DW          MENUST
DW          $PRGNAME        ; Address of title for program
DW          $PRGSTART       ; Jump here if prog is selected

$PRGNAME:   ASCII "Hello, worlds!"

$PRGSTART:  DI
            SYSTEM (INTPC)
            DO (SETOUT)
            DB $B0          ; Vertical Blanking Line
            DB $2C          ; Left/Right Color Boundary
            DB 00001000b    ; Set Bit 3 of INterrupt MODe
            DO (COLSET)
            DW $COLTAB      ; Color Table
            DO (MOVE)
            DW NORMEM       ; Destination
            DW 4000D        ; Bytes to move
            DW $BITMAP      ; Source Address
            EXIT

$LOOP:      JP $LOOP        ; Infinite loop

$COLTAB:    DB $44          ; Color 3 Left
            DB $88          ; Color 2 Left 
            DB $00          ; Color 1 Left
            DB $33          ; Color 0 Left 
            DB $66          ; Color 3 Right
            DB $99          ; Color 2 Right
            DB $CC          ; Color 1 Right
            DB $FF          ; Color 0 Right

$BITMAP:    DC 408d, 00000001b
            DC 408d, 00000010b
            DC 408d, 00000100b
            DC 408d, 00000101b
            DC 408d, 00000110b
            DC 408d, 00000111b
            DC 408d, 00001000b
            DC 408d, 00001001b
            DC 408d, 00001010b
            DC 408d, 00001011b 

