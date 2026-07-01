import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/info_fetch/feed/feed_model.dart';
import 'package:frontend/info_fetch/feed/feed_filter.dart';

FeedItem _item(String id, String title, String type) => FeedItem(
      id: id,
      title: title,
      description: 'desc',
      type: type,
    );

void main() {
  final items = [
    _item('1', 'Campanha do Agasalho', 'sem_evento'),
    _item('2', 'Mutirão de Limpeza', 'evento'),
    _item('3', 'Aula de Reforço', 'sem_evento'),
    _item('4', 'Feira Beneficente', 'evento'),
  ];

  group('filtro por tipo (US06)', () {
    test('FeedFilter.tudo retorna todos os itens', () {
      final resultado = filterFeedItems(items, filter: FeedFilter.tudo);
      expect(resultado.length, 4);
    });

    test('FeedFilter.somenteEventos retorna apenas eventos', () {
      final resultado =
          filterFeedItems(items, filter: FeedFilter.somenteEventos);
      expect(resultado.length, 2);
      expect(resultado.every(isEvento), isTrue);
    });

    test('FeedFilter.somentePublicacoes retorna apenas publicações', () {
      final resultado =
          filterFeedItems(items, filter: FeedFilter.somentePublicacoes);
      expect(resultado.length, 2);
      expect(resultado.every((i) => !isEvento(i)), isTrue);
    });
  });

  group('busca por título (US07)', () {
    test('filtra por título contendo o termo', () {
      final resultado = filterFeedItems(items, query: 'campanha');
      expect(resultado.length, 1);
      expect(resultado.first.title, 'Campanha do Agasalho');
    });

    test('não diferencia maiúsculas de minúsculas', () {
      final resultado = filterFeedItems(items, query: 'MUTIRÃO');
      expect(resultado.length, 1);
      expect(resultado.first.title, 'Mutirão de Limpeza');
    });

    test('busca vazia não altera o resultado', () {
      final resultado = filterFeedItems(items, query: '   ');
      expect(resultado.length, 4);
    });

    test('sem correspondência retorna lista vazia', () {
      final resultado = filterFeedItems(items, query: 'inexistente');
      expect(resultado, isEmpty);
    });
  });

  group('filtro combinado', () {
    test('aplica tipo e busca simultaneamente', () {
      final resultado = filterFeedItems(
        items,
        filter: FeedFilter.somenteEventos,
        query: 'feira',
      );
      expect(resultado.length, 1);
      expect(resultado.first.title, 'Feira Beneficente');
    });

    test('tipo e busca sem interseção retorna vazio', () {
      final resultado = filterFeedItems(
        items,
        filter: FeedFilter.somentePublicacoes,
        query: 'feira',
      );
      expect(resultado, isEmpty);
    });
  });
}
