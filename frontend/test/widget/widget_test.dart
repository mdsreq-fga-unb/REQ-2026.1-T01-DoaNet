import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/page_structure.dart';

void main() {
  testWidgets('PageStructure switches tabs', (WidgetTester tester) async {
    await tester.pumpWidget(
      const MaterialApp(
        home: PageStructure(
          organizationName: 'MoveEduca',
          initialPageName: 'colaboracao',
        ),
      ),
    );

    await tester.pumpAndSettle();

    expect(find.byType(BottomNavigationBar), findsOneWidget);
    expect(find.text('Feed'), findsWidgets);
    expect(find.text('Colaboração'), findsWidgets);
    expect(find.text('Transparência'), findsWidgets);

    await tester.tap(find.text('Transparência').first);
    await tester.pumpAndSettle();

    expect(find.text('Transparencia'), findsOneWidget);
  });
}
