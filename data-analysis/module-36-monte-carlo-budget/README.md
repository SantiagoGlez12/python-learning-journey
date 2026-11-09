# Módulo 36 — Simulación Monte Carlo de costos

Práctica de Python sobre un presupuesto de equipamiento de oficina, con un modelo determinístico, dos modelos probabilísticos y un análisis de sensibilidad.

## Archivos

- `module-36-monte-carlo-budget.ipynb`: notebook ejecutado y con las gráficas guardadas en sus salidas.

No se necesita CSV; los datos del presupuesto son supuestos didácticos definidos al comienzo del notebook.

## Contenido

1. Presupuesto determinístico por ítem.
2. Distribuciones normal y triangular de los precios.
3. Simulación Monte Carlo de 5,000 iteraciones por escenario.
4. Media, mediana, desviación estándar, percentiles y probabilidad de exceder un presupuesto con 10% de contingencia.
5. Histogramas, diagrama de caja y gráfico de riesgo.
6. Sensibilidad al tipo de distribución y al aumento del precio de un ítem.
7. Conclusiones y limitaciones.

## Ejecutar

Usa Python con NumPy, Pandas, Matplotlib y Jupyter. Abre el notebook en VS Code, selecciona el kernel de Python y haz clic en **Run All**.

```bash
python -m pip install numpy pandas matplotlib jupyterlab
```

## Resultados ilustrativos (semilla 36)

| Métrica | Resultado |
| --- | ---: |
| Presupuesto determinístico | 6,460.00 |
| Iteraciones por escenario | 5,000 |
| Costo medio normal | 6,456.83 |
| Costo medio triangular | 6,458.99 |
| P90 normal | 6,978.27 |
| P90 triangular | 6,882.35 |
| Probabilidad de exceder 7,106 (normal) | 5.32% |
| Probabilidad de exceder 7,106 (triangular) | 1.94% |

Los montos son unidades monetarias ilustrativas; **no** representan costos reales de proveedores.
