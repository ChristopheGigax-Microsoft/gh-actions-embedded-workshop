/* Author-only analyzer negative case. Never compile, run, or link into firmware. */
int analyzer_negative_case(void)
{
    int *value = 0;
    return *value;
}
