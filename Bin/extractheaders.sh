#extracts the line numbers that have the word "DATA follow with format" (at end of each header)
#and cuts out the line numbers to save 
grep -E -n "DATA follow with format" $1 | cut -f 1 -d ":" > $2 