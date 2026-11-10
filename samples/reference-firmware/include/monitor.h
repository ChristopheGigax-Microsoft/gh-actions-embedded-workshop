#ifndef WORKSHOP_MONITOR_H
#define WORKSHOP_MONITOR_H

#include <stdbool.h>
#include <stdint.h>

#define MONITOR_WINDOW 4

typedef struct {
    int32_t samples[MONITOR_WINDOW];
    int32_t sum;
    uint32_t count;
    uint32_t next;
} monitor_t;

int32_t monitor_convert(uint16_t raw);
void monitor_init(monitor_t *monitor);
int32_t monitor_update(monitor_t *monitor, uint16_t raw);
bool monitor_alarm(int32_t temperature_mc, int32_t threshold_mc);

#endif
