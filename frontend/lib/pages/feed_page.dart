import 'package:flutter/material.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';
import 'package:frontend/info_fetch/feed/feed_model.dart';
import 'package:frontend/widgets/feed_item_card.dart';
import 'package:frontend/config/org_config_provider.dart';

class FeedPage extends StatefulWidget {
  FeedPage({super.key, FetchFeed? fetchFeed})
    : fetchFeed = fetchFeed ?? FetchFeed();

  final FetchFeed fetchFeed;

  @override
  State<FeedPage> createState() => FeedPageState();
}

class FeedPageState extends State<FeedPage> {
  List<FeedItem> feedItems = [];
  bool isLoading = true;
  String? errorMessage;

  static const List<String> _meses = [
    '', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun',
    'jul', 'ago', 'set', 'out', 'nov', 'dez',
  ];

  String _formatDate(String? iso) {
    if (iso == null || iso.isEmpty) return '';
    final dt = DateTime.tryParse(iso);
    if (dt == null) return '';
    final local = dt.toLocal();
    return '${local.day} de ${_meses[local.month]}. de ${local.year}';
  }

  @override
  void initState() {
    super.initState();
    getData();
  }

  void getData() async {
    setState(() {
      isLoading = true;
      errorMessage = null;
    });

    try {
      final items = await widget.fetchFeed.fetchFeed();
      if (!mounted) {
        return;
      }
      setState(() {
        feedItems = items;
        isLoading = false;
      });
    } catch (_) {
      if (!mounted) {
        return;
      }
      setState(() {
        errorMessage = 'Erro ao carregar feed';
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        scrolledUnderElevation: 0,
        surfaceTintColor: Colors.transparent,
        flexibleSpace: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.center,
            spacing: 4,
            children: [
              const Icon(Icons.filter_list, size: 18),
              Container(
                decoration: BoxDecoration(
                  color: Colors.grey[350],
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: const [
                      Text('Com eventos', style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold)),
                    ],
                  ),
                ),
              ),
              Container(
                decoration: BoxDecoration(
                  color: Colors.grey[350],
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: const [
                      Text('Sem Eventos', style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold)),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
      body: Builder(
        builder: (context) {
          if (isLoading) {
            final config = OrgConfigProvider.of(context);
              return Center(
                child: CircularProgressIndicator(color: config.primaryColor),
              );
          }
          if (errorMessage != null) {
            return Center(child: Text(errorMessage!));
          }
          if (feedItems.isEmpty) {
            return const Center(child: Text('Nenhum item no feed'));
          }
          return ListView.builder(
            itemCount: feedItems.length,
            itemBuilder: (context, index) {
              final item = feedItems[index];
              return FeedItemCard(
                title: item.title,
                description: item.description,
                profileName: item.profileName ?? 'Perfil',
                profileImageUrl: item.profileImageUrl,
                date: _formatDate(item.createdAt),
                imageUrl: item.imageUrl,
                eventLinkUrl: item.eventLinkUrl,
                type: item.type,
                eventDate: item.eventDate,
                eventLocation: item.eventLocation,
              );
            },
          );
        },
      ),
    );
  }
}