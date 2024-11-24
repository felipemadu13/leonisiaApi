import { Component, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // Importe o FormsModule diretamente

@Component({
  selector: 'app-reset-password',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './reset-password.component.html',
  styleUrl: './reset-password.component.css'
})
export class ResetPasswordComponent {
  email: string = '';

  onSubmit() {
    if (this.email) {
      console.log('Solicitação de redefinição de senha para:', this.email);
      // Lógica para enviar a solicitação de redefinição de senha
    }
  } 
}
