awk 'BEGIN{OFS=" "}{
    printf "%s", $1
    for (i=2; i<=NF; i++) {
        if ($i != $(i-1)) {
            printf "%s%s", OFS ,$i
        }
    }
    print ""
}'
