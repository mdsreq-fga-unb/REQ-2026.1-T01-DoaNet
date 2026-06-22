import 'package:flutter/material.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';
import 'package:frontend/config/org_config.dart';
import 'package:frontend/config/org_config_provider.dart';
import 'package:frontend/info_fetch/org/fetch_org_config.dart';
import 'package:frontend/page_structure.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  OrgConfig config;
  try {
    config = await FetchOrgConfig(orgId: 'move-educa').fetchConfig();
  } catch (_) {
    config = OrgConfig.fallback;
  }

  runApp(
    OrgConfigProvider(
      config: config,
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key, this.fetchFeed});

  final FetchFeed? fetchFeed;

  @override
  Widget build(BuildContext context) {
    final config = OrgConfigProvider.of(context);

    return MaterialApp(
      title: config.name,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: config.primaryColor,
          onSecondary: config.primaryColor,
          onPrimaryContainer: Colors.white,
          primaryContainer: config.primaryColor,
        ),
      ),
      home: PageStructure(
        initialPageName: 'feed',
        fetchFeed: fetchFeed,
      ),
    );
  }
}