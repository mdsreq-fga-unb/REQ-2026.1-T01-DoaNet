import 'package:http/http.dart' as http;
import 'feed_model.dart' as model;

class FetchFeed {
  Future<List<model.FeedItem>> fetchFeed() async {
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
