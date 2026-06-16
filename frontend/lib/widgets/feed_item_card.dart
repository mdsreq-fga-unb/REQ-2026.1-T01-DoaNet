import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

class FeedItemCard extends StatefulWidget {
  const FeedItemCard({
    super.key,
    this.title = 'Título Padrão',
    this.description = '',
    this.profileName = 'Perfil',
    this.profileImageUrl,
    this.date = '01/01/2026',
    this.imageUrl,
    this.eventLinkUrl,
    this.type = '',
    this.eventDate,
    this.eventLocation,
  });

  final String title;
  final String description;
  final String profileName;
  final String? profileImageUrl;
  final String date;
  final String? imageUrl;
  final String? eventLinkUrl;
  final String type;
  final String? eventDate;
  final String? eventLocation;

  @override
  State<FeedItemCard> createState() => _FeedItemCardState();
}

class _FeedItemCardState extends State<FeedItemCard> {
  bool _expanded = false;

  @override
  Widget build(BuildContext context) {
    if (widget.type == 'evento') {
      return _buildEventCard(context);
    }
    return _buildPostCard(context);
  }

  Widget _buildPostCard(BuildContext context) {
    final theme = Theme.of(context);
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                CircleAvatar(
                  radius: 21,
                  backgroundColor: theme.colorScheme.primaryContainer,
                  backgroundImage: widget.profileImageUrl != null && widget.profileImageUrl!.isNotEmpty
                      ? NetworkImage(widget.profileImageUrl!) : null,
                  child: widget.profileImageUrl == null || widget.profileImageUrl!.isEmpty
                      ? Text(
                          widget.profileName.isNotEmpty ? widget.profileName[0].toUpperCase() : '?',
                          style: theme.textTheme.titleMedium?.copyWith(
                            color: theme.colorScheme.onPrimaryContainer,
                            fontWeight: FontWeight.bold,
                          ),
                        )
                      : null,
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(widget.profileName, style: theme.textTheme.titleMedium?.copyWith(fontWeight: FontWeight.w600)),
                      const SizedBox(height: 1),
                      Text(widget.date, style: theme.textTheme.labelMedium),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            if (widget.imageUrl != null && widget.imageUrl!.isNotEmpty) ...[
              ClipRRect(
                borderRadius: BorderRadius.circular(8),
                child: Image.network(
                  widget.imageUrl!,
                  width: double.infinity,
                  fit: BoxFit.cover,
                  errorBuilder: (_, _, _) => const SizedBox.shrink(),
                ),
              ),
              const SizedBox(height: 12),
            ],
            Text(widget.title, style: theme.textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold)),
            if (widget.description.isNotEmpty) ...[
              const SizedBox(height: 8),
              Text(widget.description, style: theme.textTheme.bodyMedium),
            ],
          ],
        ),
      ),
    );
  }

  Widget _buildEventCard(BuildContext context) {
    final theme = Theme.of(context);
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: InkWell(
        borderRadius: BorderRadius.circular(12),
        onTap: () => setState(() => _expanded = !_expanded),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 12),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  if (widget.eventDate != null) ...[
                    Container(
                      width: 48,
                      padding: const EdgeInsets.symmetric(vertical: 6),
                      decoration: BoxDecoration(
                        color: theme.colorScheme.primaryContainer,
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: Text(
                        widget.eventDate!,
                        textAlign: TextAlign.center,
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                          color: theme.colorScheme.onPrimaryContainer,
                          height: 1.3,
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                  ],
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(widget.title, style: theme.textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold)),
                        if (widget.eventLocation != null) ...[
                          const SizedBox(height: 4),
                          Row(
                            children: [
                              Icon(Icons.location_on_outlined, size: 14, color: theme.colorScheme.primary),
                              const SizedBox(width: 4),
                              Text(widget.eventLocation!, style: theme.textTheme.labelMedium),
                            ],
                          ),
                        ],
                      ],
                    ),
                  ),
                  Icon(_expanded ? Icons.expand_less : Icons.expand_more),
                ],
              ),
              if (_expanded) ...[
                const SizedBox(height: 12),
                const Divider(),
                const SizedBox(height: 8),
                if (widget.description.isNotEmpty) ...[
                  Text(widget.description, style: theme.textTheme.bodyMedium),
                  const SizedBox(height: 12),
                ],
                if (widget.eventLinkUrl != null && widget.eventLinkUrl!.isNotEmpty)
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: () async {
                        final url = Uri.parse(widget.eventLinkUrl!);
                        if (await canLaunchUrl(url)) {
                          await launchUrl(url);
                        }
                      },
                      style: ElevatedButton.styleFrom(
                      backgroundColor: Color(0xFF1C824C),
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(4),
                        ),
                      ),
                      child: const Text('Inscrever-se'),
                    ),
                  ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}