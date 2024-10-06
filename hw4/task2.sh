# Part A:
grep -c "sample" dataset1/file* | 
grep -E ":[1-9]+[0-9]*$" | 
cut -d: -f1 | 
xargs grep -o "CSC510" | 
uniq -c | 
grep -E -v "^\s*[1-2] dataset1/file" | 
cut -d: -f1 | 
# Part B:
gawk '{system("ls -l "$2 "| xargs echo "$1 ) }' | 
sort -k1,1nr -k6,6nr | 
gawk '{print $10}' | 
cut -d/ -f2 |
# Part C:
sed 's/file/filtered/g'