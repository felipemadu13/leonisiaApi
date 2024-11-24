import { BarChartData } from './BarChartData';
import { PieChartData } from './PieChartData';

export interface Dashboard {
  saldoGeral: number;
  entradaDiario: number;
  entradaMensal: number;
  saidaDiario: number;
  saidaMensal: number;
  balancoDiario: number;
  balancoMensal: number;
  BarChartData: BarChartData;
  PieChartData: PieChartData;
}
