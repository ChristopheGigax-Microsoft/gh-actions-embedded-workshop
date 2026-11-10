#include "monitor.h"

volatile int32_t last_temperature_mc;
volatile bool alarm_active;

int main(void)
{
    monitor_t monitor;
    monitor_init(&monitor);
    for (;;) {
        /* Deterministic fixture input, not a real sensor driver. */
        last_temperature_mc = monitor_update(&monitor, 3072);
        alarm_active = monitor_alarm(last_temperature_mc, 75000);
    }
}
