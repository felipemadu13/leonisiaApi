// servicos-cadastro.component.ts

import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ServicoService } from '@services/servico.service';
import { SiderbarMenuComponent } from '../home/sidebar-menu/siderbar-menu/siderbar-menu.component';
import { Servico } from '../../models/Servico';


@Component({
  selector: 'app-servicos-cadastro',
  standalone: true,
  imports: [SiderbarMenuComponent, ReactiveFormsModule, CommonModule],

  templateUrl: './servicos-cadastro.component.html',
  styleUrls: ['./servicos-cadastro.component.css']
})
export class ServicosCadastroComponent implements OnInit {
  cadastroForm: FormGroup;
  isEditMode: boolean = false;
  servicoId: number | null = null;

  constructor(
    private fb: FormBuilder,
    private servicoService: ServicoService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.cadastroForm = this.fb.group({
      nome: ['', Validators.required],
      descricao: [''],
      preco: [0, Validators.required]
    });
  }

  ngOnInit(): void {
    // Verifica se há um 'id' na rota para definir o modo de edição
    this.servicoId = Number(this.route.snapshot.paramMap.get('id'));
    this.isEditMode = !!this.servicoId;

    if (this.isEditMode) {
      this.carregarServico();
    }
  }

  carregarServico(): void {
    this.servicoService.getServicoById(this.servicoId!).subscribe(
      (servico: Servico) => {
        this.cadastroForm.patchValue({
          nome: servico.nome,
          descricao: servico.descricao,
          preco: servico.preco
        });
      },
      (error: any) => console.error('Erro ao carregar o serviço', error)
    );
  }

  salvar(): void {
    if (this.cadastroForm.invalid) {
      return;
    }

    const servicoData: Servico = this.cadastroForm.value;
    if (this.isEditMode) {
      this.servicoService.updateServico(this.servicoId!, servicoData).subscribe(
        () => this.router.navigate(['/servicos']),
        (error: any) => console.error('Erro ao editar o serviço', error)
      );
    } else {
      this.servicoService.createServico(servicoData).subscribe(
        () => this.router.navigate(['/servicos']),
        (error: any) => console.error('Erro ao cadastrar o serviço', error)
      );
    }
  }

  cancelar(): void {
    this.router.navigate(['/servicos']);
  }
}
