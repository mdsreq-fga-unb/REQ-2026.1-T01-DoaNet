import 'feed_model.dart';

/// Tipo usado pelo backend para identificar uma publicação de evento.
const String kFeedEventType = 'evento';

/// Opções de filtro do feed (espelham o protótipo "Filtrar Feed").
enum FeedFilter { tudo, somentePublicacoes, somenteEventos }

/// Retorna true se o item é uma publicação de evento.
bool isEvento(FeedItem item) => item.type == kFeedEventType;

/// Aplica o filtro por tipo (US06) e a busca por título (US07).
///
/// - [filter]: restringe por tipo (tudo / somente publicações / somente eventos).
/// - [query]: busca por título, sem diferenciar maiúsculas de minúsculas.
List<FeedItem> filterFeedItems(
  List<FeedItem> items, {
  FeedFilter filter = FeedFilter.tudo,
  String query = '',
}) {
  Iterable<FeedItem> result = items;

  switch (filter) {
    case FeedFilter.somenteEventos:
      result = result.where(isEvento);
      break;
    case FeedFilter.somentePublicacoes:
      result = result.where((item) => !isEvento(item));
      break;
    case FeedFilter.tudo:
      break;
  }

  final normalized = query.trim().toLowerCase();
  if (normalized.isNotEmpty) {
    result = result.where(
      (item) => item.title.toLowerCase().contains(normalized),
    );
  }

  return result.toList();
}
