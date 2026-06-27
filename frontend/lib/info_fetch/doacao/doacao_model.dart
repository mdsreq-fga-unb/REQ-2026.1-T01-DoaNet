enum DirecaoDoacao { instituicao, projeto }

enum VisibilidadeDoacao { publica, anonima }

class DoacaoRequest {
  final double valor;
  final VisibilidadeDoacao visibilidade;
  final String? nomeDoador;
  final DirecaoDoacao direcao;
  final String? nomeProjeto;

  DoacaoRequest({
    required this.valor,
    required this.visibilidade,
    this.nomeDoador,
    required this.direcao,
    this.nomeProjeto,
  });

  Map<String, dynamic> toJson() => {
        'valor': valor,
        'is_anonima': visibilidade == VisibilidadeDoacao.anonima,
        if (nomeDoador != null && nomeDoador!.isNotEmpty)
          'nome_doador': nomeDoador,
        'direcao': direcao.name,
        if (nomeProjeto != null && nomeProjeto!.isNotEmpty)
          'nome_projeto': nomeProjeto,
      };
}
