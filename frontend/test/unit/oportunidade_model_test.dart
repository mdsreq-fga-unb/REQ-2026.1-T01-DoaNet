import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/info_fetch/oportunidades/oportunidade_model.dart';

void main() {
  test('oportunidadeFromJson faz parse do link_inscricao', () {
    const jsonString =
        '[\n'
        '  {\n'
        '    "id": "1",\n'
        '    "titulo": "Professor de Reforço",\n'
        '    "descricao": "Apoio escolar",\n'
        '    "local": "Asa Norte",\n'
        '    "horario": "Sáb 9h",\n'
        '    "link_inscricao": "https://forms.example.com/inscricao",\n'
        '    "ativo": true\n'
        '  }\n'
        ']';

    final items = oportunidadeFromJson(jsonString);

    expect(items, hasLength(1));
    expect(items.first.linkInscricao, 'https://forms.example.com/inscricao');
    expect(items.first.titulo, 'Professor de Reforço');
  });

  test('linkInscricao é null quando ausente no JSON', () {
    final item = OportunidadeItem.fromJson({
      'id': '2',
      'titulo': 'Vaga sem link',
      'descricao': 'desc',
      'local': 'Local',
      'horario': 'Horário',
      'ativo': true,
    });

    expect(item.linkInscricao, isNull);
  });
}
