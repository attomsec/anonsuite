#!/bin/bash -p

clear
echo ""
echo "RAM Memory Stresser: Allocates up to 99% of available memory in 250 MB blocks, fills it with random data, and frees it after pressing Enter."
echo ""
echo "Compiling C file in: modules/c/ram_stresser.c"
gcc -o ram_stresser modules/c/ram_stresser.c
echo ""
echo "Running RAM Memory Stresser..."
./modules/c/ram_stresser