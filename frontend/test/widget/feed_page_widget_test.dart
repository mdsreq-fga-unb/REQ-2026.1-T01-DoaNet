import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
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

void main() {
  testWidgets('FeedPage renders filters and items', (tester) async {
    final items = [
      FeedItem(
        id: '1',
        title: 'Titulo teste',
        description: 'Descricao teste',
        type: 'event',
        profileName: 'ONG X',
        profileImageUrl: null,
        imageUrl: null,
        eventLinkUrl: null,
      ),
    ];

    await tester.pumpWidget(
      MaterialApp(home: FeedPage(fetchFeed: FakeFetchFeed(items))),
    );

    await tester.pumpAndSettle();

    expect(find.text('Com eventos'), findsOneWidget);
    expect(find.text('Sem Eventos'), findsOneWidget);
    expect(find.text('Titulo teste'), findsOneWidget);
    expect(find.text('Descricao teste'), findsOneWidget);
    expect(find.text('Perfil'), findsOneWidget);
    print('OK: FeedPage renders filters and items');
  });

  testWidgets('FeedPage renders filters with empty feed', (tester) async {
    await tester.pumpWidget(
      MaterialApp(home: FeedPage(fetchFeed: FakeFetchFeed(const []))),
    );

    await tester.pumpAndSettle();

    expect(find.text('Com eventos'), findsOneWidget);
    expect(find.text('Sem Eventos'), findsOneWidget);
    expect(find.text('Nenhum item no feed'), findsOneWidget);
    expect(find.byType(FeedItemCard), findsNothing);
    print('OK: FeedPage renders filters with empty feed');
  });
}
