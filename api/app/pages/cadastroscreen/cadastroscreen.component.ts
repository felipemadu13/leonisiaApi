// cadastroscreen.component.ts

import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-cadastroscreen',
  templateUrl: './cadastroscreen.component.html',
  styleUrls: ['./cadastroscreen.component.css']
})
export class CadastroScreenComponent {
  servico = { nome: '', descricao: '', preco: null };
  mensagemSucesso = '';
  mensagemErro = '';

  constructor(private http: HttpClient) {}

  onSubmit(): void {
    this.http.post('http://localhost:8000/api/servicos/', this.servico).subscribe(
      response => {
        this.mensagemSucesso = 'Serviço cadastrado com sucesso!';
        this.servico = { nome: '', descricao: '', preco: null };
        this.mensagemErro = '';
      },
      error => {
        this.mensagemErro = 'Ocorreu um erro ao cadastrar o serviço. Tente novamente.';
        this.mensagemSucesso = '';
      }
    );
  }
}
