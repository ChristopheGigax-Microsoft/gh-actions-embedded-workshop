#include "monitor.h"
#include <stdio.h>

/* Required workshop exercise: temporarily expect 50001, then restore 50000. */
#define EXPECTED_MIDPOINT_MC 50000

static int failures;

static void check(const char *name, int32_t expected, int32_t actual)
{
    if (expected != actual) {
        fprintf(stderr, "%s: expected %ld, actual %ld\n",
                name, (long)expected, (long)actual);
        ++failures;
    }
}

int main(void)
{
    monitor_t monitor;
    monitor_init(&monitor);
    check("conversion minimum", 0, monitor_convert(0));
    check("conversion maximum", 100000, monitor_convert(4095));
    check("conversion clamp", 100000, monitor_convert(65535));
    check("moving average first", 0, monitor_update(&monitor, 0));
    check("moving average midpoint", EXPECTED_MIDPOINT_MC,
          monitor_update(&monitor, 4095));
    check("moving average third", 66666, monitor_update(&monitor, 4095));
    check("moving average full", 75000, monitor_update(&monitor, 4095));
    check("moving average wrap", 100000, monitor_update(&monitor, 4095));
    check("alarm below", 0, monitor_alarm(74999, 75000));
    check("alarm at", 1, monitor_alarm(75000, 75000));
    check("alarm above", 1, monitor_alarm(75001, 75000));
    return failures == 0 ? 0 : 1;
}
