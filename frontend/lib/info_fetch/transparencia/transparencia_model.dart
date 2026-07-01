import 'dart:convert';

List<TransacaoModel> transacaoFromJson(String str) => List<TransacaoModel>.from(json.decode(str).map((x) => TransacaoModel.fromJson(x)));

String transacaoToJson(List<TransacaoModel> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class TransacaoModel {
  TransacaoModel({
    this.id,
    required this.tipo,
    required this.valor,
    required this.data,
    required this.descricao,
    this.createdAt,
    this.createdBy,
  });

  String? id;
  String tipo;
  double valor;
  DateTime data;
  String descricao;
  DateTime? createdAt;
  String? createdBy;

  factory TransacaoModel.fromJson(Map<String, dynamic> json) => TransacaoModel(
        id: json["id"],
        tipo: json["tipo"],
        valor: json["valor"].toDouble(),
        data: DateTime.parse(json["data"]),
        descricao: json["descricao"],
        createdAt: json["created_at"] != null ? DateTime.parse(json["created_at"]) : null,
        createdBy: json["created_by"],
      );

  Map<String, dynamic> toJson() => {
        "id": id,
        "tipo": tipo,
        "valor": valor,
        "data": data.toIso8601String(),
        "descricao": descricao,
        "created_at": createdAt?.toIso8601String(),
        "created_by": createdBy,
      };
}
