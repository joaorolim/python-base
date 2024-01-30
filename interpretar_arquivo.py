#!/usr/bin/env python3

def interpretar_arquivo_txt(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'rb') as arquivo:
            # Lê os bytes do arquivo
            bytes_do_arquivo = arquivo.read()

            print(bytes_do_arquivo)

            # Interpreta os bytes usando ASCII
            texto_interpretado = bytes_do_arquivo.decode('utf-8')

            return texto_interpretado

    except FileNotFoundError:
        print(f"O arquivo {caminho_do_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao interpretar o arquivo: {e}")

# Exemplo de uso
caminho_do_arquivo_txt = 'names.txt'
texto_interpretado = interpretar_arquivo_txt(caminho_do_arquivo_txt)

if texto_interpretado:
    print("Conteúdo do arquivo:")
    print(texto_interpretado)
