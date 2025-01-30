.data
prompt_a: .asciiz "Podaj wartość a: "
prompt_b: .asciiz "Podaj wartość b: "
prompt_c: .asciiz "Podaj wartość c: "
result_msg: .asciiz "Wynik: "

.text
.globl main
main:
    # Pobranie wartości a
    li $v0, 4
    la $a0, prompt_a
    syscall
    li $v0, 5
    syscall
    move $t0, $v0  # $t0 = a

    # Pobranie wartości b
    li $v0, 4
    la $a0, prompt_b
    syscall
    li $v0, 5
    syscall
    move $t1, $v0  # $t1 = b

    # Pobranie wartości c
    li $v0, 4
    la $a0, prompt_c
    syscall
    li $v0, 5
    syscall
    move $t2, $v0  # $t2 = c

    # Obliczenia: 7*(a+b)+2*b+c
    add $t3, $t0, $t1  # $t3 = a + b
    mul $t3, $t3, 7    # $t3 = 7 * (a + b)
    mul $t4, $t1, 2    # $t4 = 2 * b
    add $t3, $t3, $t4  # $t3 = 7*(a+b) + 2*b
    add $t3, $t3, $t2  # $t3 = 7*(a+b) + 2*b + c

    # Wyświetlenie wyniku
    li $v0, 4
    la $a0, result_msg
    syscall
    li $v0, 1
    move $a0, $t3
    syscall

    # Zakończenie programu
    li $v0, 10
    syscall