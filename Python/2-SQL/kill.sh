#!/bin/bash

while true; do
pids=$(lsof -ti tcp:5000)
if [ -n "$pids" ]; then
echo "Processes found on port 5000: $pids"
echo "Killing processes..."
kill $pids
else
echo "No processes found on port 5000"
fi
sleep 1 # Adjust the sleep time according to your needs
done
