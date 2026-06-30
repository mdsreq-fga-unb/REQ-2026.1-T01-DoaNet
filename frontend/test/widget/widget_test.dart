import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/config/org_config.dart';
import 'package:frontend/config/org_config_provider.dart';
import 'package:frontend/page_structure.dart';

void main() {
  testWidgets('PageStructure switches tabs', (WidgetTester tester) async {
    await tester.pumpWidget(
      OrgConfigProvider(
        config: OrgConfig.fallback,
        child: const MaterialApp(
          home: PageStructure(
            initialPageName: 'colaboracao',
          ),
        ),
      ),
    );

    await tester.pumpAndSettle();

    expect(find.byType(BottomNavigationBar), findsOneWidget);
    expect(find.text(OrgConfig.fallback.name), findsOneWidget);
    expect(find.text('Feed'), findsWidgets);
    expect(find.text('Colaboração'), findsWidgets);
    expect(find.text('Transparência'), findsWidgets);

    await tester.tap(find.text('Transparência').first);
    await tester.pumpAndSettle();

    expect(find.text('Transparencia'), findsOneWidget);
  });
}