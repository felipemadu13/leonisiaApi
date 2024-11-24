import { Component, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe, DatePipe } from '@angular/common';
import { registerLocaleData } from '@angular/common';
import localePt from '@angular/common/locales/pt'; 
import { SiderbarMenuComponent } from '../home/sidebar-menu/siderbar-menu/siderbar-menu.component';
import { ServicoRealizadoService } from '@services/servico-realizado.service';
import { TransacoesService } from '@services/transacoes.service';

registerLocaleData(localePt); 

@Component({
  selector: 'app-servicos-realizados',
  standalone: true,  
  imports: [CurrencyPipe, DatePipe, CommonModule, SiderbarMenuComponent],
  templateUrl: './servicos-realizados.component.html',
  styleUrls: ['./servicos-realizados.component.css'],
  providers: [
    CurrencyPipe,
    DatePipe,
    { provide: 'LOCALE_ID', useValue: 'pt-BR' },
  ]
})
export class ServicosRealizadosComponent implements OnInit {
  servicosRealizados: any[] = [];
  transacoes: any[] = [];

  constructor(private servicosRealizadosService: ServicoRealizadoService, private transacoesService: TransacoesService) { }

   ngOnInit(): void {
    this.servicosRealizadosService.getServicos().subscribe(data => {
      this.servicosRealizados = data;
      console.log(data)

    });

    this.transacoesService.getTransactions().subscribe((data) => {
      this.transacoes = data.sort((a, b) => new Date(b.data).getTime() - new Date(a.data).getTime());
      console.log(data)

    });
  
  }
}
