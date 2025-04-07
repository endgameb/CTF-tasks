#include <stdio.h>
#include <string.h>
#include <ctype.h>

void caesar_decrypt(char *data, int shift) {
    for (int i = 0; data[i] != '\0'; i++) {
        if (isalpha(data[i])) {
            // Если буква, сдвигаем
            char base = islower(data[i]) ? 'a' : 'A';
            data[i] = (data[i] - base - shift + 26) % 26 + base;
        }
    }
}

int main() {
    // Пример строки для шифра Цезаря (к примеру, строка с ключом 17)
    char str[] = "wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}";

    // Применяем сдвиг от 1 до 25
    for (int shift = 1; shift <= 25; shift++) {
        char decrypted[strlen(str) + 1];
        strcpy(decrypted, str);

        caesar_decrypt(decrypted, shift);
        printf("Shift: %d -> %s\n", shift, decrypted);
    }

    return 0;
}
