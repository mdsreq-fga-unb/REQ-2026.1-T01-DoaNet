import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:frontend/config/org_config_provider.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';

import 'pages/colaboracao_page.dart';
import 'pages/feed_page.dart';
import 'pages/transparencia_page.dart';

class PageStructure extends StatefulWidget {
  const PageStructure({
    super.key,
    required this.initialPageName,
    this.fetchFeed,
  });

  final String initialPageName;
  final FetchFeed? fetchFeed;

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
        return FeedPage(fetchFeed: widget.fetchFeed);
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
    final config = OrgConfigProvider.of(context);
    final String firstLetter = config.name.isNotEmpty
        ? config.name[0].toUpperCase()
        : '?';

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        surfaceTintColor: Colors.transparent,
        elevation: 1,
        shadowColor: const Color(0xFFD9D9D9),
        title: config.logoUrl != null
            ? Image.network(config.logoUrl!, height: 32)
            : Text(
                config.name,
                style: TextStyle(
                  color: config.primaryColor,
                  fontWeight: FontWeight.bold,
                  fontSize: 26,
                  fontFamily: 'Roboto',
                ),
              ),
        actions: [
          Padding(
            padding: const EdgeInsets.only(right: 24.0),
            child: CircleAvatar(
              backgroundColor: const Color(0xFFF5F5F5),
              radius: 18,
              child: Text(
                firstLetter,
                style: TextStyle(
                  color: config.primaryColor,
                  fontFamily: 'Abyssinica SIL',
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
        ],
      ),
      
      body: ColoredBox(
        color: config.backgroundColor,
        child: _pageForName(),
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex(),
        selectedItemColor: config.primaryColor,
        unselectedItemColor: const Color(0xFF505050),
        backgroundColor: Colors.white,
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
        items: [
          BottomNavigationBarItem(
            icon: SvgPicture.asset(
              'assets/icons/feed.svg',
              height: 24,
              colorFilter: const ColorFilter.mode(Color(0xFF505050), BlendMode.srcIn),
            ),
            activeIcon: SvgPicture.asset(
              'assets/icons/feed.svg',
              height: 24,
              colorFilter: ColorFilter.mode(config.primaryColor, BlendMode.srcIn),
            ),
            label: 'Feed',
          ),
          BottomNavigationBarItem(
            icon: SvgPicture.asset(
              'assets/icons/colaboracao.svg',
              height: 24,
              colorFilter: const ColorFilter.mode(Color(0xFF505050), BlendMode.srcIn),
            ),
            activeIcon: SvgPicture.asset(
              'assets/icons/colaboracao.svg',
              height: 24,
              colorFilter: ColorFilter.mode(config.primaryColor, BlendMode.srcIn),
            ),
            label: 'Colaboração',
          ),
          BottomNavigationBarItem(
            icon: SvgPicture.asset(
              'assets/icons/transparencia.svg',
              height: 24,
              colorFilter: const ColorFilter.mode(Color(0xFF505050), BlendMode.srcIn),
            ),
            activeIcon: SvgPicture.asset(
              'assets/icons/transparencia.svg',
              height: 24,
              colorFilter: ColorFilter.mode(config.primaryColor, BlendMode.srcIn),
            ),
            label: 'Transparência',
          ),
        ],
      ),
    );
  }
}