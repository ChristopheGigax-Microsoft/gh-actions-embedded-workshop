cmake_minimum_required(VERSION 3.25)
project(workshop_monitor VERSION 1.0.0 LANGUAGES C)

option(BUILD_FIRMWARE "Build the reference Arm image instead of host tests" OFF)
option(QUALITY_GATES "Enable extra warnings and native coverage" OFF)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

add_library(monitor STATIC src/monitor.c)
target_include_directories(monitor PUBLIC include)

if(QUALITY_GATES)
  if(NOT CMAKE_C_COMPILER_ID STREQUAL "GNU")
    message(FATAL_ERROR "The reference quality preset requires native GCC/gcov; adapt it for your compiler.")
  endif()
  target_compile_options(monitor PRIVATE -Wall -Wextra -Wpedantic -Werror)
  if(NOT BUILD_FIRMWARE)
    target_compile_options(monitor PUBLIC --coverage -O0 -g)
    target_link_options(monitor PUBLIC --coverage)
  endif()
endif()

if(BUILD_FIRMWARE)
  enable_language(ASM)
  add_executable(firmware platform/startup.S platform/main.c)
  target_link_libraries(firmware PRIVATE monitor)
  target_compile_options(monitor PRIVATE -mcpu=cortex-m3 -mthumb -ffreestanding -fno-builtin -ffunction-sections -fdata-sections -Os)
  target_compile_options(firmware PRIVATE -mcpu=cortex-m3 -mthumb -ffreestanding -fno-builtin -ffunction-sections -fdata-sections -Os)
  target_link_options(firmware PRIVATE
    -mcpu=cortex-m3 -mthumb -nostdlib
    "-T${CMAKE_CURRENT_SOURCE_DIR}/platform/memory.ld"
    "-Wl,-Map=${CMAKE_BINARY_DIR}/monitor.map"
    -Wl,--gc-sections -Wl,--build-id=none)
  set_target_properties(firmware PROPERTIES OUTPUT_NAME monitor SUFFIX .elf
    LINK_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/platform/memory.ld")
  add_custom_command(TARGET firmware POST_BUILD
    COMMAND "${CMAKE_OBJCOPY}" -O binary "$<TARGET_FILE:firmware>" "${CMAKE_BINARY_DIR}/monitor.bin"
    COMMAND "${CMAKE_SIZE}" "$<TARGET_FILE:firmware>"
    BYPRODUCTS "${CMAKE_BINARY_DIR}/monitor.bin"
    VERBATIM)
else()
  enable_testing()
  add_executable(test_monitor tests/test_monitor.c)
  target_link_libraries(test_monitor PRIVATE monitor)
  if(QUALITY_GATES)
    target_compile_options(test_monitor PRIVATE -Wall -Wextra -Wpedantic -Werror)
  endif()
  add_test(NAME monitor_logic COMMAND test_monitor)
endif()
