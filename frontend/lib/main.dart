import 'package:flutter/material.dart';
import 'package:frontend/info_fetch/feed/fetch_feed.dart';
import 'package:frontend/config/org_config.dart';
import 'package:frontend/config/org_config_provider.dart';
import 'package:frontend/config/app_config.dart';
import 'package:frontend/info_fetch/org/fetch_org_config.dart';
import 'package:frontend/page_structure.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const AppBootstrap());
}

/// Carrega a configuração da organização exibindo uma tela de carregamento
/// enquanto o backend responde. Tolera o "cold start" do Render (até ~45s)
/// graças ao timeout em [FetchOrgConfig] e oferece "tentar novamente" em caso
/// de falha.
class AppBootstrap extends StatefulWidget {
  const AppBootstrap({super.key});

  @override
  State<AppBootstrap> createState() => _AppBootstrapState();
}

class _AppBootstrapState extends State<AppBootstrap> {
  late Future<OrgConfig> _configFuture;

  @override
  void initState() {
    super.initState();
    _configFuture = _loadConfig();
  }

  Future<OrgConfig> _loadConfig() {
    return FetchOrgConfig(orgId: kDefaultOrgId).fetchConfig();
  }

  void _retry() {
    setState(() {
      _configFuture = _loadConfig();
    });
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<OrgConfig>(
      future: _configFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const _BootstrapScaffold(child: _LoadingView());
        }
        if (snapshot.hasError || !snapshot.hasData) {
          return _BootstrapScaffold(child: _ErrorView(onRetry: _retry));
        }
        return OrgConfigProvider(
          config: snapshot.data!,
          child: const MyApp(),
        );
      },
    );
  }
}

/// MaterialApp mínimo usado apenas nas telas de bootstrap (carregando/erro),
/// antes de a config real estar disponível.
class _BootstrapScaffold extends StatelessWidget {
  const _BootstrapScaffold({required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: OrgConfig.fallback.primaryColor,
        ),
      ),
      home: Scaffold(
        backgroundColor: Colors.white,
        body: Center(
          child: SingleChildScrollView(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 320),
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: child,
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class _LoadingView extends StatelessWidget {
  const _LoadingView();

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        CircularProgressIndicator(color: OrgConfig.fallback.primaryColor),
        const SizedBox(height: 20),
        const Text(
          'Conectando ao servidor…',
          style: TextStyle(fontSize: 16, color: Color(0xFF505050)),
        ),
        const SizedBox(height: 6),
        const Text(
          'Isso pode levar alguns segundos na primeira vez.',
          textAlign: TextAlign.center,
          style: TextStyle(fontSize: 13, color: Color(0xFF909090)),
        ),
      ],
    );
  }
}

class _ErrorView extends StatelessWidget {
  const _ErrorView({required this.onRetry});

  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        const Icon(Icons.cloud_off, size: 48, color: Color(0xFF909090)),
        const SizedBox(height: 16),
        const Text(
          'Não foi possível conectar ao servidor.',
          textAlign: TextAlign.center,
          style: TextStyle(fontSize: 16, color: Color(0xFF505050)),
        ),
        const SizedBox(height: 20),
        SizedBox(
          width: double.infinity,
          child: ElevatedButton.icon(
            onPressed: onRetry,
            icon: const Icon(Icons.refresh),
            label: const Text('Tentar novamente'),
            style: ElevatedButton.styleFrom(
              backgroundColor: OrgConfig.fallback.primaryColor,
              foregroundColor: Colors.white,
            ),
          ),
        ),
      ],
    );
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key, this.fetchFeed});

  final FetchFeed? fetchFeed;

  @override
  Widget build(BuildContext context) {
    final config = OrgConfigProvider.of(context);

    return MaterialApp(
      title: config.name,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: config.primaryColor,
          primary: config.primaryColor,
          primaryContainer: config.primaryColor.withAlpha(38),
          onPrimaryContainer: config.primaryColor,
          surface: config.backgroundColor,
        ),
      ),
      home: PageStructure(
        initialPageName: 'feed',
        fetchFeed: fetchFeed,
      ),
    );
  }
}
