import 'dart:convert';
import 'package:http/http.dart' as http;
import '../../api_config.dart';
import '../../config/org_config.dart';

class FetchOrgConfig {
  final String orgId;

  FetchOrgConfig({required this.orgId});

  Future<OrgConfig> fetchConfig() async {
    final response = await http.get(
      Uri.parse('${ApiConfig.baseUrl}/orgs/$orgId/config'),
    ).timeout(ApiConfig.requestTimeout);

    if (response.statusCode == 200) {
      final json = jsonDecode(response.body) as Map<String, dynamic>;
      return OrgConfig.fromJson(json);
    }

    throw Exception('Erro ao carregar configurações da organização');
  }
}