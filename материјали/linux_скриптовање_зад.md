# ПРА: Linux скриптовање - задаци за вежбање

## Задатак 1

Написати bash скрипту којој се прослеђује тачно један аргумент са командне линије. Исписати аргумент уколико је прослеђен тачно један, а у супротном обавестити корисника о неадекватном коришћењу скрипте.
    

<details markdown='block'>
<summary>Решење </summary>

```bash
#!/usr/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Неисправно коришћење."
    echo "Очекивано: $0 аргумент1"
    exit 1
fi
echo $1
```
</details>


## Задатак 2
Написати bash скрипту која захтева од корисника назив директоријума који ће бити креиран. Уколико директоријум са тим називом већ постоји, обуставити извршавање скрипте. 

Потом је потребно приступити новонаправљеном директоријуму, као и исписати путању на којој се он налази. Затим, направити 4 празне датотеке произвољног назива, проверити резултат позивом наредбе `ls`. 

У направљене датотеке уписати произвољан садржај, а онда их све ишчитати, односно уписани садржај исписати у терминалу (на стандардни излаз). За крај, почистити за собом, односно вратити се у изворни директоријум, и обрисати све направљене датотеке и поддиректоријум.

<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# Prompts the user for a directory name and then creates it  with mkdir.

echo "Унети назив директоријума: "
read NEW_DIR

# Save original directory so we can return to it (could also just use pushd, popd)

ORIG_DIR=$(pwd)

# check to make sure it doesn't already exist!

[[ -d $NEW_DIR ]] && echo $NEW_DIR већ постоји. Извршавање се прекида... && exit
mkdir $NEW_DIR

# Changes to the new directory and prints out where it is using pwd.

cd $NEW_DIR
pwd

# Using touch, creates several empty files and runs ls on them to verify they are empty.

for n in 1 2 3 4
do
    touch датотека$n
done

ls -la датотека?

# (Could have just done touch датотека1 датотека2 датотека3 датотека4, just want to show do loop!)

# Puts some content in them using echo and redirection.

for name in датотека?
do
    echo Назив ове датотеке је $name > $name
done

# Displays their content using cat

echo "Садржаји датотека:"

cat датотека?

# Says goodbye to the user and cleans up after itself
cd "$ORIG_DIR"
rm -rf $NEW_DIR

```
</details>


## Задатак 3

Написати bash скрипту унутар које су дефинисане 3 произвољне функције. Скрипта по позиву очекује кориснички унос у виду једног од бројева 1, 2, или 3, а затим позива одговарајућу функцију.

<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# Functions (must be defined before use)
func1() {
echo "Позвана је функција 1"
}
func2() {
echo "Позвана је функција 2"
}
func3() {
echo "Позвана је функција 3"
}

# Beginning of the main script

# prompt the user to get their choice
echo "Унесите број од 1 до 3: "
read n

[[ $n != 1 ]] && [[ $n != 2 ]] && [[ $n != 3 ]] && \
    echo -e "Погрешан унос! Неопходно је унети један од бројева: 1,2,3 \nУнели сте: $n" && exit

# Call the chosen function
func$n

```
</details>

## Задатак 4

Написати bash скрипту која очекује тачно један аргумент са командне линије. Потребно је да прослеђени аргумент буде број између 1 и 12, а задатак скрипте је да, на основу унетог броја, на стандардни излаз испише одговарајући месец у години.


<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# Accept a number between 1 and 12 as
# an argument to this script, then return the
# the name of the month that corresponds to that number.

# Check to see if the user passed a parameter.
if [ $# -eq 0 ]
then
  echo "Грешка! Потребно је унети број од 1 до 12 као аргумент."
  exit 1
fi

if [ $# -gt 1 ]
then
  echo "Грешка! Очекује се тачно један аргумент."
  exit 1
fi


# set month equal to argument passed for use in the script
month=$1

################################################
# The example of a case statement:

case $month in

  1)  echo "Јануар"   ;;
  2)  echo "Фебруар"  ;;
  3)  echo "Март"     ;;
  4)  echo "Април"     ;;
  5)  echo "Мај"       ;;
  6)  echo "Јун"      ;;
  7)  echo "Јул"      ;;
  8)  echo "Август"    ;;
  9)  echo "Септембар" ;;
  10) echo "Октобар"   ;;
  11) echo "Новембар"  ;;
  12) echo "Децембар"  ;;
  *)
     echo "Грешка! Ниједан месец није нумерисан унетим бројем: $month"
     echo "Потребно је унети број између 1 и 12."
     exit 2
     ;;
esac
exit 0

