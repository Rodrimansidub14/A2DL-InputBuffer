# Simulador de Búfer de Entrada en Python

## Descripción

Este proyecto implementa un simulador de búfer de entrada en Python. El programa procesa una cadena de caracteres utilizando un búfer de tamaño fijo y extrae lexemas (palabras) delimitados por espacios o por un marcador especial `eof` (End of File). Este enfoque es común en el análisis léxico de compiladores para manejar eficientemente grandes volúmenes de texto.

## Funcionamiento

El programa utiliza dos funciones principales:

### `cargar_buffer`

Esta función carga una porción de la entrada en el búfer.

- **Parámetros:**
  - `entrada`: Lista de caracteres que representa el texto a procesar.
  - `inicio`: Índice desde donde comenzar a cargar los datos en el búfer.
  - `tamano_buffer`: Tamaño fijo del búfer (en caracteres).

- **Proceso:**
  1. **Verificación de EOF:**
     - Si `inicio` es igual o mayor que la longitud de `entrada`, significa que se ha alcanzado el final de los datos. En este caso, la función retorna una lista con el carácter especial `'eof'` para indicar el final de la entrada.
  
  2. **Extracción de Segmento del Búfer:**
     - Se extrae una porción de la entrada desde `inicio` hasta `inicio + tamano_buffer`. Este segmento representa el contenido actual del búfer.
  
  3. **Manejo de EOF Parcial:**
     - Si la porción extraída es menor que el tamaño del búfer (`tamano_buffer`), significa que no hay suficientes caracteres para llenar el búfer completamente. En este caso, se añade `'eof'` al búfer para marcar el final de la entrada.
  
  4. **Retorno del Búfer:**
     - La función retorna la lista `buffer`, que contiene los caracteres cargados y, potencialmente, el centinela `'eof'`.

### `procesar_buffer`

Esta función procesa el contenido del búfer para extraer y mostrar los lexemas.

- **Parámetros:**
  - `entrada`: Lista de caracteres que representa el texto a procesar.
  - `tamano_buffer`: Tamaño fijo del búfer.

- **Proceso:**
  1. **Inicialización de Variables:**
     - `pos_entrada`: Rastrea la posición actual en la entrada que se está cargando en el búfer.
     - `lexema_parcial`: Lista que almacena parte de un lexema que no pudo ser completamente procesado en una carga de búfer.
     - `eof_encontrado`: Bandera que indica si ya se ha añadido `'eof'` al búfer para evitar múltiples adiciones.
     - `buffer`: Lista que representa el contenido actual del búfer.

  2. **Bucle Principal (`while True`):**
     - **Carga del Búfer:**
       - **Si el Búfer está Vacío:**
         - **Con `lexema_parcial`:**
           - Calcula cuántos caracteres nuevos son necesarios para completar el búfer (`needed`).
           - Extrae `needed` caracteres de la entrada desde `pos_entrada`.
           - Actualiza `pos_entrada` según los caracteres nuevos cargados.
           - Combina `lexema_parcial` con los nuevos caracteres cargados para formar el nuevo búfer.
           - Resetea `lexema_parcial` ya que ahora está completo.
           - Si el búfer resultante es más pequeño que `tamano_buffer` y no se ha encontrado `eof`, añade `'eof'` al búfer y marca `eof_encontrado` como `True`.
         
         - **Sin `lexema_parcial`:**
           - Carga un segmento normal del búfer desde `pos_entrada` hasta `pos_entrada + tamano_buffer`.
           - Actualiza `pos_entrada` según los caracteres cargados.
           - Si el búfer es más pequeño que `tamano_buffer` y no se ha añadido previamente `'eof'`, lo añade y marca `eof_encontrado` como `True`.
    
    3. **Procesamiento del Búfer:**
       - Inicializa los punteros `inicio` y `avance` en `0`.
       - Recorre el búfer carácter por carácter:
         - **Delimitadores (`' '` o `'eof'`):**
           - Si se encuentra un delimitador y `inicio` no es igual a `avance`, se extrae el lexema desde `inicio` hasta `avance` y se imprime.
           - Si el delimitador es `'eof'`, se termina el procesamiento retornando de la función.
           - Actualiza `inicio` a `avance + 1` para apuntar al inicio del siguiente lexema.
         - **Avance del Puntero:**
           - Incrementa `avance` para continuar recorriendo el búfer.
    
    4. **Manejo de Lexemas Partidos:**
       - **Después de Procesar el Búfer:**
         - Si `inicio` es menor que la longitud del búfer, significa que hay un lexema que no fue completado en esta carga (está al final del búfer sin un delimitador).
         - Este lexema parcial se almacena en `lexema_parcial` para ser combinado con la próxima carga de búfer.
         - Si no hay lexema parcial, se resetea `lexema_parcial` a una lista vacía.
       - **Reset del Búfer:**
         - Limpia el búfer para la próxima iteración del bucle principal.

## Ejemplo de Ejecución

### Entrada
```Esto es un ejemplo de entrada con eof```

### Salida Esperada
```
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: de
Lexema procesado: entrada
Lexema procesado: con
Lexema procesado: eof
```

### Video de explicación
https://youtu.be/lOlaSp0WIiQ 
