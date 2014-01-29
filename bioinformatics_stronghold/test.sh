FILE="rosalind_$1.txt"
python "$1.py" < "rosalind_$1.txt" | tee "rosalind_$1.out"