```
</details>

## Задатак 5

Написати bash скрипту којој се прослеђују тачно два аргумента са командне линије. Поменути аргументи јесу два стринга које је потребно упоредити. Обавестити корисника о томе који стринг је дужи, као и да ли се они поклапају.


<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# check two string arguments were given
[[ $# -lt 2 ]] && \
    echo "Грешка! Потребно је проследити два стринга." && exit 1

str1=$1
str2=$2

#------------------------------------

len1=${#str1}
len2=${#str2}
echo Дужина првог стринга је $len1. Дужина другог стринга је $len2.

if [ $len1 -gt $len2 ]
then
    echo "Први стринг је дужи од другог."
else
    if [ $len2 -gt $len1 ]
    then
	echo "Други стринг је дужи од првог."
    else
	echo "Оба стринга су исте дужине."
    fi
fi

## compare the two strings to see if they are the same

if [[ $str1 == $str2 ]]
then
    echo "Унети стрингови су идентични."
else
    if [[ $str1 != $str2 ]]
    then
	echo "Унети стрингови се разликују."
    fi
fi

```
</details>


## Задатак 6

Написати bash скрипту којој се прослеђују тачно три аргумента са командне линије. Нека први аргумент одговара операцији која ће се извршити над преостала два аргумента. Нека су дозвољене операције сабирање, одузимање, множење и дељење. Уколико је позив скрипте адекватан, исписати резултат извршавања задате операције над прослеђеним аргументима.


<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# Functions. Must be before the main part of the script

add() {
    answer=$(($1 + $2))
}
sub() {
    answer=$(($1 - $2))
}
mult() {
    answer=$(($1 * $2))
}
div() {
    answer=$(($1 / $2))
}
# End of functions
#

# Main part of the script

# need 3 arguments, and parse to make sure they are valid types

op=$1 ; arg1=$2 ; arg2=$3

[[ $# -lt 3 ]] && \
    echo "Погрешан унос! Унети три аргумента. Први треба бити операција (a,s,m,d), а наредна два бројеви над којима ће се операција извршити." && exit 1

[[ $op != a ]] && [[ $op != s ]] && [[ $op != d ]] && [[ $op != m ]] && \
    echo Оператор мора бити a, s, m, или d. Оператор $op није подржан! && exit 1

# ok, do the work!

case $op in 
    a) add $arg1 $arg2 ;;
    s) sub $arg1 $arg2 ;;
    m) mult $arg1 $arg2 ;;
    d) div $arg1 $arg2 ;;
    *) echo Оператор $op није један од: a, s, m, или d!
	exit 2 ;;
esac

# Show the answers
echo $arg1 $op $arg2 :
echo Резултат је $answer.

```
</details>




## Задатак 7

Написати bash скрипту коjа спаjа датотеке чиjи су називи задати као аргументи скрипте. Скрипта прима произвољан броj аргумената, али наjмање два, од коjих први представља излазну датотеку, док jедан или више преосталих аргумената представљаjу улазне датотеке чиjи садржаj треба споjити и уписати у датотеку прослеђену као први аргумент. Требало би проверити постојање излазне датотеке и могућност уписа у исту. Такође, може се десити да неке од задатих улазних датотека не постоjе или да корисник не поседуjе дозволу за њихово читање. Спаjање датотека се врши чак и у случаjу да неке од улазних датотека и не постоjе или су пак нечитљиве, све док постоjи макар jедна. Уколико се деси да излазна датотека већ постоjи, споjени улазни садржаj треба додати истоj.


<details markdown='block'>
<summary>Решење </summary>

```bash
#!/usr/bin/env bash
if (($# < 2)); then
    echo "Ниjе прослеђен довољан броj (макар два) аргумената." >&2
    exit 1
elif [[ -f "$1" && ! -w "$1" ]]; then
    echo "Немате дозволу за упис у постоjећу излазну датотеку." >&2
    exit 2
fi

izlaz="$1"
shift
ulaz=
for argument in "$@"; do
    if [[ -f "$argument" && -r "$argument" ]]; then
        ulaz="$ulaz \"$argument\""
    fi
done

if [[ -n "$ulaz" ]]; then
    eval "cat $ulaz" >> "$izlaz"
else
    echo "Не постоjи ниjедна читљива улазна датотека." >&2
    exit 3
fi
#или

#!/usr/bin/env bash
if [ $# -lt 2 ]; then
    echo "Ниjе прослеђен довољан броj (макар два) аргумената." >&2
    exit 1
elif [ -f "$1" -a ! -w "$1" ]; then
    echo "Немате дозволу за упис у постоjећу излазну датотеку." >&2
    exit 2
fi
izlaz="$1"
shift
ulaz=
for argument in "$@"; do
    if [ -f "$argument" -a -r "$argument" ]; then
        ulaz="$ulaz \"$argument\""
    fi
done
if [ -n "$ulaz" ]; then
    eval "cat $ulaz" >> "$izlaz"
else
    echo "Не постоjи ниjедна читљива улазна датотека." >&2
    exit 3
fi
```
</details>
