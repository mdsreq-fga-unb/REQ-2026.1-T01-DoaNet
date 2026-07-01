import 'package:flutter/material.dart';
import 'org_config.dart';

class OrgConfigProvider extends InheritedWidget {
  final OrgConfig config;

  const OrgConfigProvider({
    super.key,
    required this.config,
    required super.child,
  });

  static OrgConfig of(BuildContext context) {
    final provider = context
        .dependOnInheritedWidgetOfExactType<OrgConfigProvider>();
    return provider?.config ?? OrgConfig.fallback;
  }

  @override
  bool updateShouldNotify(OrgConfigProvider old) =>
      config != old.config;
}