#!/bin/bash

read -p "Enter year: " year

if [ ! -d /home/tom/advent-of-code/${year} ]; then
    mkdir -p /home/tom/advent-of-code/${year};
fi

cd /home/tom/advent-of-code/${year}

read -p "Enter day: " day

if [ ! -d /day-${day} ]; then
    mkdir -p day-${day};
fi

cd day-${day}

if [ ! -f day-${day}.py ]; then
    touch day-${day}.py;
fi

if [ ! -f input.txt ]; then
    touch input.txt;
fi





