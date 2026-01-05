#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Definisanje promenljive za naziv datoteke
    char filename[100];

    // Traži od korisnika da unese naziv datoteke
    printf("Унесите назив датотеке: ");
    fgets(filename, sizeof(filename), stdin);  // Unos sa tastature

    // Uklanjanje novog reda na kraju unosa (ako postoji)
    filename[strcspn(filename, "\n")] = 0;

    // Otvoriti datoteku u režimu samo za čitanje da proverimo da li postoji
    FILE *file = fopen(filename, "r");  // Otvori datoteku samo za čitanje

    if (file == NULL) {
        // Ako datoteka ne postoji, ispiši grešku i izađi iz programa
        perror("Датотека не постоји");
        return 1;
    }

    fclose(file);  // Zatvaramo datoteku jer smo samo proverili njeno postojanje

    // Otvoriti datoteku za upis
    file = fopen(filename, "w");

    if (file == NULL) {
        perror("Није могуће отворити датотеку за упис");
        return 1;
    }

    // Upisivanje sadržaja u datoteku
    fprintf(file, "Строго дефинисан садржај датотеке %s.\n", filename);

    // Zatvaranje fajla
    fclose(file);

    // Informacija o uspešnom upisu
    printf("Садржај је успешно уписан у датотеку %s.\n", filename);

    return 0;
}
