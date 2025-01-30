.data
menu: .asciiz "Wybierz operację (1: dodawanie, 2: mnożenie): "
prompt_x: .asciiz "Podaj pierwszą liczbę: "
prompt_y: .asciiz "Podaj drugą liczbę: "
result_add: .asciiz "Wynik dodawania: "
result_mul: .asciiz "Wynik mnożenia: "

.text
.globl main
main:
    # Wyświetlenie menu
    li $v0, 4
    la $a0, menu
    syscall
    li $v0, 5
    syscall
    move $t0, $v0  # $t0 = wybór operacji

    # Pobranie pierwszej liczby
    li $v0, 4
    la $a0, prompt_x
    syscall
    li $v0, 5
    syscall
    move $t1, $v0  # $t1 = x

    # Pobranie drugiej liczby
    li $v0, 4
    la $a0, prompt_y
    syscall
    li $v0, 5
    syscall
    move $t2, $v0  # $t2 = y

    # Wykonanie operacji
    beq $t0, 1, add_op  # Jeśli 1, dodawanie
    beq $t0, 2, mul_op  # Jeśli 2, mnożenie
    j end

add_op:
    add $t3, $t1, $t2  # $t3 = x + y
    li $v0, 4
    la $a0, result_add
    syscall
    li $v0, 1
    move $a0, $t3
    syscall
    j end

mul_op:
    mul $t3, $t1, $t2  # $t3 = x * y
    li $v0, 4
    la $a0, result_mul
    syscall
    li $v0, 1
    move $a0, $t3
    syscall

end:
    li $v0, 10
    syscall