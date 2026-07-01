import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';
import 'package:frontend/info_fetch/feed/feed_model.dart';
import 'package:frontend/main.dart';
import 'package:frontend/widgets/feed_item_card.dart';

class FakeFetchFeed extends FetchFeed {
  FakeFetchFeed(this.items);

  final List<FeedItem> items;

  @override
  Future<List<FeedItem>> fetchFeed() async {
    return items;
  }
}

class ErrorFetchFeed extends FetchFeed {
  @override
  Future<List<FeedItem>> fetchFeed() async {
    throw Exception('Network error');
  }
}

FeedItem buildFeedItem({
  required String id,
  required String title,
  required String description,
}) {
  return FeedItem(
    id: id,
    title: title,
    description: description,
    type: 'event',
    profileName: null,
    profileImageUrl: null,
    imageUrl: null,
    eventLinkUrl: null,
  );
}

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('Integration: feed loads items', (tester) async {
    final items = [
      buildFeedItem(
        id: '1',
        title: 'Titulo teste',
        description: 'Descricao teste',
      ),
    ];

    await tester.pumpWidget(MyApp(fetchFeed: FakeFetchFeed(items)));
    await tester.pumpAndSettle();

    expect(find.text('Buscar publicações e eventos'), findsOneWidget);
    expect(find.byIcon(Icons.tune), findsOneWidget);
    expect(find.text('Titulo teste'), findsOneWidget);
    expect(find.text('Descricao teste'), findsOneWidget);
    expect(find.byType(FeedItemCard), findsOneWidget);
  });

  testWidgets('Integration: feed empty state', (tester) async {
    await tester.pumpWidget(MyApp(fetchFeed: FakeFetchFeed(const [])));
    await tester.pumpAndSettle();

    expect(find.text('Buscar publicações e eventos'), findsOneWidget);
    expect(find.byIcon(Icons.tune), findsOneWidget);
    expect(find.text('Nenhum item no feed'), findsOneWidget);
    expect(find.byType(FeedItemCard), findsNothing);
  });

  testWidgets('Integration: feed error state', (tester) async {
    await tester.pumpWidget(MyApp(fetchFeed: ErrorFetchFeed()));
    await tester.pumpAndSettle();

    expect(find.text('Erro ao carregar feed'), findsOneWidget);
  });

  testWidgets('Integration: navigation between tabs', (tester) async {
    await tester.pumpWidget(MyApp(fetchFeed: FakeFetchFeed(const [])));
    await tester.pumpAndSettle();

    await tester.tap(find.byIcon(Icons.volunteer_activism_outlined));
    await tester.pumpAndSettle();

    expect(find.text('Colaboracao'), findsOneWidget);

    await tester.tap(find.byIcon(Icons.grade_sharp));
    await tester.pumpAndSettle();

    expect(find.text('Transparencia'), findsOneWidget);
  });

  testWidgets('Integration: feed visible after tab switch', (tester) async {
    final items = [
      buildFeedItem(
        id: '1',
        title: 'Titulo persistente',
        description: 'Descricao persistente',
      ),
    ];

    await tester.pumpWidget(MyApp(fetchFeed: FakeFetchFeed(items)));
    await tester.pumpAndSettle();

    expect(find.text('Titulo persistente'), findsOneWidget);

    await tester.tap(find.byIcon(Icons.grade_sharp));
    await tester.pumpAndSettle();

    await tester.tap(find.byIcon(Icons.home_outlined));
    await tester.pumpAndSettle();

    expect(find.text('Titulo persistente'), findsOneWidget);
  });
}
