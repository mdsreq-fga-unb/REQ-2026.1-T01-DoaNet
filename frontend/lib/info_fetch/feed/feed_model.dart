import 'dart:convert';

List<FeedItem> feedFromJson(String str) =>
    List<FeedItem>.from(json.decode(str).map((x) => FeedItem.fromJson(x)));

String feedToJson(List<FeedItem> data) =>
    json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class FeedItem {
  String id;
  String title;
  String description;
  String type;
  String? imageUrl;
  String? profileName;
  String? profileImageUrl;
  String? eventLinkUrl;
  String? eventDate;
  String? eventLocation;

  FeedItem({
    required this.id,
    required this.title,
    required this.description,
    required this.type,
    this.imageUrl,
    this.profileName,
    this.profileImageUrl,
    this.eventLinkUrl,
    this.eventDate,
    this.eventLocation,
  });

  factory FeedItem.fromJson(Map<String, dynamic> json) => FeedItem(
    id: json["id"],
    title: json["title"],
    description: json["description"],
    type: json["type"],
    imageUrl: json["image_url"],
    profileName: json["profile_name"],
    profileImageUrl: json["profile_image_url"],
    eventLinkUrl: json["event_url"],
    eventDate: json["event_date"],
    eventLocation: json["event_location"]
  );
  Map<String, dynamic> toJson() => {
    "id": id,
    "title": title,
    "description": description,
    "type": type,
    "image_url": imageUrl,
    "profile_name": profileName,
    "profile_image_url": profileImageUrl,
    "event_url": eventLinkUrl,
    "event_date": eventDate,
    "event_location": eventLocation,
  };
}
