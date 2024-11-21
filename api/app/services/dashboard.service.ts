import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Dashboard } from '../models/Dashboard';


@Injectable({
  providedIn: 'root'
})
export class DashboardService {
  private apiUrl = 'http://localhost:8000/dashboard';

  constructor(private http: HttpClient) { }

  getDashboard(): Observable<Dashboard> {
    return this.http.get<Dashboard>(this.apiUrl);
  }

}
