import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/info_fetch/doacao/doacao_model.dart';

void main() {
  test('toJson inclui is_anonima true quando anonima', () {
    final req = DoacaoRequest(
      valor: 50.0,
      visibilidade: VisibilidadeDoacao.anonima,
      direcao: DirecaoDoacao.instituicao,
    );
    final json = req.toJson();

    expect(json['is_anonima'], isTrue);
    expect(json.containsKey('nome_doador'), isFalse);
    print('OK: toJson anonima');
  });

  test('toJson inclui nome_doador quando publica com nome preenchido', () {
    final req = DoacaoRequest(
      valor: 50.0,
      visibilidade: VisibilidadeDoacao.publica,
      nomeDoador: 'Pedro',
      direcao: DirecaoDoacao.instituicao,
    );
    final json = req.toJson();

    expect(json['is_anonima'], isFalse);
    expect(json['nome_doador'], 'Pedro');
    print('OK: toJson publica com nome');
  });

  test('toJson nao inclui nome_doador quando string vazia', () {
    final req = DoacaoRequest(
      valor: 50.0,
      visibilidade: VisibilidadeDoacao.publica,
      nomeDoador: '',
      direcao: DirecaoDoacao.instituicao,
    );
    final json = req.toJson();

    expect(json.containsKey('nome_doador'), isFalse);
    print('OK: toJson nome vazio nao incluido');
  });

  test('toJson inclui nome_projeto quando direcao e projeto', () {
    final req = DoacaoRequest(
      valor: 100.0,
      visibilidade: VisibilidadeDoacao.publica,
      nomeDoador: 'Pedro',
      direcao: DirecaoDoacao.projeto,
      nomeProjeto: 'Aulas de Reforco',
    );
    final json = req.toJson();

    expect(json['direcao'], 'projeto');
    expect(json['nome_projeto'], 'Aulas de Reforco');
    print('OK: toJson direcao projeto com nome_projeto');
  });

  test('toJson nao inclui nome_projeto quando direcao e instituicao', () {
    final req = DoacaoRequest(
      valor: 50.0,
      visibilidade: VisibilidadeDoacao.publica,
      nomeDoador: 'Pedro',
      direcao: DirecaoDoacao.instituicao,
    );
    final json = req.toJson();

    expect(json['direcao'], 'instituicao');
    expect(json.containsKey('nome_projeto'), isFalse);
    print('OK: toJson direcao instituicao sem nome_projeto');
  });

  test('toJson inclui valor correto', () {
    final req = DoacaoRequest(
      valor: 123.45,
      visibilidade: VisibilidadeDoacao.anonima,
      direcao: DirecaoDoacao.instituicao,
    );
    final json = req.toJson();

    expect(json['valor'], 123.45);
    print('OK: toJson valor correto');
  });
}
