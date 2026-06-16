import 'package:flutter/material.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';

import 'page_structure.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key, this.fetchFeed});

  final FetchFeed? fetchFeed;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'DoaNet Feed',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.lightBlue,
          onSecondary: Colors.blueAccent,
          onPrimaryContainer: Colors.white,
          primaryContainer: Colors.blueAccent,
        ),
      ),
      home: PageStructure(
        organizationName: 'MoveEduca',
        initialPageName: 'feed',
        fetchFeed: fetchFeed,
      ),
    );
  }
}
