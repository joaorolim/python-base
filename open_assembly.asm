section .data
    arquivo db 'exemplo.txt', 0  ; Nome do arquivo
    modo db 'r', 0                ; Modo de abertura ('r' para leitura)
    permissao db 0644             ; Permissões do arquivo

section .text
global _start

_start:
    ; Chamada ao sistema para abrir o arquivo
    mov eax, 5          ; Número da chamada ao sistema para open (syscall)
    mov ebx, arquivo    ; Endereço do nome do arquivo
    mov ecx, 0          ; Modo de abertura (0 para leitura)
    mov edx, permissao  ; Permissões do arquivo
    int 0x80            ; Interrupção para chamar o sistema

    ; Manipular o retorno da chamada ao sistema (pode ser o identificador do arquivo)

    ; Terminar o programa
    mov eax, 1          ; Número da chamada ao sistema para exit
    xor ebx, ebx        ; Código de saída
    int 0x80            ; Interrupção para chamar o sistema
