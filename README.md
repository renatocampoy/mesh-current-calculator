# Mesh Current Calculator

O **Mesh Current Calculator** é um aplicativo GUI desenvolvido em Python para resolver sistemas de malhas elétricas utilizando o método das correntes de malha. Ele permite a entrada de equações de malhas e valores conhecidos, resolvendo-as e exibindo os valores das correntes de malha.

## Funcionalidades

- Adicionar equações de malhas elétricas.
- Definir valores conhecidos para as malhas.
- Resolver o sistema de equações para encontrar as correntes nas malhas.
- Exibir os resultados das correntes de malha.

## Demonstração em Vídeo

[![Assista ao vídeo de demonstração](http://i3.ytimg.com/vi/cplhZHZ8OW0/hqdefault.jpg)](https://www.youtube.com/watch?v=cplhZHZ8OW0)


## Pré-requisitos

Para executar este projeto, você precisa ter o Python instalado em seu sistema, bem como as bibliotecas `sympy` e `tkinter`. Você pode instalar `sympy` utilizando o pip:

```sh
pip install sympy
```

## Como Executar

1. Clone este repositório ou baixe o arquivo `mesh_current_calculator.py`.

2. Certifique-se de ter o Python instalado e as bibliotecas necessárias (`sympy` e `tkinter`).

3. Execute o script Python:

```sh
python mesh_current_calculator.py
```

4. Uma interface gráfica será aberta. Use os botões para adicionar malhas, resolver o sistema e limpar a tela.

## Exemplo de Uso

- Clique em **Adicionar Malha** para inserir uma nova malha.
- Se a malha tiver um valor definido, escolha "s" e insira o valor.
- Caso contrário, insira a equação da malha (ex: `20*(I2 - I1) + 40*(I2 - I3) + 50 = 0`).
- Clique em **Resolver Malhas** para calcular as correntes.
- Os resultados serão exibidos na área de texto.

## Autor

Desenvolvido por Eng. Renato Campoy (renato@campoy.eng.br).

## Licença

Este projeto é distribuído sob a licença =
