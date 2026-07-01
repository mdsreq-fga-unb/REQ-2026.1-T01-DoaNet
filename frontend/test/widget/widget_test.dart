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

    expect(find.text('MoveEduca'), findsOneWidget);
    expect(find.text('Colaboracao'), findsOneWidget);
    expect(find.byIcon(Icons.home_outlined), findsOneWidget);
    expect(find.byIcon(Icons.volunteer_activism_outlined), findsOneWidget);
    expect(find.byIcon(Icons.grade_sharp), findsOneWidget);

    await tester.tap(find.byIcon(Icons.grade_sharp));
    await tester.pumpAndSettle();

    expect(find.text('Transparencia'), findsOneWidget);
    print('OK: PageStructure switches tabs');
  });
}
