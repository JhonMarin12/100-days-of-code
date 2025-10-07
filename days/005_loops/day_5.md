# 🐍 Día 5 - Ciclos (Loop)
Los ciclos son repticiones que se pueden repetir dentro de nuestro codigo, dentro de python tenemos dos tipos de ciclos
- ciclo for
- ciclo while

la diferencia entre los dos es que for es un ciclo cuya dependencia radica en el objeto sobre el cual estamos realizando el flujo, por otro lado el ciclo while depende de una condición para que este se siga repitiendo. 

## Indetación
Si bien hemos visto anteriormente en condicionale estos espacios que "identan" el codigo, el concepto identar se refiere a mantener en los bloques adecuados el codigo, esto debido a la propia sintaxis del lenguaje y su vez una forma de entender como esta construido un programa.

### Inicializar valores en 0
obervarmos que no siempre es bueno inicializar valores con 0 ya que en ocasiones nos sabremos que tipo de datos son los que vienen, entonces como podriamos inicializar una variable sin incurrir en este error.
- valor = float('-inf')
- valor = lista[0] # Usar el primer elemento

## funcion range()
no solo podemos usar el ciclo for asociado a listas, podemos hacer ciclos for que no dependan de una lista, la función range crea un objeto iterable, un rango de numeros sobre el cual podemos iterar.