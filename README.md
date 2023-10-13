# check-weather

> Estes códigos presentes nesse repositório foram criados pelo site https://www.pythontutorial.net/python-unit-testing/, no qual eu traduzi e reescrevi para realizar aprendizado.

## Rodando testes unitários

### Rodando todos os testes
Para rodar todos os testes no repositório de testes, utilize o comando:

```shell
python3 -m unittest discover -v
```

O ``discover`` é um subcomando que encontra todos os testes no projeto.

Saída:
```powershell
test_area (test_circle.TestCircle) ... ok
test_circle_instance_of_shape (test_circle.TestCircle) ... ok
test_create_circle_negative_radius (test_circle.TestCircle) ... ok
test_area (test_square.TestSquare) ... ok
test_create_square_negative_length (test_square.TestSquare) ... ok
test_square_instance_of_shape (test_square.TestSquare) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```


### Rodando um único teste de módulo
Para rodar um teste de módulo singular, você utiliza o seguinte comando:

```shell
python3 -m unittest test_package.test_module -v
```

Por exemplo, para executar todos os seguintes testes no módulo ``test_circle`` do arquivo de ``test``.

```shell
python -m unittest test.test_circle -v
```

Saída:
```powershell
test_area (test.test_circle.TestCircle) ... ok
test_circle_instance_of_shape (test.test_circle.TestCircle) ... ok
test_create_circle_negative_radius (test.test_circle.TestCircle) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

### Rodando um único teste de classe
Um módulo de teste pode conter múltiplas classes. Para rodar um único teste de classe num módulo de testes, você pode utilizar o seguinte comando.

```shell
python -m unittest test_package.test_module.TestClass -v
```

Por exemplo, o seguinte comando de teste da classe ``TestSquare`` do módulo dos arquivos de teste ``test_square``.

```shell
python -m unittest test.test_circle.TestCircle -v
```

## Gerando Cobertura de testes

Cobertura de testes é a proporção entre o número de linhas executadas por pelo menos um caso de teste e o totaal do número de linhas.

> cobertura de teste = linhas de código executadas / número de linhas totais
