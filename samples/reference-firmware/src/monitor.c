#include "monitor.h"

int32_t monitor_convert(uint16_t raw)
{
    uint32_t bounded = raw > 4095U ? 4095U : raw;
    return (int32_t)((bounded * 100000U) / 4095U);
}

void monitor_init(monitor_t *monitor)
{
    monitor->sum = 0;
    monitor->count = 0;
    monitor->next = 0;
    for (uint32_t i = 0; i < MONITOR_WINDOW; ++i) {
        monitor->samples[i] = 0;
    }
}

int32_t monitor_update(monitor_t *monitor, uint16_t raw)
{
    int32_t value = monitor_convert(raw);
    monitor->sum -= monitor->samples[monitor->next];
    monitor->samples[monitor->next] = value;
    monitor->sum += value;
    monitor->next = (monitor->next + 1U) % MONITOR_WINDOW;
    if (monitor->count < MONITOR_WINDOW) {
        ++monitor->count;
    }
    return monitor->sum / (int32_t)monitor->count;
}

bool monitor_alarm(int32_t temperature_mc, int32_t threshold_mc)
{
    return temperature_mc >= threshold_mc;
}
