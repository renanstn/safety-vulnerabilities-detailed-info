# Safety Detailed Report

## Descrição

O objetivo deste projeto é, a partir do link de detalhes de uma vulnerabilidade
obtido no output do comando `safety check --full-report --output text`, extrair
da página o **título** e a **classificação** dela, no seguinte formato:

```
- CVE-2022-23491 - HIGH
```

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
