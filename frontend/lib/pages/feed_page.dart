import 'package:flutter/material.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';
import 'package:frontend/info_fetch/feed/feed_model.dart';
import 'package:frontend/widgets/feed_item_card.dart';

class FeedPage extends StatefulWidget {
  const FeedPage({super.key});

  @override
  State<FeedPage> createState() => FeedPageState();
}

class FeedPageState extends State<FeedPage> {
  List<FeedItem>? feedItems;
  var isLoaded = false;

  @override
  void initState() {
    super.initState();
    getData();
  }

  void getData() async {
    feedItems = await FetchFeed().fetchFeed();
    if (feedItems != null) {
      setState(() {
        isLoaded = true;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 2,
        shape: Border.all(color: Theme.of(context).dividerColor, width: 2),
        flexibleSpace: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            spacing: 4,
            children: [
              Container(
                decoration: BoxDecoration(
                  border: Border.all(
                    color: Theme.of(context).dividerColor,
                    width: 2,
                  ),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: const Padding(
                  padding: EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                  child: Column(
                    children: [
                      Text(
                        'Buscar Por Titulo',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              Container(
                decoration: BoxDecoration(
                  border: Border.all(
                    color: Theme.of(context).dividerColor,
                    width: 2,
                  ),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: const Padding(
                  padding: EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                  child: Column(
                    children: [
                      Text(
                        'Filtrar por Tipo',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
      body: ListView.builder(
        itemCount: feedItems?.length ?? 1,
        itemBuilder: (context, index) {
          return FeedItemCard(
            title: feedItems?[index].title ?? 'Título sem nome',
            description: feedItems?[index].description ?? '',
            profileName: 'Perfil',
            profileImageUrl: feedItems?[index].profileImageUrl,
            date: '01/01/2026',
          );
        },
      ),
    );
  }
}
