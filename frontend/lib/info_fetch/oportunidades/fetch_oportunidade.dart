import 'package:http/http.dart' as http;
import 'package:frontend/api_config.dart';
import 'oportunidade_model.dart' as model;

class FetchOportunidade {
  final String orgId;

  // Igual ao FetchFeed: org_id vazio faz o backend retornar todas as
  // oportunidades (sem filtrar por organização).
  FetchOportunidade({this.orgId = ''});

  Future<List<model.OportunidadeItem>> fetchOportunidades() async {
    var client = http.Client();
    
    var uri = Uri.parse('${ApiConfig.baseUrl}/oportunidades?org_id=$orgId');
    
    var response = await client.get(uri);
    if (response.statusCode == 200) {
      return model.oportunidadeFromJson(response.body);
    } else {
      throw Exception('Falha ao carregar as oportunidades de voluntariado');
    }
  }
}