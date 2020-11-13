#!/bin/bash
sh ./deps.sh
chmod +x ./run
chmod +x ./word
for x in {1..5};do
pdir="./files_$(./word $x)"
dirs=()
files=()
ext="txt"
dirs+=("$pdir")
for n in {1..5};do
num=$(./word $n)
dirs+=("$pdir/$num")
files+=("$num.$ext")
done
rm -rf $pdir
c=1
for d in "${dirs[@]}";do
mkdir $d
for f in "${files[@]}";do
p="$d/$f"
n=$(./word $c)
echo -e "\nfile number $n">$p
let c++
done
done
done
echo -e "Done!!!\nrun './run' to start"