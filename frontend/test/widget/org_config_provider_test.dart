import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/config/org_config.dart';
import 'package:frontend/config/org_config_provider.dart';

void main() {
  testWidgets('OrgConfigProvider provides config to descendants', (tester) async {
    const testConfig = OrgConfig(
      name: 'TesteOrg',
      description: 'Descrição teste',
      primaryColor: Color(0xFFFF0000),
      backgroundColor: Color(0xFFFFFFFF),
    );

    OrgConfig? capturedConfig;

    await tester.pumpWidget(
      OrgConfigProvider(
        config: testConfig,
        child: Builder(
          builder: (context) {
            capturedConfig = OrgConfigProvider.of(context);
            return const SizedBox();
          },
        ),
      ),
    );

    expect(capturedConfig, isNotNull);
    expect(capturedConfig!.name, 'TesteOrg');
    expect(capturedConfig!.primaryColor, const Color(0xFFFF0000));
    print('OK: OrgConfigProvider provides config to descendants');
  });

  testWidgets('OrgConfigProvider returns fallback when not in tree', (tester) async {
    OrgConfig? capturedConfig;

    await tester.pumpWidget(
      Builder(
        builder: (context) {
          capturedConfig = OrgConfigProvider.of(context);
          return const SizedBox();
        },
      ),
    );

    expect(capturedConfig, isNotNull);
    expect(capturedConfig!.name, OrgConfig.fallback.name);
    print('OK: OrgConfigProvider returns fallback when not in tree');
  });
}