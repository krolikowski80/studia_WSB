.data
array1: .word 1, 2, 3, 4
array2: .word 1, 2, 3, 4
result: .space 16

.text
.globl main
main:
    la $t0, array1  # Adres tablicy 1
    la $t1, array2  # Adres tablicy 2
    la $t2, result  # Adres tablicy wynikowej

    li $t3, 4       # Liczba elementów

loop:
    lw $t4, 0($t0)  # Pobierz element z tablicy 1
    lw $t5, 0($t1)  # Pobierz element z tablicy 2
    add $t6, $t4, $t5  # Dodaj elementy
    sw $t6, 0($t2)  # Zapisz wynik

    addi $t0, $t0, 4  # Przejdź do następnego elementu w tablicy 1
    addi $t1, $t1, 4  # Przejdź do następnego elementu w tablicy 2
    addi $t2, $t2, 4  # Przejdź do następnego elementu w tablicy wynikowej

    subi $t3, $t3, 1  # Zmniejsz licznik
    bgtz $t3, loop    # Jeśli są jeszcze elementy, kontynuuj pętlę

    li $v0, 10
    syscall