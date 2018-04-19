read number1
read number2

echo $((number1 + number2))
echo $[number1 - number2]
echo `expr $number1 \* $number2`
echo $((number1 / number2))
