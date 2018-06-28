#include <stdio.h>

int main(void) {
    FILE *f = NULL;
    f = fopen("/var/test.txt", "w"); // returns NULL if there is an error creating the file
    putc('a', f);
    fclose(f);
}
