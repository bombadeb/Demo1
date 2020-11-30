# Repetitions solution

## Solution using AWK command 
Inside BEGIN we have used OFS to empty space that will act as the output field saperator for the rest

we have compared second item to the first item and printing it if it is not equal (We printed the first word as we are iterating from the second word)

```
awk 'BEGIN{OFS=" "}{
    printf "%s", $1
    for (i=2; i<=NF; i++) {
        if ($i != $(i-1)) {
            printf "%s%s", OFS ,$i
        }
    }
    print ""
}' input.txt > output.txt
```

## Execution steps 
```
cd 1/ && \
cat inputs/sample-input.txt | ./Repetitions.sh
```
