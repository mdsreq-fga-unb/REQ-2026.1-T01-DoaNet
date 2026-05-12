import 'package:flutter/material.dart';

import 'pages/colaboracao_page.dart';
import 'pages/feed_page.dart';
import 'pages/transparencia_page.dart';

class PageStructure extends StatefulWidget {
  const PageStructure({
    super.key,
    required this.organizationName,
    required this.initialPageName,
  });

  final String organizationName;
  final String initialPageName;

  @override
  State<PageStructure> createState() => _PageStructureState();
}

class _PageStructureState extends State<PageStructure> {
  late String _pageName;

  @override
  void initState() {
    super.initState();
    _pageName = widget.initialPageName;
  }

  int _currentIndex() {
    switch (_pageName) {
      case 'feed':
        return 0;
      case 'colaboracao':
        return 1;
      case 'transparencia':
        return 2;
      default:
        return 0;
    }
  }

  Widget _pageForName() {
    switch (_pageName) {
      case 'feed':
        return const FeedPage();
      case 'colaboracao':
        return const ColaboracaoPage();
      case 'transparencia':
        return const TransparenciaPage();
      default:
        return const Center(child: Text('Pagina desconhecida'));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.organizationName),
      ),
      body: _pageForName(),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex(),
        onTap: (index) {
          setState(() {
            switch (index) {
              case 0:
                _pageName = 'feed';
                break;
              case 1:
                _pageName = 'colaboracao';
                break;
              case 2:
                _pageName = 'transparencia';
                break;
              default:
                _pageName = 'feed';
            }
          });
        },
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home_outlined),
            label: 'Feed',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.volunteer_activism_outlined),
            label: 'Colaboração',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.grade_sharp),
            label: 'Transparência',
          ),
        ],
      ),
    );
  }
}
