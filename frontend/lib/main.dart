import 'package:flutter/material.dart';

import 'page_structure.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'DoaNet Feed',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal),
      ),
      home: PageStructure(
        organizationName: 'Nome da Organizacao',
        initialPageName: 'feed',
      ),
    );
  }
}
