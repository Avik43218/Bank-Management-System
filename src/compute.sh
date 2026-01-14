!/bin/bash

FILE_NAME="$1"
UNIQUE_ID="$2"

shift 2
cd ..
cd cpp/

g++ -o "${FILE_NAME%.*}" "$FILE_NAME"

touch "$UNIQUE_ID".dat
exec "./${FILE_NAME%.*}" "$@"
