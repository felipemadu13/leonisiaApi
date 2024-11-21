import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { faHome, faUser, faCog, faBars, faRepeat, faReceipt, faShop, faCut  } from '@fortawesome/free-solid-svg-icons';


@Component({
  selector: 'app-siderbar-menu',
  standalone: true,
  imports: [FontAwesomeModule, CommonModule, RouterLink, RouterOutlet],
  templateUrl: './siderbar-menu.component.html',
  styleUrl: './siderbar-menu.component.css'
})
export class SiderbarMenuComponent {
  isCollapsed: boolean = false;

  // Ícones Font Awesome
  faHome = faHome;
  faUser = faUser;
  faCog = faCog;
  faBars = faBars;
  faRepeat = faRepeat;  // Ícone de repetição
  faReceipt = faReceipt;  // Ícone de recibo
  faShop = faShop;  // Ícone de loja
  faCut = faCut;  // Ícone de tesoura (representando cabelo)

  toggleMenu() {
    this.isCollapsed = !this.isCollapsed;
  }
}
