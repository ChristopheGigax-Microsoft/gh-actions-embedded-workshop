/* Reference Cortex-M3 map only; replace for the customer's actual target. */
ENTRY(Reset_Handler)
MEMORY
{
    FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 128K
    RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 20K
}
__stack_top = ORIGIN(RAM) + LENGTH(RAM);
SECTIONS
{
    .isr_vector : { KEEP(*(.isr_vector)) } > FLASH
    .text : { *(.text*) *(.rodata*) . = ALIGN(4); } > FLASH
    .ARM.exidx : { *(.ARM.exidx*) } > FLASH
    .data : {
        . = ALIGN(4);
        __data_start = .;
        *(.data*)
        . = ALIGN(4);
        __data_end = .;
    } > RAM AT > FLASH
    __data_load = LOADADDR(.data);
    .bss (NOLOAD) : {
        . = ALIGN(4);
        __bss_start = .;
        *(.bss*) *(COMMON)
        . = ALIGN(4);
        __bss_end = .;
    } > RAM
    ASSERT(__bss_end <= __stack_top - 1024, "Reference RAM leaves less than 1 KiB for stack")
}
