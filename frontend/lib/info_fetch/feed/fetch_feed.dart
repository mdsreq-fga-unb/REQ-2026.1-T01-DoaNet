import 'package:http/http.dart' as http;
import 'package:frontend/api_config.dart';
import 'feed_model.dart' as model;

class FetchFeed {
  final String orgId;

  FetchFeed({this.orgId = ''});

  Future<List<model.FeedItem>> fetchFeed() async {

    var client = http.Client();
    var uri = Uri.parse('${ApiConfig.baseUrl}/feed?org_id=$orgId');
    var response = await client.get(uri);
    if (response.statusCode == 200) {
      return model.feedFromJson(response.body);
    } else {
      throw Exception('Failed to load Feed Item');
    }
  }
}