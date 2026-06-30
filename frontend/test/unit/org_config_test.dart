import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/config/org_config.dart';

void main() {
  test('OrgConfig.fromJson parses correctly', () {
    final json = {
      'org_id': 'move-educa',
      'name': 'MoveEduca',
      'description': 'Uma ONG incrível',
      'primary_color': '#0088FF',
      'background_color': '#FFFFFF',
      'logo_url': 'https://example.com/logo.png',
    };

    final config = OrgConfig.fromJson(json);

    expect(config.orgId, 'move-educa');
    expect(config.name, 'MoveEduca');
    expect(config.description, 'Uma ONG incrível');
    expect(config.primaryColor, const Color(0xFF0088FF));
    expect(config.backgroundColor, const Color(0xFFFFFFFF));
    expect(config.logoUrl, 'https://example.com/logo.png');
    print('OK: OrgConfig.fromJson parses correctly');
  });

  test('OrgConfig.fromJson handles null logo_url', () {
    final json = {
      'org_id': 'move-educa',
      'name': 'MoveEduca',
      'description': 'Uma ONG incrível',
      'primary_color': '#FF0000',
      'background_color': '#FFFFFF',
      'logo_url': null,
    };

    final config = OrgConfig.fromJson(json);

    expect(config.logoUrl, isNull);
    print('OK: OrgConfig.fromJson handles null logo_url');
  });

  test('OrgConfig.fromJson uses fallback org_id when null', () {
    final json = {
      'name': 'MoveEduca',
      'description': 'Uma ONG incrível',
      'primary_color': '#FF0000',
      'background_color': '#FFFFFF',
      'logo_url': null,
    };

    final config = OrgConfig.fromJson(json);

    expect(config.orgId, 'move-educa');
    print('OK: OrgConfig.fromJson uses fallback org_id when null');
  });

  test('OrgConfig.fallback has valid values', () {
    const config = OrgConfig.fallback;

    expect(config.orgId, isNotEmpty);
    expect(config.name, isNotEmpty);
    expect(config.description, isNotEmpty);
    expect(config.primaryColor, isNotNull);
    expect(config.backgroundColor, isNotNull);
    print('OK: OrgConfig.fallback has valid values');
  });

  test('_hexToColor parses hex correctly', () {
    final json = {
      'org_id': 'teste',
      'name': 'Teste',
      'description': 'Teste',
      'primary_color': '#FF4B4B',
      'background_color': '#FAFAFA',
      'logo_url': null,
    };

    final config = OrgConfig.fromJson(json);

    expect(config.primaryColor.red, 255);
    expect(config.primaryColor.green, 75);
    expect(config.primaryColor.blue, 75);
    print('OK: _hexToColor parses hex correctly');
  });
}