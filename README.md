# Gerador de Senhas

Programa simples em Python que gera uma **senha aleatória de 10 caracteres**, misturando letras, números e símbolos.

## Como funciona

O código monta uma lista com todos os caracteres possíveis e sorteia 10 deles para formar a senha:

- **Letras:** maiúsculas e minúsculas (`string.ascii_letters`)
- **Números:** de 0 a 9 (`string.digits`)
- **Símbolos:** pontuação como `!`, `@`, `#`, `$` (`string.punctuation`)

O sorteio é feito com `random.choices()`, que escolhe caracteres ao acaso, e o `"".join()` junta tudo em um único texto.

## Como executar

Não precisa instalar nada, pois as bibliotecas `random` e `string` já vêm com o Python.

```bash
python gerador_senha.py
```

> Troque `gerador_senha.py` pelo nome do arquivo com o código.

## Exemplo de saída

```text
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789
A senha gerada foi: k7#Qm@2pZ!
```

A primeira linha mostra todos os caracteres disponíveis. A senha muda a cada execução.

## Observações

- O tamanho da senha é definido pelo valor de `k` no código. Para uma senha de 16 caracteres, use `k=16`.
- Como o sorteio é totalmente aleatório, não há garantia de que a senha tenha pelo menos um número, um símbolo ou uma letra maiúscula.
- Este projeto foi feito para fins de estudos.

## Autor

Desenvolvido por **Davi Moura**.
