grep -E '^([^,]*,[^,]*,2,)' titanic.csv | 
grep -E ',S\s' | 
sed 's/female/F/; s/male/M/'| 
gawk -F, 'NR > 0 && $7 != "" { sum += $7; count++; print $0} END { if (count > 0) print "Average age: ", sum / count; else print "No valid ages" }' > outputTask3.txt