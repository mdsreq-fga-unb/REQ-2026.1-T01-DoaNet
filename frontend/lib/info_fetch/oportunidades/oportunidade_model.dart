import 'dart:convert';

List<OportunidadeItem> oportunidadeFromJson(String str) =>
    List<OportunidadeItem>.from(json.decode(str).map((x) => OportunidadeItem.fromJson(x)));

class OportunidadeItem {
  String id;
  String titulo;
  String descricao;
  String local;
  String horario;
  int vagasTotais;
  int vagasPreenchidas;
  String? linkInscricao;
  String? imagemUrl;
  bool ativo;

  OportunidadeItem({
    required this.id,
    required this.titulo,
    required this.descricao,
    required this.local,
    required this.horario,
    required this.vagasTotais,
    required this.vagasPreenchidas,
    this.linkInscricao,
    this.imagemUrl,
    required this.ativo,
  });

  factory OportunidadeItem.fromJson(Map<String, dynamic> json) => OportunidadeItem(
    id: json["_id"] ?? json["id"] ?? '',
    titulo: json["titulo"] ?? '',
    descricao: json["descricao"] ?? '',
    local: json["local"] ?? '',
    horario: json["horario"] ?? '',
    vagasTotais: json["vagas_totais"] ?? 0,
    vagasPreenchidas: json["vagas_preenchidas"] ?? 0,
    linkInscricao: json["link_inscricao"],
    imagemUrl: json["imagem_url"],
    ativo: json["ativo"] ?? true,
  );
}