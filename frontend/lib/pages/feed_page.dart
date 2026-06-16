import 'package:flutter/material.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';
import 'package:frontend/info_fetch/feed/feed_model.dart';
import 'package:frontend/widgets/feed_item_card.dart';

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
            return const Center(child: CircularProgressIndicator());
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
                date: '01/01/2026',
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