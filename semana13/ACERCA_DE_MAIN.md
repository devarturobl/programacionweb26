# Acerca de `main.py`

`main.py` implementa un dashboard interactivo con [NiceGUI](https://nicegui.io/) para visualizar 20 valores aleatorios. La interfaz está en español y adapta su distribución a pantallas pequeñas.

## Qué muestra

- **Tarjetas de resumen:** cantidad de elementos, suma, promedio y valor máximo.
- **Gráfica de barras:** compara el valor de cada elemento.
- **Gráfica circular tipo dona:** muestra la participación de cada elemento en el total.
- **Gráfica de línea:** permite comparar los valores siguiendo el orden de los elementos; no representa una serie temporal.
- **Botón «Generar nuevos datos»:** crea otro conjunto de 20 valores y actualiza las métricas y gráficas.

Los valores se generan aleatoriamente entre 15 y 100. Se mantienen en memoria mientras se ejecuta la aplicación; no se guardan en una base de datos.

## Organización del código

- `ELEMENT_COUNT`, `PALETTE` y las listas `values`, `labels` y `short_labels` definen el tamaño, colores y datos del conjunto.
- `chart_data()` prepara los valores con sus nombres para la gráfica circular.
- `bar_options()`, `pie_options()` y `line_options()` configuran las opciones de ECharts usadas por `ui.echart`.
- `dashboard()` construye la página, sus métricas y las tres gráficas. Está marcada como actualizable mediante `@ui.refreshable`.
- `metric()` crea cada tarjeta de resumen.
- `regenerate_data()` genera los nuevos valores y solicita actualizar el dashboard.
- `ui.add_head_html()` contiene los estilos de la página y sus reglas de diseño adaptable.

## Ejecución

Con Python y NiceGUI instalados, desde esta carpeta ejecuta:

```bash
python main.py
```

Después abre la dirección local que NiceGUI muestra en la terminal, normalmente <http://localhost:8080>.
