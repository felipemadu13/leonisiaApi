import { Component, ViewChild } from '@angular/core';
import { Chart, ChartConfiguration, ChartData, ChartOptions, ChartType, ChartTypeRegistry } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';
import DataLabelsPlugin from 'chartjs-plugin-datalabels';
import { SiderbarMenuComponent } from "../sidebar-menu/siderbar-menu/siderbar-menu.component";
import { CommonModule, CurrencyPipe } from '@angular/common';
import { DashboardService } from '../../../services/dashboard.service';
import { Dashboard } from '../../../models/Dashboard';
import { FormsModule } from '@angular/forms';
import { MatButton } from '@angular/material/button';
import { registerLocaleData } from '@angular/common';
import localePt from '@angular/common/locales/pt';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { LOCALE_ID } from '@angular/core';

registerLocaleData(localePt);

Chart.register(DataLabelsPlugin);

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [SiderbarMenuComponent, CommonModule, FormsModule, BaseChartDirective, MatButton, CurrencyPipe, RouterLink, RouterOutlet],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [
    CurrencyPipe,
    { provide: 'LOCALE_ID', useValue: 'pt-BR' },
  ]
})
export class HomeComponent {
   currentDate: Date = new Date();

  @ViewChild(BaseChartDirective) chart: BaseChartDirective<'bar'> | undefined;

  public barChartType: keyof ChartTypeRegistry = 'bar';

  public barChartData: ChartData<'bar'> = {
    labels: [],
    datasets: [
      { data: [], label: '' },
    ],
  };

  public barChartOptions: ChartConfiguration<'bar'>['options'] = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {},
      y: { display: false }
    },
    plugins: {
      legend: { display: false},
      datalabels: {
        anchor: 'end',
        align: 'end',
        formatter: (value: any) => {
          const currencyPipe = new CurrencyPipe('pt-BR');
          return currencyPipe.transform(value, 'BRL', 'symbol', '1.2-2');
        }
      },
      tooltip: {
        callbacks: {
          label: (context) => {
            const currencyPipe = new CurrencyPipe('pt-BR');
            const transformedValue = currencyPipe.transform(context.parsed.y, 'BRL', 'symbol', '1.2-2');
            return transformedValue !== null ? transformedValue : '';
          }
        }
      }
    },
  };

  public pieChartType: ChartType = 'pie';

  public pieChartData: ChartData<'pie', number[], string | string[]> = {
    labels: [],
    datasets: [
      {
        data: [],
      },
    ],
  };
  
  public pieChartOptions: ChartConfiguration['options'] = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'right',
      },
      datalabels: {
      },
    },
  };

  dashboard: Dashboard = {
    saldoGeral: 0,
    entradaDiario: 0,
    entradaMensal: 0,
    saidaDiario: 0,
    saidaMensal: 0,
    balancoDiario: 0,
    balancoMensal: 0,
    BarChartData: {
      labels: [],
      datasets: [{ data: [], label: '' }],
    },
    PieChartData: {
      labels: [],
      datasets: [{ data: [], label: '' }],
    },
  };

  entrada: string = 'diario';
  saida: string = 'diario';
  balanco: string = 'diario';

  constructor(private dashboardService: DashboardService) { }

  ngOnInit(): void {
    this.dashboardService.getDashboard().subscribe(data => {
      this.dashboard = data;

      this.barChartData.labels = data.BarChartData.labels;
      this.barChartData.datasets = data.BarChartData.datasets;

      this.pieChartData.labels = data.PieChartData.labels;
      this.pieChartData.datasets = data.PieChartData.datasets;

      this.chart?.update();
    });
  }
}
