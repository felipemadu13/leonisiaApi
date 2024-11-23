export interface PieChartData {
  labels: string[];   // Rótulos no eixo X
  datasets: {         // Conjunto de dados, pode haver mais de um dataset
    data: number[];   // Dados numéricos para o gráfico
    label: string;    // Rótulo para cada conjunto de dados
  }[];
}
