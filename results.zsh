#!/bin/zsh

for x (5 10 20 50 100 200 500 1000 2000 5000 10000)
  do
  echo "$x: $(tail -n 3 points-${x}_result.txt | head -1)"
done
