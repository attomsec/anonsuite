#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MEMINFO_FILE "/proc/meminfo"
#define BLOCK_SIZE_MB 250

// Function to get available memory using MemAvailable
size_t get_available_memory() {
    FILE *fp = fopen(MEMINFO_FILE, "r");
    if (fp == NULL) {
        perror("Error opening /proc/meminfo");
        exit(1);
    }

    char line[256];
    size_t available_memory = 0;

    // Read the /proc/meminfo file and extract the available memory
    while (fgets(line, sizeof(line), fp)) {
        if (strstr(line, "MemAvailable:") != NULL) {
            sscanf(line, "MemAvailable: %zu kB", &available_memory);
        }
    }

    fclose(fp);

    // Calculate 98% of available memory
    return available_memory * 0.99;
}

int main() {
    size_t available_memory = get_available_memory();
    printf("Available memory (99%%): %zu kB\n", available_memory);

    // Convert from kB to bytes
    available_memory *= 1024;

    // Define block size to allocate (250 MB in bytes)
    size_t block_size = 250 * 1024 * 1024;

    unsigned char *memory;
    size_t total_allocated = 0;

    // Allocate memory in blocks of 250 MB
    while (total_allocated < available_memory) {
        size_t remaining = available_memory - total_allocated;
        size_t allocate = (remaining < block_size) ? remaining : block_size; // Allocate the smaller value between remaining and block size

        memory = (unsigned char *)malloc(allocate);
        if (memory == NULL) {
            printf("Error allocating memory! Failed after trying to allocate %zu bytes.\n", total_allocated);
            return 1;
        }

        // Fill the allocated memory with random data
        for (size_t i = 0; i < allocate; i++) {
            memory[i] = rand() % 256; // Fill with values between 0 and 255
        }

        total_allocated += allocate;

        printf("Allocated: %zu MB of memory (total: %zu MB)\n", allocate / (1024 * 1024), total_allocated / (1024 * 1024));
    }

    // Pause for visualization
    printf("Press Enter to release the memory...\n");
    getchar();

    // Free the allocated memory
    printf("Releasing the memory...\n");
    free(memory);

    // Final message
    printf("Random data written and cleaned. You are clean.\n");

    return 0;
}
