import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from '@services/auth.service';  // Ajuste o caminho conforme necessário

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router) {}

  canActivate(): boolean {
    if (this.authService.isAuthenticated()) {
      console.log('AuthGuard: Usuário autenticado - acesso permitido.');
      return true;  // Usuário autenticado, acesso permitido
    } else {
      console.warn('AuthGuard: Usuário não autenticado - redirecionando para login.');
      this.router.navigate(['/login']);  // Redirecionar para a página de login
      return false;  // Bloquear o acesso
    }
  }
}
