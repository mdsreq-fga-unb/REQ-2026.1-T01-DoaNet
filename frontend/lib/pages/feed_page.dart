import 'package:flutter/material.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';
import 'package:frontend/info_fetch/feed/feed_model.dart';
import 'package:frontend/info_fetch/feed/feed_filter.dart';
import 'package:frontend/widgets/feed_item_card.dart';
import 'package:frontend/config/org_config.dart';
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

  final TextEditingController _searchController = TextEditingController();
  String _searchQuery = '';
  FeedFilter _filter = FeedFilter.tudo;

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

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
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

  Future<void> _abrirFiltro(OrgConfig config) async {
    FeedFilter selecionado = _filter;

    final resultado = await showModalBottomSheet<FeedFilter>(
      context: context,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (sheetContext) {
        return StatefulBuilder(
          builder: (sheetContext, setSheetState) {
            Widget opcao(FeedFilter valor, String titulo, String subtitulo) {
              final ativa = selecionado == valor;
              return GestureDetector(
                onTap: () => setSheetState(() => selecionado = valor),
                child: Container(
                  width: double.infinity,
                  margin: const EdgeInsets.only(bottom: 12),
                  padding:
                      const EdgeInsets.symmetric(vertical: 14, horizontal: 16),
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(
                      color: ativa ? config.primaryColor : Colors.grey.shade300,
                      width: ativa ? 2 : 1,
                    ),
                  ),
                  child: Column(
                    children: [
                      Text(
                        titulo,
                        style: const TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Color(0xFF171616),
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        subtitulo,
                        style: TextStyle(
                          fontSize: 13,
                          color: Colors.grey.shade600,
                        ),
                      ),
                    ],
                  ),
                ),
              );
            }

            return Padding(
              padding: const EdgeInsets.fromLTRB(20, 20, 20, 24),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'Filtrar Feed',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF171616),
                    ),
                  ),
                  const SizedBox(height: 16),
                  opcao(FeedFilter.tudo, 'Tudo',
                      'Exibe posts e eventos juntos'),
                  opcao(FeedFilter.somentePublicacoes, 'Somente Publicações',
                      'Oculta os eventos do feed'),
                  opcao(FeedFilter.somenteEventos, 'Somente Eventos',
                      'Oculta os posts do feed'),
                  const SizedBox(height: 8),
                  SizedBox(
                    width: double.infinity,
                    height: 48,
                    child: ElevatedButton(
                      onPressed: () =>
                          Navigator.of(sheetContext).pop(selecionado),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: config.primaryColor,
                        foregroundColor: Colors.white,
                        elevation: 0,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(8),
                        ),
                      ),
                      child: const Text(
                        'Aplicar Filtro',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 4),
                  Center(
                    child: TextButton(
                      onPressed: () => Navigator.of(sheetContext).pop(),
                      child: Text(
                        'Cancelar',
                        style: TextStyle(color: Colors.grey.shade700),
                      ),
                    ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );

    if (resultado != null && mounted) {
      setState(() => _filter = resultado);
    }
  }

  @override
  Widget build(BuildContext context) {
    final config = OrgConfigProvider.of(context);
    final itensVisiveis = filterFeedItems(
      feedItems,
      filter: _filter,
      query: _searchQuery,
    );
    final filtroAtivo = _filter != FeedFilter.tudo;

    return Column(
      children: [
        // ── Barra de busca + botão de filtro ─────────────────────────
        Container(
          color: Colors.white,
          padding: const EdgeInsets.fromLTRB(12, 8, 12, 8),
          child: Row(
            children: [
              Expanded(
                child: TextField(
                  controller: _searchController,
                  onChanged: (valor) => setState(() => _searchQuery = valor),
                  textInputAction: TextInputAction.search,
                  decoration: InputDecoration(
                    hintText: 'Buscar publicações e eventos',
                    prefixIcon: const Icon(Icons.search, size: 20),
                    isDense: true,
                    contentPadding: const EdgeInsets.symmetric(vertical: 10),
                    filled: true,
                    fillColor: const Color(0xFFF2F2F2),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(24),
                      borderSide: BorderSide.none,
                    ),
                    enabledBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(24),
                      borderSide: BorderSide.none,
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(24),
                      borderSide: BorderSide(color: config.primaryColor),
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 8),
              IconButton(
                tooltip: 'Filtrar Feed',
                icon: const Icon(Icons.tune),
                color: filtroAtivo ? config.primaryColor : null,
                onPressed: () => _abrirFiltro(config),
              ),
            ],
          ),
        ),
        Expanded(
          child: Builder(
            builder: (context) {
              if (isLoading) {
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
              if (itensVisiveis.isEmpty) {
                return const Center(
                  child: Text('Nenhum resultado encontrado'),
                );
              }
              return ListView.builder(
                itemCount: itensVisiveis.length,
                itemBuilder: (context, index) {
                  final item = itensVisiveis[index];
                  return FeedItemCard(
                    title: item.title,
                    description: item.description,
                    profileName: (item.profileName == null || item.profileName!.isEmpty)
                        ? config.name
                        : item.profileName!,
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
        ),
      ],
    );
  }
}
