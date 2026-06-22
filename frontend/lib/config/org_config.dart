import 'package:flutter/material.dart';

class OrgConfig {
  final String name;
  final String? logoUrl;
  final Color primaryColor;
  final Color backgroundColor;

  const OrgConfig({
    required this.name,
    this.logoUrl,
    required this.primaryColor,
    required this.backgroundColor,
  });

  factory OrgConfig.fromJson(Map<String, dynamic> json) {
    return OrgConfig(
      name: json['name'] as String,
      logoUrl: json['logo_url'] as String?,
      primaryColor: _hexToColor(json['primary_color'] as String),
      backgroundColor: _hexToColor(json['background_color'] as String),
    );
  }

  
  static const OrgConfig fallback = OrgConfig(
    name: 'MoveEduca',
    primaryColor: Color(0xFF0088FF),
    backgroundColor: Colors.white,
  );

  static Color _hexToColor(String hex) {
    final buffer = StringBuffer();
    if (hex.length == 7) buffer.write('ff');
    buffer.write(hex.replaceFirst('#', ''));
    return Color(int.parse(buffer.toString(), radix: 16));
  }
}