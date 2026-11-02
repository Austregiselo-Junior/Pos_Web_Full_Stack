export interface Paciente {
    clienteId?: number;
    nome: string;
    dataConsulta: string;
    telefone: string;
    formaPagamento: string;
    valorSessao?: number;
    quantidadeSessao?: number;
    situacaoFinanceiraSessao?: string;
    valorTotal?: number;
    desconto?: number;
    quantidadeParcelas?: number;
    diaVencimento?: number;
    situacaoFinanceiraMensal?: string;
  }