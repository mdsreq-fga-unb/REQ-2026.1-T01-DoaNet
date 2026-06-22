import 'dart:convert';
import 'package:http/http.dart' as http;
import '../../config/org_config.dart';

class FetchOrgConfig {
  final String orgId;

  FetchOrgConfig({required this.orgId});

  Future<OrgConfig> fetchConfig() async {
    final response = await http.get(
      Uri.parse('https://sua-api.com/orgs/$orgId/config'),
    );

    if (response.statusCode == 200) {
      final json = jsonDecode(response.body) as Map<String, dynamic>;
      return OrgConfig.fromJson(json);
    }

    throw Exception('Erro ao carregar configurações da organização');
  }
}