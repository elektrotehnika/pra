# ПРА: вежбе - linux - скриптовање

## Задатак 1

Написати скрипту којој се прослеђује тачно један аргумент са командне линије. Исписати аргумент уколико је прослеђен тачно један, а у супротном обавестити корисника о неадекватном коришћењу скрипте.
    

<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash
#
# check for an argument, print a usage message if not supplied.
#
if [ $# -eq 0 ] ; then
    echo "Usage: $0 argument"
    exit 1
fi
echo $1
exit 0
```
</details>


## Задатак 2
Написати bash скрипту која захтева од корисника назив директоријума који ће бити креиран. Уколико директоријум са тим називом већ постоји, обуставити извршавање скрипте. 

Потом је потребно приступити новонасталом директоријуму, као и иштампати путању на којој се он налази. Затим, направити 4 празна фајла произвољног назива, проверити резултат позивом команде *ls*. 

У генерисане фајлове исписати произвољан садржај, а онда их све ичшитати, односно уписани садржај исписати у терминалу. За крај, почистити за собом, односно вратити се у изворни директоријум, и обрисати све креиране фајлове и поддиректоријум.

<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# Prompts the user for a directory name and then creates it  with mkdir.

echo "Uneti naziv direktorijuma:"
read NEW_DIR

# Save original directory so we can return to it (could also just use pushd, popd)

ORIG_DIR=$(pwd)

# check to make sure it doesn't already exist!

[[ -d $NEW_DIR ]] && echo $NEW_DIR already exists, aborting && exit
mkdir $NEW_DIR

# Changes to the new directory and prints out where it is using pwd.

cd $NEW_DIR
pwd

# Using touch, creates several empty files and runs ls on them to verify they are empty.

for n in 1 2 3 4
do
    touch file$n
done

ls -la file?

# (Could have just done touch file1 file2 file3 file4, just want to show do loop!)

# Puts some content in them using echo and redirection.

for names in file?
do
    echo This file is named $names > $names
done

# Displays their content using cat

echo "Sadrzaji fajlova:"

cat file?

# Says goodbye to the user and cleans up after itself
cd "$ORIG_DIR"
rm -rf $NEW_DIR

```
</details>


## Задатак 3

Написати bash скрипту унутар које су дефинисане 3 произвољне функције. Скрипта по позиву очекује кориснички унос у виду једног од бројева 1, 2, или 3; а затим позива одговарајућу функцију.

<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# Functions (must be defined before use)
func1() {
echo "Pozvana je funkcija 1"
}
func2() {
echo "Pozvana je funkcija 2"
}
func3() {
echo "Pozvana je funkcija 3"
}

# Beginning of the main script

# prompt the user to get their choice
echo "Unesite broj od 1 do 3"
read n


[[ $n != 1 ]] && [[ $n != 2 ]] && [[ $n != 3 ]] && \
    echo -e "Neophodno je uneti jedan od brojeva: [1,2,3] \nUneli ste: $n" && exit

# Call the chosen function
func$n

```
</details>

## Задатак 4

Написати bash скрипту која очекује тачно 1 параметар из командне линије. Подразумевано је прослеђена вредност параметра (аргумент при позиву функције) број између 1 и 12, а задатак скрипте је да на основу унетог редног броја у конзолу иштампа одговарајући месец у години.


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
  echo "Greska. Zahteva se broj od 1 do 12 kao argument."
  exit 1
fi

if [ $# -gt 1 ]
then
  echo "Greska. Ocekuje se tacno 1 argument."
  exit 1
fi


# set month equal to argument passed for use in the script
month=$1

################################################
# The example of a case statement:

case $month in

  1)  echo "Januar"   ;;
  2)  echo "Februar"  ;;
  3)  echo "Mart"     ;;
  4)  echo "April"     ;;
  5)  echo "Maj"       ;;
  6)  echo "Jun"      ;;
  7)  echo "Jul"      ;;
  8)  echo "Avgust"    ;;
  9)  echo "Septembar" ;;
  10) echo "Oktobar"   ;;
  11) echo "Novembar"  ;;
  12) echo "Decembar"  ;;
  *)
     echo "Greska. Nijedan mesec nije numerisan unetim brojem: $month"
     echo "Uneti broj izmedju 1 i 12."
     exit 2
     ;;
esac
exit 0

```
</details>

## Задатак 5

Написати скрипту којој се прослеђују тачно 2 аргумента са командне линије. Поменути аргументи јесу 2 стринга које је потребно упоредити. Обавестити корисника о томе који стринг је дужи, као и да ли се они поклапају.


<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# check two string arguments were given
[[ $# -lt 2 ]] && \
    echo "Potrebno je proslediti 2 stringa!" && exit 1

str1=$1
str2=$2

#------------------------------------

len1=${#str1}
len2=${#str2}
echo length of string1 = $len1, length of string2 = $len2

if [ $len1 -gt $len2 ]
then
    echo "String 1 je duzi od stringa 2"
else
    if [ $len2 -gt $len1 ]
    then
	echo "String 2 je duzi od stringa 1"
    else
	echo "String 1 i string 2 su iste duzine"
    fi
fi

## compare the two strings to see if they are the same

if [[ $str1 == $str2 ]]
then
    echo "String 1 i string 2 su isti"
else
    if [[ $str1 != $str2 ]]
    then
	echo "String 1 i string 2 nisu isti"
    fi
fi

```
</details>


## Задатак 6

Написати скрипту којој се прослеђују тачно 3 аргумента са командне линије. Нека први аргумент одговара операцији која ће се извршити над преостала 2 аргумента. Нека су дозвољене операције сабирање, одузимање, множење и дељење. Уколико је позив скрипте адекватан, иштампати резултат извршавања задате операције над прослеђеним аргументима.


<details markdown='block'>
<summary>Решење </summary>

```bash
#!/bin/bash

# Functions.  must be before the main part of the script


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
    echo "Uputstvo: Proslediti operaciju (a,s,m,d) i 2 operanda(broja)" && exit 1

[[ $op != a ]] && [[ $op != s ]] && [[ $op != d ]] && [[ $op != m ]] && \
    echo operator mora biti a, s, m, or d, nije podrzan $op  && exit 1

# ok, do the work!

case $op in 
    a) add $arg1 $arg2 ;;
    s) sub $arg1 $arg2 ;;
    m) mult $arg1 $arg2 ;;
    d) div $arg1 $arg2 ;;
    *) echo $op nije jedan od a, s, m, or d!
	exit 2 ;;
