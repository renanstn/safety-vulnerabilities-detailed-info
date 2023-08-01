# Safety Detailed Report

## Descrição

O objetivo deste projeto é pegar o output do comando `safety check`, extrair o
link que detalha cada vulnerabilidade, acessar o link, e extrair da página o
**título** e o **nível** delas.

## Exemplo de uso

Para testes individuais:

```sh
python get_details.py https://pyup.io/v/49733/f17/
```

Usando a partir de uma lista com múltiplos links:

```sh
docker-compose run --rm --no-deps my-project \
safety check --full-report --output text | \
grep 'please visit' | \
cut -d" " -f 9 | \
xargs -n 1 python get_details.py
```
