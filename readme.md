# Estructuras repetitivas 3147235
Proyecto para trabajar ciclos for y while en python

## Conceptos clave para trabajar en ciclos:
* **Breakpoint (Punto de interrupción)**: Herramienta para ejecutar código, una instrucción a la vez      
(depuración- debugger).
Permite ver el valor de las variables definidas en un programa
a tráves de la ejecución de código, permitiendo observar el comportamiento del programa/código a tráves del tiempo.

* **Variable contadora (contador)**: Una variable contadora es una variable a la cual podemos aumentar o disminuir su valor en una determinada cantidad constante (de 1 en 1, de 2 en 2, etc).

- Una variable contadora se debe inicializar 
**antes del ciclo de la estructura repetitiva** con un valor inicial (0.)
- Una variable contadora por lo general se nombra con las letras i , j.
- Una variable contadora **debe participar en la condicional del ciclo**.
- Toda variable contadora debe tener **una instrucción de incremento** para aumentar su valor.
- En un ciclo while, la instrucción de incremento se pone 
**al final del bloque de código del ciclo**.

* **Iteración**: Es un recorrido en la ejecución de un ciclo.

## Ciclo while

Estructura que permite ejecutar un bloque de código un número 
determinado de veces.
El bloque de código dentro de while se ejecutará 
sucesivamente **mientras que la condicional sea evaluada como 
VERDAD**.

### Sintáxis en Python:

```
While condicional:
      instruccion1
      instruccion2
      instruccion3
   ....
      instruccion n
```

## Ciclo for

Se utiliza (python) para recorrer conjuntos de datos   
( estructuras de datos - colecciones de datos) 

*El ciclo recorrerá cada dato de la estructura desde el primero hasta el último*.

*El  elemento recorrido se asigna a una variable en el ciclo*.

### Sintáxis for:

```
    for <variable> in <recolección de datos>:
        instruccion1
        instruccion2
        instruccion3
   ....
        instruccion n
```

```