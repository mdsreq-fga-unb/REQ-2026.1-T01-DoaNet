import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/config/org_config.dart';
import 'package:frontend/config/org_config_provider.dart';
import 'package:frontend/info_fetch/feed/feed_model.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';
import 'package:frontend/pages/feed_page.dart';
import 'package:frontend/widgets/feed_item_card.dart';

class FakeFetchFeed extends FetchFeed {
  FakeFetchFeed(this.items);

  final List<FeedItem> items;

  @override
  Future<List<FeedItem>> fetchFeed() async {
    return items;
  }
}

Widget _withProvider(Widget child) {
  return OrgConfigProvider(
    config: OrgConfig.fallback,
    child: MaterialApp(home: Scaffold(body: child)),
  );
}

FeedItem _post(String id, String title) => FeedItem(
      id: id,
      title: title,
      description: 'Descricao $title',
      type: 'sem_evento',
      profileName: 'ONG X',
    );

FeedItem _evento(String id, String title) => FeedItem(
      id: id,
      title: title,
      description: 'Descricao $title',
      type: 'evento',
      profileName: 'ONG X',
    );

void main() {
  testWidgets('FeedPage renderiza busca, filtro e itens', (tester) async {
    final items = [_post('1', 'Titulo teste')];

    await tester.pumpWidget(
      _withProvider(FeedPage(fetchFeed: FakeFetchFeed(items))),
    );
    await tester.pumpAndSettle();

    expect(find.text('Buscar publicações e eventos'), findsOneWidget);
    expect(find.byIcon(Icons.tune), findsOneWidget);
    expect(find.text('Titulo teste'), findsOneWidget);
    expect(find.text('ONG X'), findsOneWidget);
  });

  testWidgets('FeedPage mostra mensagem de feed vazio', (tester) async {
    await tester.pumpWidget(
      _withProvider(FeedPage(fetchFeed: FakeFetchFeed(const []))),
    );
    await tester.pumpAndSettle();

    expect(find.text('Nenhum item no feed'), findsOneWidget);
    expect(find.byType(FeedItemCard), findsNothing);
  });

  testWidgets('Busca por título filtra em tempo real (case-insensitive)',
      (tester) async {
    final items = [
      _post('1', 'Campanha do Agasalho'),
      _post('2', 'Mutirão de Limpeza'),
    ];

    await tester.pumpWidget(
      _withProvider(FeedPage(fetchFeed: FakeFetchFeed(items))),
    );
    await tester.pumpAndSettle();

    expect(find.byType(FeedItemCard), findsNWidgets(2));

    await tester.enterText(find.byType(TextField), 'agasalho');
    await tester.pumpAndSettle();

    expect(find.text('Campanha do Agasalho'), findsOneWidget);
    expect(find.text('Mutirão de Limpeza'), findsNothing);
    expect(find.byType(FeedItemCard), findsOneWidget);
  });

  testWidgets('Busca sem resultado exibe mensagem informativa', (tester) async {
    final items = [_post('1', 'Campanha do Agasalho')];

    await tester.pumpWidget(
      _withProvider(FeedPage(fetchFeed: FakeFetchFeed(items))),
    );
    await tester.pumpAndSettle();

    await tester.enterText(find.byType(TextField), 'inexistente');
    await tester.pumpAndSettle();

    expect(find.text('Nenhum resultado encontrado'), findsOneWidget);
    expect(find.byType(FeedItemCard), findsNothing);
  });

  testWidgets('Filtro "Somente Eventos" oculta publicações', (tester) async {
    final items = [
      _post('1', 'Post normal'),
      _evento('2', 'Evento especial'),
    ];

    await tester.pumpWidget(
      _withProvider(FeedPage(fetchFeed: FakeFetchFeed(items))),
    );
    await tester.pumpAndSettle();

    // Abre o modal de filtro
    await tester.tap(find.byIcon(Icons.tune));
    await tester.pumpAndSettle();

    expect(find.text('Filtrar Feed'), findsOneWidget);

    // Seleciona "Somente Eventos" e aplica
    await tester.tap(find.text('Somente Eventos'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Aplicar Filtro'));
    await tester.pumpAndSettle();

    expect(find.text('Evento especial'), findsOneWidget);
    expect(find.text('Post normal'), findsNothing);
  });
}
