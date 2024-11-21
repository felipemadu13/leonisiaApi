import { ServicoRealizado2 } from './ServicoRealizado2';

export interface Transacoes {
  tipo: 'entrada' | 'saida';
  data: Date;
  metodoPagamento: string;
  valor: number;
  servicosRealizados: ServicoRealizado2[];
}
