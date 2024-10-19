# ПРА: вежбе - увод у Linux

## Задатак 1
Креирати директоријум са називом Moj Direktorijum.

<details markdown='block'>
<summary>Решење </summary>

```bash
#пазити на размак као карактер!
mkdir "Moj Direktorijum"
```
</details>


## Задатак 2
Додати Documents директоријум у PATH променљиву.

<details markdown='block'>
<summary>Решење </summary>

```bash
cd Documents
PATH=$PATH:$PWD
```
</details>

## Задатак 3

Креирати 3 фајла названа редом pra1.txt pra2.txt pra3.txt.

Уписати у сваки од фајлова по један ред.

Креирати четврти фајл са садржајем претходна 3.


<details markdown='block'>
<summary>Решење </summary>

```bash
echo sadrzaj1 > file1
echo sadrzaj2 > file2
echo sadrzaj3 > file3
cat file1 file2 file3 > file4
```
</details>

## Задатак 4
Креирати фајл и онемогућити његово читање и промену за све осим за власника фајла. Извршавање фајла забранити за све кориснике.

<details markdown='block'>
<summary>Решење </summary>

```bash
touch file
sudo chmod 600 file
```
</details>

## Задатак 5
Креирати фајл fin.txt са текстом:

*Електротехника и рачунарство то су срца два.*

Користити садржај овог фајла за прављење новог који садржи три пута поновљен садржај fin.txt фајла.
<details markdown='block'>
<summary>Решење </summary>

```bash
echo Електротехника и рачунарство то су срца два. > fin.txt
cat fin.txt fin.txt fin.txt > newFile
```
</details>

<br>

<br>

<br>


# Задатак 6

## Задатак 6.1
Овај задатак ће обухватити манипулацију фајловима и директоријумима, а подразумева сређивање ваше фиктивне колекције уметничког садржаја. Најпре креирајте фолдер за вежбање (рецимо да се зове баш *Vezbanje*), нека се налази у вашем "кућном" директоријуму. Пожељно је проверавати резултате акција употребом команде **ls**.

<details markdown='block'>
<summary>Решење </summary>

```bash
cd
pwd
```

```bash
ls
```

```bash
mkdir Vezbanje
ls
```
</details>




## Задатак 6.2

Рецимо да у вашој колекцији имате песме, филмове, као и фотографије. У оквиру директоријума за вежбу, креирати по 6 нумерисаних фајлова сваког типа, чије су екстензије редом
.mp3, .mp4, .jpg.

<details markdown='block'>
<summary>Решење </summary>

```bash
cd Vezbanje
touch pesma1.mp3 pesma2.mp3 pesma3.mp3 pesma4.mp3 pesma5.mp3 pesma6.mp3
touch film1.mp4 film2.mp4 film3.mp4 film4.mp4 film5.mp4 film6.mp4
touch foto1.jpg foto2.jpg foto3.jpg foto4.jpg foto5.jpg foto6.jpg
ls -l
```
</details>

<details markdown='block'>
<summary>Решење - незнатно компактнија варијанта</summary>

```bash
cd Vezbanje
touch pesma{1..6}.mp3 film{1..6}.mp4 foto{1..6}.jpg
ls -l
```
</details>

## Задатак 6.3

Ваша колекција је сада пуна разноврсног садржаја, али је поприлично неуредна. Направите одвојене под-директоријуме и адекватно распоредите одговарајући садржај. Нека се директоријуми зову рецимо Muzika, Filmovi, Slike.

<details markdown='block'>
<summary>Решење </summary>

```bash
mkdir Muzika
mkdir Filmovi
mkdir Slike
ls -l
```
```bash
mv pesma1.mp3 pesma2.mp3 pesma3.mp3 pesma4.mp3 pesma5.mp3 pesma6.mp3 Muzika
mv film1.mp4 film2.mp4 film3.mp4 film4.mp4 film5.mp4 film6.mp4 Filmovi
mv foto1.jpg foto2.jpg foto3.jpg foto4.jpg foto5.jpg foto6.jpg Slike
ls -l
```
</details>




<details markdown='block'>
<summary>Решење - незнатно компактнија варијанта</summary>

```bash
mkdir Muzika Filmovi Slike
ls -l
```
```bash
mv *.mp3 Muzika
mv *.mp4 Filmovi
mv *.jpg Slike
ls -l
```
</details>

## Задатак 6.4

Ваша колекција је знатно боље организована сада, али какав сте Ви колекционар ако своје богатство не поделите са осталима? Планирате да познаницима пошаљете неке садржаје, али нису сви истог приоритета. Наиме, идеја је да различит садржај добију ваши пријатељи, породица и колеге са посла. С тим у вези, креирајте 3 под-директоријума, нека се зову рецимо Porodica, Prijatelji, Kolege. Коначно, извршите расподелу садржаја копирањем из основних у новостворене под-директоријуме, фајлови нумерисани бројевима 1 и 2 су намењени за породицу, 3 и 4 за пријатеље, и коначно, 5 и 6 сте резервисали за колеге.

<details markdown='block'>
<summary>Решење </summary>

```bash
mkdir Porodica Prijatelji Kolege
ls -l
```
```bash
cp Filmovi/film1.mp4 Filmovi/film2.mp4 Slike/foto1.jpg Slike/foto2.jpg Muzika/pesma1.mp3 Muzika/pesma2.mp3 Porodica
cp Filmovi/film3.mp4 Filmovi/film4.mp4 Slike/foto3.jpg Slike/foto4.jpg Muzika/pesma3.mp3 Muzika/pesma4.mp3 Prijatelji
cp Filmovi/film5.mp4 Filmovi/film6.mp4 Slike/foto5.jpg Slike/foto6.jpg Muzika/pesma5.mp3 Muzika/pesma6.mp3 Kolege
```
</details>

