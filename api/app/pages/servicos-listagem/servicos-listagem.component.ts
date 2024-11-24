// servicos-listagem.component.ts

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { registerLocaleData } from '@angular/common';
import localePt from '@angular/common/locales/pt'; 
import { ServicoService } from '@services/servico.service';
import { SiderbarMenuComponent } from '../home/sidebar-menu/siderbar-menu/siderbar-menu.component'; // Importação do componente da Sidebar

registerLocaleData(localePt); 

@Component({
  selector: 'app-servicos-listagem',
  standalone: true,
  imports: [CurrencyPipe, CommonModule, SiderbarMenuComponent], // Adição da Sidebar nos imports
  templateUrl: './servicos-listagem.component.html',
  styleUrls: ['./servicos-listagem.component.css'],
  providers: [
    CurrencyPipe,
    { provide: 'LOCALE_ID', useValue: 'pt-BR' },
  ]
})
export class ServicosListagemComponent implements OnInit {
  servicos: any[] = [];

  constructor(private servicoService: ServicoService, private router: Router) { }

  ngOnInit(): void {
    this.servicoService.getServicos().subscribe(data => {
      this.servicos = data;
    });
    
  }

  deletarServico(id: number): void {
    this.servicoService.deleteServico(id).subscribe(() => {
      this.servicos = this.servicos.filter(servico => servico.id !== id);
    });
  }

  editarServico(id: number): void {
    this.router.navigate(['/servicos/editar/', id]);
  }

  irParaCadastro(): void {
    this.router.navigate(['/servicos/cadastro']);
  }


}
