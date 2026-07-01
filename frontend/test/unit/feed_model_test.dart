import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/info_fetch/feed/feed_model.dart';

void main() {
  test('feedFromJson parses items', () {
    const jsonString =
        '[\n'
        '  {\n'
        '    "id": "1",\n'
        '    "title": "Titulo X",\n'
        '    "description": "Descricao X",\n'
        '    "type": "event",\n'
        '    "image_url": "http://example.com/image.png",\n'
        '    "profile_name": "ONG X",\n'
        '    "profile_image_url": "http://example.com/profile.png",\n'
        '    "event_url": "http://example.com/event"\n'
        '  }\n'
        ']';

    final items = feedFromJson(jsonString);

    expect(items, hasLength(1));
    final item = items.first;
    expect(item.id, '1');
    expect(item.title, 'Titulo X');
    expect(item.description, 'Descricao X');
    expect(item.type, 'event');
    expect(item.imageUrl, 'http://example.com/image.png');
    expect(item.profileName, 'ONG X');
    expect(item.profileImageUrl, 'http://example.com/profile.png');
    expect(item.eventLinkUrl, 'http://example.com/event');
    print('OK: feedFromJson parses items');
  });

  test('feedFromJson parses empty list', () {
    const jsonString = '[]';

    final items = feedFromJson(jsonString);

    expect(items, isEmpty);
    print('OK: feedFromJson parses empty list');
  });

  test('feedFromJson keeps optional fields null', () {
    const jsonString =
        '[\n'
        '  {\n'
        '    "id": "1",\n'
        '    "title": "Titulo X",\n'
        '    "description": "Descricao X",\n'
        '    "type": "event"\n'
        '  }\n'
        ']';

    final item = feedFromJson(jsonString).first;

    expect(item.imageUrl, isNull);
    expect(item.profileName, isNull);
    expect(item.profileImageUrl, isNull);
    expect(item.eventLinkUrl, isNull);
    print('OK: feedFromJson keeps optional fields null');
  });

  test('feedFromJson throws on invalid JSON', () {
    const jsonString = '[{"id": "1"}';

    expect(() => feedFromJson(jsonString), throwsFormatException);
    print('OK: feedFromJson throws on invalid JSON');
  });
}