<details markdown='block'>
<summary>Решење - незнатно компактнија варијанта</summary>

```bash
mkdir Porodica Prijatelji Kolege
ls -l
```
```bash
find . -type f -regex '.*[12]\..*' -exec cp --no-clobber {} Porodica/ \;
find . -type f -regex '.*[34]\..*' -exec cp --no-clobber {} Prijatelji/ \;
find . -type f -regex '.*[56]\..*' -exec cp --no-clobber {} Kolege/ \;
```
</details>



## Задатак 6.5

Ваше добро дело је пропагирало до драгих вам особа, међутим, нису сви одушевљени вашом колекцијом, чак већина има озбиљне замерке на ваше деловање, а добро је познато да би сви волели бити критичари. Изреволтирани, одлучујете обрисати све под-директоријуме намењене дељењу са породицом, пријатељима и колегама. За бонус "поене": употребити команду *rmdir*.

<details markdown='block'>
<summary>Решење</summary>

```bash
rm -r Porodica Prijatelji Kolege
ls -l
```
</details>

<details markdown='block'>
<summary>Решење - знатно некомпактнија варијанта</summary>

```bash
cd Porodica
rm -r *
cd ../Prijatelji
rm -r *
cd ../Kolege
rm -r *
cd ..
rmdir Porodica Prijatelji Kolege
ls -l
```
</details>

## Задатак 6.6

За крај овог задатка, уносом путем тастатуре забележите поруку коју остављате свету, а онда је сачувајте као садржај фајла унутар директоријума Vezbanje, нека се фајл зове рецимо text.poruka.

<details markdown='block'>
<summary>Решење</summary>

```bash
cat - > text.poruka
```
</details>



<br>

<br>

<br>


# Задатак 7

## Задатак 7.1

За потребе овог задатка ставите се у позицију професора на предмету ПРА (први и једини предуслов - не можете сами себи уписати оцену). Потребно је да организујете права приступа систему за сараднике на предмету - Филипа, Исидору, Лазара. Направите корисничку групу saradnici, а потом и појединачне корисничке налоге за Филипа, Исидору и Лазара. За сваки налог подесите шифру за налог по слободној вољи, и додајте креиране налоге у групу saradnici.

<details markdown='block'>
<summary>Решење</summary>

```bash
sudo su -
#ukucati sifru korisnika kako biste pristupili shellu kao root korisnik
#u novom promptu BI TREBALO da pise root@hostname i na kraju # umesto uobicajenog $
groupadd saradnici
useradd -G saradnici filip
useradd -G saradnici isidora
useradd -G saradnici lazar
```

```bash
passwd filip
#unesite DVA puta sifru za korisnika
```

```bash
passwd isidora
#unesite DVA puta sifru za korisnika
```

```bash
passwd lazar
#unesite DVA puta sifru za korisnika
```

</details>



## Задатак 7.2

Додати заједнички директоријум saradnici, конкретно унутар директоријума /home/, нека то буде заједнички "кућни" директоријум за све сараднике, пошто нису креирани појединачни. Подесити привилегије тако да важи:
* корисничка група која је власник директоријума јесте saradnici,
* за садржај унутар директоријума власник и група имају пуне привилегије, док остали корисници немају никакво право.

\* Имати у виду да је идеја да ово буде дељени директоријум, односно да сва 3 сарадника из групе имају приступ овом директоријуму.



<details markdown='block'>
<summary>Решење</summary>

```bash
#sudo su -
#ukoliko ste se izlogovali iz prethodnog shell-a
mkdir /home/saradnici
chown :saradnici /home/saradnici
chmod 2770 /home/saradnici
ls -ld /home/saradnici
```

Уколико није јасно зашто је овакав излаз ls команде, или зашто број 2 стоји при позиву chmod команде, посаветовати се са дежурним [лекаром или фармацеутом](https://chat.openai.com/), или питати сараднике на вежбама.

</details>


## Задатак 7.3

Потребно је истестирати привилегије које сте до сада реализовали. Првобитно се излоговати из сесије супер корисника, уколико већ нисте. Потом, неопходно је да унутар директоријума креирате фајл, рецимо под називом test. Размотрите да ли је могуће то учинити са вашег подразумеваног налога, и зашто не (уколико сте пак пробали да изведете овај маневар, и то сте успешно реализовали, вратити се на подзадатак [7.2](#задатак-72)). За крај, потребно је неки садржај уписати у test фајл, рецимо унос са тастатуре; неопходно је да ово учини 1 од 2 сарадника који нису изворни власник фајла. Рецимо да је иницијално фајл креирао Филип, а потом садржај у њега уписао Лазар. Уколико имате проблема са писањем садржаја у поменути фајл, поново се навратите на подзадатак [7.2](#задатак-72).

<details markdown='block'>
<summary>Решење</summary>

```bash
#exit
#ukoliko se niste izlogovali iz prethodnog shell-a
su filip
#uneti korisnicku sifru
touch /home/saradnici/test
exit
ls -l /home/saradnici/test
#obratiti paznju na vlasnika, ali i grupu kod izlistanog fajla
```
```bash
su lazar
echo sporcki pozdrav > /home/saradnici/test
cat /home/saradnici/test
exit
```

</details>
