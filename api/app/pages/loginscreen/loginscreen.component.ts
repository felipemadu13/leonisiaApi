import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';  // Importa FormsModule
import { Router } from '@angular/router';
import { AuthService } from '@services/auth.service';

@Component({
  selector: 'app-loginscreen',
  templateUrl: './loginscreen.component.html',
  styleUrls: ['./loginscreen.component.css'],
  standalone: true,  // Declara como componente standalone
  imports: [FormsModule]  // Adiciona FormsModule aqui
})
export class LoginscreenComponent {
  email: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  goToHome() {
    this.authService.login(this.email, this.password).subscribe(
      (response: any) => {
        console.log('Login bem-sucedido:', response);  // Log para depuração
        if (response.token) {
          this.authService.setToken(response.token); // Armazena o token recebido
          this.router.navigate(['/home']); // Redireciona para a página inicial
        } else {
          alert('Erro: Token não recebido.');
        }
      },
      (error: any) => {
        console.error('Erro ao fazer login:', error);
        alert('Erro ao fazer login: ' + (error.error?.error || 'Verifique suas credenciais'));
      }
    );
  }
}
