enum DirecaoDoacao { instituicao, projeto }

enum VisibilidadeDoacao { publica, anonima }

class EnderecoDoacao {
  final String logradouro; // Street Address
  final String complemento; // Street Address Line 2
  final String cidade; // City
  final String estado; // Region/State/Province
  final String cep; // Postal / Zip code (CEP)
  final String pais; // Country

  EnderecoDoacao({
    required this.logradouro,
    this.complemento = '',
    required this.cidade,
    required this.estado,
    required this.cep,
    required this.pais,
  });

  Map<String, dynamic> toJson() => {
        'logradouro': logradouro,
        'complemento': complemento,
        'cidade': cidade,
        'estado': estado,
        'cep': cep,
        'pais': pais,
      };
}

class DoacaoRequest {
  final double valor;
  final VisibilidadeDoacao visibilidade;
  final String? nomeDoador;
  final String? cpf;
  final EnderecoDoacao? endereco;
  final DirecaoDoacao direcao;
  final String? nomeProjeto;

  DoacaoRequest({
    required this.valor,
    required this.visibilidade,
    this.nomeDoador,
    this.cpf,
    this.endereco,
    required this.direcao,
    this.nomeProjeto,
  });

  Map<String, dynamic> toJson() => {
        'valor': valor,
        'is_anonima': visibilidade == VisibilidadeDoacao.anonima,
        // Nome sempre enviado (usado na transparência, independente do anonimato)
        if (nomeDoador != null && nomeDoador!.isNotEmpty)
          'nome_doador': nomeDoador,
        if (cpf != null && cpf!.isNotEmpty) 'cpf': cpf,
        if (endereco != null) 'endereco': endereco!.toJson(),
        'direcao': direcao.name,
        if (nomeProjeto != null && nomeProjeto!.isNotEmpty)
          'nome_projeto': nomeProjeto,
      };
}