esac

# Show the answers
echo $arg1 $op $arg2 :
echo Rezultat je  $answer1

```
</details>




## Задатак 7

Написати bash скрипту коjа спаjа датотеке чиjи су називи задати као аргументи скрипте. Скрипта
прима произвољан броj параметара, али наjмање два од коjих први представља излазну датотеку,
док jедан или више преосталих параметара представљаjу улазне датотеке чиjи садржаj треба споjити.
Може се десити да неке од задатих улазних датотека не постоjе или да корисник не поседуjе дозволу
за њихово читање, па jе потребно извршити и одговараjуће провере. Спаjање датотека се врши чак
и у случаjу да неке од улазних датотека и не постоjе или су пак нечитљиве, све док постоjи макар
jедна. Уколико се деси да излазна датотека већ постоjи, споjени улазни садржаj треба додати истоj.


<details markdown='block'>
<summary>Решење </summary>

```bash
#!/usr/bin/env bash
if (($# < 2)); then
    echo "Ниjе прослеђен довољан броj (макар два) параметара." >&2
    exit 1
elif [[ -f "$1" && ! -w "$1" ]]; then
    echo "Немате дозволу за упис у постоjећу излазну датотеку." >&2
    exit 2
fi

izlaz="$1"
shift
ulaz=
for parametar in "$@"; do
    if [[ -f "$parametar" && -r "$parametar" ]]; then
        ulaz="$ulaz \"$parametar\""
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
    echo "Ниjе прослеђен довољан броj (макар два) параметара." >&2
    exit 1
elif [ -f "$1" -a ! -w "$1" ]; then
    echo "Немате дозволу за упис у постоjећу излазну датотеку." >&2
    exit 2
fi
izlaz="$1"
shift
ulaz=
for parametar in "$@"; do
    if [ -f "$parametar" -a -r "$parametar" ]; then
        ulaz="$ulaz \"$parametar\""
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