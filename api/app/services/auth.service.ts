import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://127.0.0.1:8000/api';  // URL base da API
  private tokenKey = 'token';  // Chave para armazenar o token no armazenamento local

  constructor(private http: HttpClient) {}

  // Método para fazer login
  login(username: string, password: string): Observable<any> {
    const loginData = { username, password };
    return this.http.post(`${this.apiUrl}/login/`, loginData);
  }

  // Armazenar o token no armazenamento local
  setToken(token: string): void {
    localStorage.setItem(this.tokenKey, token);
  }

  // Obter o token armazenado
  getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  // Verificar se o usuário está autenticado
  isAuthenticated(): boolean {
    const token = this.getToken();
    return !!token;  // Retorna true se o token existir
  }

  // Método para logout (remover o token)
  logout(): void {
    localStorage.removeItem(this.tokenKey);
  }
}
