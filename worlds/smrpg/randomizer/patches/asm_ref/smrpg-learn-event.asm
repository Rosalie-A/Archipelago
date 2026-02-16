; SMRPG new event command - Learn special ability
; Author: Abyssonym
; Date: 2026/02/01
; Assembler: Asar 1.91 - https://github.com/RPGHacker/asar
; This patch replaces an existing opcode ($ce by default).
; The new command takes one 1-byte parameter, masked as follows:
;    $1f - Special to learn (up to $1a-Star Rain)
;    $e0 - Character to learn it (up to $04-Mallow)

hirom

!debug_enabled = 0

; The opcode that we are replacing with our custom special-learning command
!opcode = $ce

!script_handler_addr = $c03e93
!command_pointers_addr = $c0c6a5
!bit_selector_addr = $c2e555
!specials_learned_addr = $7ff810

!c0_freespace_addr = $c08130        ; Overwrites antipiracy message
!hook_freespace_addr = $fa20b0      ; Partitions used to be here. Change if needed.

org !command_pointers_addr+(!opcode*2)
    dw !c0_freespace_addr

org !c0_freespace_addr
    jsl !hook_freespace_addr
    jmp.w !script_handler_addr

org !hook_freespace_addr
    ; $0000,Y - Address of event command parameters
    ; Takes one 1-byte parameter, masked as follows:
    ;    $1f - Special to learn
    ;    $e0 - Character to learn it
    ; Special data is at: $7ff810+(C*$14)
    ; Special data is 4 bytes long (bitmap up to $1a - Star Rain)
    ; Therefore the byte offset is at (C*$14)+(S>>3)
    phy             ; Save script pointer
    rep #$20
    lda $0000,y
    and #$00ff
    pha             ; Push command parameter
    lsr #5
    pha             ; Push character index
    asl #2          ; Multiply by $04: C*4
    clc
    adc $01,s       ; Multiply by $05: (C*4)+C
    asl #2          ; Multiply by $14: ((C*4)+C)*4
    sta $01,s       ; Save character offset
    lda $0000,y
    and #$001f      ; Get special index
    lsr #3          ; Get special offset
    clc
    adc $01,s       ; Add special offset + character offset = byte offset
    tay
    pla             ; Consume character offset
    pla             ; Get command parameter
    sep #$20
    and #$07        ; Get bit number
    tax             ; Offset of corresponding bit mask
    lda.l !bit_selector_addr,x
    tyx             ; Byte offset
    ora.l !specials_learned_addr,x
    sta.l !specials_learned_addr,x
    ply             ; Restore script pointer
    iny             ; Advance script pointer
    rtl

if !debug_enabled == 1
    !test_character = $03   ; Geno
    !test_special = $1a     ; Star Rain
    org $defa16
        ; Mario's lamp event
        db !opcode
        db (!test_character<<5)|!test_special 
        db $fe      ; End event
endif