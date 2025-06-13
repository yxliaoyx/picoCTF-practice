PORT=12345
OUTPUT=$(nc -w 1 jupiter.challenges.picoctf.org $PORT)

c=$(echo "$OUTPUT" | grep "^c:" | cut -d' ' -f2)
n=$(echo "$OUTPUT" | grep "^n:" | cut -d' ' -f2)
e=$(echo "$OUTPUT" | grep "^e:" | cut -d' ' -f2)

RsaCtfTool -n "$n" -e "$e" --decrypt "$c"
