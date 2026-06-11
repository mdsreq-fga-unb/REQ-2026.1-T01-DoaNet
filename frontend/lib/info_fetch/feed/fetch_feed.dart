import 'package:http/http.dart' as http;
import 'feed_model.dart' as model;

class FetchFeed {
  final bool useMock;

  FetchFeed({this.useMock = false});

  Future<List<model.FeedItem>> fetchFeed() async {
    if (useMock) return _mockItems();

    var client = http.Client();
    var uri = Uri.parse('http://localhost:8000/feed');
    var response = await client.get(uri);
    if (response.statusCode == 200) {
      return model.feedFromJson(response.body);
    } else {
      throw Exception('Failed to load Feed Item');
    }
  }
}

  List<model.FeedItem> _mockItems() {
    return [
      model.FeedItem(
        id: '1',
        title: 'Campanha de Agasalho',
        description: 'Doe roupas de inverno para quem precisa. Juntos fazemos a diferença!',
        type: 'post',
        profileName: 'MoveEduca',
        profileImageUrl: null,
        imageUrl: 'https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg',
        eventLinkUrl: null,
        eventDate: null,
        eventLocation: null,
      ),
      model.FeedItem(
        id: '2',
        title: 'Palestra: Cidadania e Voluntariado',
        description: 'A MoveEduca convida a comunidade para uma palestra sobre a importância da cidadania e voluntariado.',
        type: 'evento',
        profileName: 'MoveEduca',
        profileImageUrl: null,
        imageUrl: null,
        eventLinkUrl: 'https://github.com/dashboard',
        eventDate: '15\nJUN',
        eventLocation: 'Asa Norte, Brasília',
      ),
      model.FeedItem(
        id: '3',
        title: 'Teste',
        description: 'teste teste teste.',
        type: 'post',
        profileName: 'MoveEduca',
        profileImageUrl: null,
        imageUrl: null,
        eventLinkUrl: null,
        eventDate: null,
        eventLocation: null,
      ),
    ];
  }