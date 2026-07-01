import 'package:http/http.dart' as http;
import 'package:frontend/api_config.dart';
import 'transparencia_model.dart' as model;

class FetchTransparencia {
  Future<List<model.TransacaoModel>> fetchTransacoes() async {
    var client = http.Client();
    
    var uri = Uri.parse('${ApiConfig.baseUrl}/transparencia');
    
    var response = await client.get(uri).timeout(ApiConfig.requestTimeout);
    if (response.statusCode == 200) {
      return model.transacaoFromJson(response.body);
    } else {
      throw Exception('Falha ao carregar as transações');
    }
  }
}
