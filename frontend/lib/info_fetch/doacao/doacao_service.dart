import 'dart:convert';
import 'package:http/http.dart' as http;
import '../../api_config.dart';
import 'doacao_model.dart';

class DoacaoService {
  Future<String> criarCheckoutSession(DoacaoRequest doacao) async {
    final response = await http.post(
      Uri.parse('${ApiConfig.baseUrl}/doacoes/checkout'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(doacao.toJson()),
    ).timeout(ApiConfig.requestTimeout);

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['checkout_url'] as String;
    }
    throw Exception('Erro ao criar sessão de pagamento: ${response.body}');
  }
}
