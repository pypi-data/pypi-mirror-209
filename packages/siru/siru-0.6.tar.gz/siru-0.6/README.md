# SIRU

[![PyPI - Version](https://img.shields.io/pypi/v/siru.svg)](https://pypi.org/project/siru)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/siru.svg)](https://pypi.org/project/siru)

-----

SIRU is a tool to run automated tests on hardware, designed to be used in the development of embedded systems.

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install siru
```
## Arquitectura Ruwaq

@startuml
skinparam componentStyle uml1

frame "Microkernel" {
    [Despachador] -l-> Ejecutar : usa
    Ejecutar <.l. [Servidor PREAT] : usa

    port Registrar
    [Despachador] -r-> Registrar

    [Servidor PREAT] ..> Enviar : usa
    [Servidor PREAT] ..> Recibido : usa

    Recibido <-- [Transporte]
    Enviar <-- [Transporte]
}

Registrar <.. [GPIO]: usa
[Despachador] --> [GPIO]
@enduml

## Arquitectura Siru

@startuml
skinparam componentStyle uml1

[DUT] -right-> [ATE]

[ATE] -right-> [GPIO]

[ATE] ..> Ejecutar: usa
[ATE] ..> Esperar: usa
[GPIO] ..> Ejecutar: usa

Ejecutar <-- [PREAT]
Esperar <-- [PREAT]
@enduml
siru
## License

`SIRU` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
